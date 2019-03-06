require_relative 'version'

require 'open-uri'
require 'uri'

class VersionFetcher
  class << self

    # GitLab Shell Version
    def gitlab_shell(version, repo)
      return version if version == 'master'

      url = "#{repo}/raw/#{ref(version)}/GITLAB_SHELL_VERSION"
      new_version = URI.parse(url).read.strip
      $stdout.puts "# Shell appVersion: #{new_version}"
      new_version
    end

    # Gitaly Version
    def gitaly(version, repo)
      return version if version == 'master'

      url = "#{repo}/raw/#{ref(version)}/GITALY_SERVER_VERSION"
      new_version = URI.parse(url).read.strip
      $stdout.puts "# Gitaly appVersion: #{new_version}"
      new_version
    end

    def fetch(chart_name, ref, repo)
      chart_name = chart_name.tr('-', '_').to_sym
      return ref unless respond_to?(chart_name)
      Version.new(send(chart_name, ref, repo)) if ref
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
end
