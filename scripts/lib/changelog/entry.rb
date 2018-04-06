require 'yaml'
require 'active_support/core_ext/object/blank'

module Changelog
  # Represents a Rugged::Blob and its changelog entry
  class Entry
    attr_reader :author, :blob, :id, :path, :title, :type

    # Types are not sorted by ABC intentionally.
    # The markdown output is generated going through this array down.
    TYPES = %w[
      security
      removed
      fixed
      deprecated
      changed
      performance
      added
      other
    ].freeze

    # path - Path to the blob, relative to the Repository root
    # blob - Underlying Rugged::Blob object
    def initialize(path, blob)
      @path = path
      @blob = blob

      parse_blob(blob.content)
    end

    def to_s
      str = ""
      str << "#{title}.".gsub(/\.{2,}$/, '.')
      str << " !#{id}" if id.present?
      str << " (#{author})" if author.present?

      str
    end

    def valid?
      title.present?
    end

    private

    def parse_blob(content)
      yaml = YAML.safe_load(content)

      @author = yaml['author']
      @id     = parse_id(yaml)
      @title  = yaml['title']
      @type   = parse_type(yaml)
    rescue StandardError # rubocop:disable Lint/HandleExceptions
      # noop
    end

    def parse_id(yaml)
      id = yaml['merge_request'] || yaml['id']
      id.to_s.gsub!(/[^\d]/, '')

      # We don't want `nil` to become `0`
      id.present? ? id.to_i : id
    end

    # Any type (including invalid ones) which are not included in the `TYPES` constant
    # we define as `other`.
    def parse_type(yaml)
      type = yaml['type']&.downcase

      TYPES.include?(type) ? type : 'other'
    end
  end
end
