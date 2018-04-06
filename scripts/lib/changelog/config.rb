module Changelog
  class Config
    def self.log
      'CHANGELOG.md'
    end

    def self.paths
      [File.join(root_path, 'unreleased')]
    end

    def self.extension
      '.yml'
    end

    def self.root_path
      'changelogs'
    end
  end
end
