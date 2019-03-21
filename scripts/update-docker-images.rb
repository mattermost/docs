#!/usr/bin/env ruby

require 'docker'
require 'yaml'
require 'net/http'
require 'json'
require 'cgi'
require 'zip'

class CNGImageSync
  CI_API_V4_URL = ENV['CI_API_V4_URL'] || "https://dev.gitlab.org/api/v4".freeze
  DEV_REGISTRY_URL = "dev.gitlab.org:5005".freeze
  COM_REGISTRY_URL = "registry.gitlab.com".freeze
  DEV_PROJECT_PATH = ENV['DEV_CNG_PROJECT'] || "gitlab/charts/components/images".freeze
  COM_PROJECT_PATH = ENV['COM_CNG_PROJECT'] || "gitlab-org/build/cng".freeze
  DEV_PROJECT_REGISTRY = ENV['DEV_CNG_REGISTRY'] || "#{DEV_REGISTRY_URL}/#{DEV_PROJECT_PATH}".freeze
  COM_PROJECT_REGISTRY = ENV['COM_CNG_REGISTRY'] || "#{COM_REGISTRY_URL}/#{COM_PROJECT_PATH}".freeze
  DEV_REGISTRY_PASSWORD = ENV['DEV_API_TOKEN'] || ENV['CI_JOB_TOKEN']
  COM_REGISTRY_PASSWORD = ENV['COM_API_TOKEN']

  GITLAB_VERSION = YAML.load_file('Chart.yaml')['appVersion'].strip.freeze

  class << self
    def get_api(uri, token=ENV['DEV_API_TOKEN'])
      req = Net::HTTP::Get.new(uri)
      req['PRIVATE-TOKEN'] = token
      res = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
        http.request(req)
      end

      res
    end

    def get_components(version)
      artifact_uri = URI("#{CI_API_V4_URL}/projects/#{CGI.escape(DEV_PROJECT_PATH)}/jobs/artifacts/v#{version}-ee/raw/artifacts/image_versions.txt?job=component-details")
      puts "Fetching component list from #{artifact_uri}"
      res = get_api(artifact_uri)
      components = res.body.split("\n")
      components.map { |c| c.split(":") }.to_h
    end

    def authenticate_registry(registry, password)
      Docker.authenticate!(username: ENV['CI_REGISTRY_USER'], password: password, serveraddress: registry)
    end

    def pull_and_tag_images(initial_registry, new_registry, components)
      components.each do |component, version|
        initial_ref = "#{initial_registry}/#{component}:#{version}".downcase
        target_repo = "#{new_registry}/#{component}".downcase
        puts "Pulling #{initial_ref}"
        STDOUT.flush

        image = Docker::Image.create(fromImage: initial_ref)
        image.tag(repo: target_repo, tag: version)
      end
    end

    def push_images(registry, components)
      components.each do |component, version|
        ref = "#{registry}/#{component}:#{version}".downcase
        puts "Pushing #{ref}"
        STDOUT.flush
        image = Docker::Image.get(ref)
        image.push(nil, repo_tag: ref)
      end
    end

    def check_auth
      message = <<~MESSAGE
          Login credentials for registries are missing. Make sure the following environment variables are set
            COM_API_TOKEN - PAT with access to gitlab.com API
      MESSAGE
      raise message if COM_REGISTRY_PASSWORD.nil?
    end

    def execute
      check_auth

      puts "Syncing images for version #{GITLAB_VERSION}"
      components = get_components(GITLAB_VERSION)

      authenticate_registry(DEV_REGISTRY_URL, DEV_REGISTRY_PASSWORD)
      pull_and_tag_images(DEV_PROJECT_REGISTRY, COM_PROJECT_REGISTRY, components)

      authenticate_registry(COM_REGISTRY_URL, COM_REGISTRY_PASSWORD)
      push_images(COM_PROJECT_REGISTRY, components)

      puts "Sync completed"
    end
  end
end
