#!/usr/bin/env ruby

require 'docker'
require 'yaml'
require 'net/http'
require 'json'
require 'cgi'

class CNGImageSync
  CI_API_V4_URL = ENV['CI_API_V4_URL'] || "https://dev.gitlab.org/api/v4".freeze
  DEV_REGISTRY_URL = "dev.gitlab.org:5005".freeze
  COM_REGISTRY_URL = "registry.gitlab.com".freeze
  DEV_PROJECT_PATH = ENV['DEV_CNG_PROJECT'] || "gitlab/charts/components/images".freeze
  COM_PROJECT_PATH = ENV['COM_CNG_PROJECT'] || "gitlab-org/build/cng".freeze
  DEV_PROJECT_REGISTRY = ENV['DEV_CNG_REGISTRY'] || "#{DEV_REGISTRY_URL}/#{DEV_PROJECT_PATH}".freeze
  COM_PROJECT_REGISTRY = ENV['COM_CNG_REGISTRY'] || "#{COM_REGISTRY_URL}/#{COM_PROJECT_PATH}".freeze
  DEV_REGISTRY_USERNAME = ENV['DEV_REGISTRY_USERNAME'] || 'gitlab-ci-token'.freeze
  DEV_REGISTRY_PASSWORD = ENV['DEV_REGISTRY_PASSWORD'] || ENV['CI_JOB_TOKEN']
  COM_REGISTRY_USERNAME = ENV['COM_REGISTRY_USERNAME']
  COM_REGISTRY_PASSWORD = ENV['COM_REGISTRY_PASSWORD']


  GITLAB_VERSION = YAML.load_file('Chart.yaml')['appVersion'].strip.freeze
  # All the components that aren't listed here, use `latest` as image tag.
  SPECIFIC_VERSION_MAPPING = {
    "gitlab-rails-ee"=> GITLAB_VERSION,
    "gitlab-task-runner-ee"=> GITLAB_VERSION,
    "gitlab-unicorn-ee"=> GITLAB_VERSION,
    "gitlab-sidekiq-ee"=> GITLAB_VERSION,
    "gitlab-workhorse-ee"=> GITLAB_VERSION,
    "cfssl-self-sign"=> YAML.load_file('charts/shared-secrets/values.yaml')['selfsign']['image']['tag'],
    "alpine-certificates"=> YAML.load_file('values.yaml')['global']['certificates']['image']['tag'],
    "gitlab-shell"=> YAML.load_file('charts/gitlab/charts/gitlab-shell/Chart.yaml')['appVersion'],
    "gitaly"=> YAML.load_file('charts/gitlab/charts/gitaly/Chart.yaml')['appVersion'],
  }.freeze

  class << self
    def get_api(uri, token=ENV['DEV_API_TOKEN'])
      req = Net::HTTP::Get.new(uri)
      req['PRIVATE-TOKEN'] = token
      res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
        http.request(req)
      end

      res
    end

    # Get the commit associated to a tag
    def get_tag_commit(tag)
      tags_uri = URI("#{CI_API_V4_URL}/projects/#{CGI.escape(PROJECT_PATH)}/repository/tags/#{tag}")
      res = get_api(tags_uri)
      JSON.parse(res.body)['commit']['id']
    end

    def get_last_pipeline(commit)
      commit_uri = URI("#{CI_API_V4_URL}/projects/#{CGI.escape(PROJECT_PATH)}/repository/commits/#{commit}")
      res = get_api(commit_uri)
      JSON.parse(res.body)['last_pipeline']['id']
    end

    def get_jobs_in_pipeline(pipeline_id)
      jobs_uri = URI("#{CI_API_V4_URL}/projects/#{CGI.escape(PROJECT_PATH)}/pipelines/#{pipeline_id}/jobs")
      res = get_api(jobs_uri)
      JSON.parse(res.body).map { |x| x['name'] }
    end

    def get_components(version)
      commit = get_tag_commit(version)
      puts "Commit for tag #{version} is #{commit}"
      pipeline = get_last_pipeline(commit)
      puts "Last pipeline for commit #{commit} is : #{pipeline}"

      get_jobs_in_pipeline(pipeline)
    end

    def authenticate_registry(registry, username, password)
      Docker.authenticate!(username: username, password: password, serveraddress: registry)
    end

    def pull_and_tag_images(initial_registry, new_registry, components)
      components.each do |component|
        version = SPECIFIC_VERSION_MAPPING["#{component}"] || "latest"
        puts "#{component}:#{version}"
        initial_ref = "#{initial_registry}/#{component}:#{version}".downcase
        target_repo = "#{new_registry}/#{component}".downcase

        image = Docker::Image.create(fromImage: initial_ref)
        image.tag(repo: target_repo, tag: version)
      end
    end

    def push_images(registry, components)
      components.each do |component|
        version = SPECIFIC_VERSION_MAPPING[component] || "latest"
        ref = "#{registry}/#{component}:#{version}".downcase
        image = Docker::Image.get(ref)
        image.push(nil, repo_tag: ref)
      end
    end

    def check_auth
      message = <<~MESSAGE
          Login credentials for registries are missing. Make sure the following environment variables are set
            DEV_REGISTRY_USERNAME - Username to access docker registry on dev (Ignore if on Dev CI)
            DEV_REGISTRY_PASSWORD - Password to access docker registry on dev (Ignore if on Dev CI)
            COM_REGISTRY_USERNAME - Username to access docker registry on com
            COM_REGISTRY_PASSWORD - Password to access docker registry on com
      MESSAGE
      raise message if DEV_REGISTRY_USERNAME.nil? || DEV_REGISTRY_PASSWORD.nil? || COM_REGISTRY_USERNAME.nil? || COM_REGISTRY_PASSWORD.nil?
    end

    def execute
      check_auth

      puts "Syncing images for version #{GITLAB_VERSION}"
      components = get_components(GITLAB_VERSION)

      authenticate_registry(DEV_REGISTRY_URL, DEV_REGISTRY_USERNAME, DEV_REGISTRY_PASSWORD)
      pull_and_tag_images(DEV_PROJECT_REGISTRY, COM_PROJECT_REGISTRY, components)

      authenticate_registry(COM_REGISTRY_URL, COM_REGISTRY_USERNAME, COM_REGISTRY_PASSWORD)
      push_images(COM_PROJECT_REGISTRY, components)

      puts "Sync completed"
    end
  end
end
