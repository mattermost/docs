require_relative 'version'

require 'net/http'
require 'uri'

class VersionFetcher
  class << self

    # GitLab Shell Version
    define_method 'gitlab-shell'.to_sym do |version|
      return version if version == 'master'

      new_version = Net::HTTP.get(URI.parse("https://gitlab.com/gitlab-org/gitlab-ee/raw/#{ref(version)}/GITLAB_SHELL_VERSION")).strip
      $stdout.puts "# Shell appVersion: #{new_version}"
      new_version
    end

    # Gitaly Version
    def gitaly(version)
      return version if version == 'master'

      new_version = Net::HTTP.get(URI.parse("https://gitlab.com/gitlab-org/gitlab-ee/raw/#{ref(version)}/GITALY_SERVER_VERSION")).strip
      $stdout.puts "# Gitaly appVersion: #{new_version}"
      new_version
    end

    def fetch(chart_name, ref)
      return ref unless include?(chart_name.to_sym)
      Version.new(send(chart_name.to_sym, ref))
    end

    def include?(chart_name)
      respond_to?(chart_name.to_sym)
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
