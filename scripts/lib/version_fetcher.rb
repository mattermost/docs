require_relative 'version'

require 'open-uri'
require 'uri'
require 'cgi'

class VersionFetcher
  def initialize(version, repo)
    @version = Version.new(version) if version
    @repo = repo
    @api_token = ENV['FETCH_DEV_ARTIFACTS_PAT']
    @api_url = if @repo.start_with?('gitlab/')
                 'https://dev.gitlab.org/api/v4'
               elsif @repo.start_with?('gitlab-org/')
                 'https://gitlab.com/api/v4'
               else
                 ENV['CI_API_V4_URL']
               end
  end

  # GitLab Shell Version
  def gitlab_shell
    return @version if @version.nil? || @version == 'master'

    url = "#{@api_url}/projects/#{CGI.escape(@repo)}/repository/files/GITLAB_SHELL_VERSION/raw?ref=#{ref(@version)}"
    $stdout.puts "Getting GitLab Shell version from #{url}"
    new_version = open(url, 'PRIVATE-TOKEN' => @api_token).read.strip
    $stdout.puts "# Shell appVersion: #{new_version}"
    Version.new(new_version)
  end

  # Gitaly Version
  def gitaly
    return @version if @version.nil? || @version == 'master'

    url = "#{@api_url}/projects/#{CGI.escape(@repo)}/repository/files/GITALY_SERVER_VERSION/raw?ref=#{ref(@version)}"
    $stdout.puts "Getting Gitaly version from #{url}"
    new_version = open(url, 'PRIVATE-TOKEN' => @api_token).read.strip
    $stdout.puts "# Gitaly appVersion: #{new_version}"
    Version.new(new_version)
  end

  # GitLab Exporter Version
  def gitlab_exporter
    # Don't edit the appVersion, it get's set manually as monitor isn't released by release-tools
    nil
  end

  def fetch(chart_name)
    chart_name = chart_name.tr('-', '_').to_sym

    # Return the fetch result for the chart if it's defined
    # Otherwise return the parent chart's version
    if respond_to?(chart_name)
      send(chart_name)
    else
      @version
    end
  end

  private

  def ref(version)
    if version.valid?
      version.tag(ee: true)
    else
      version.to_s
    end
  end
end
