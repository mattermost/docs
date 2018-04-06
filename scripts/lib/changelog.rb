require_relative 'changelog/manager'

module Changelog
  class NoChangelogError < StandardError
    attr_reader :changelog_path

    def initialize(changelog_path)
      @changelog_path = changelog_path
    end
  end
end
