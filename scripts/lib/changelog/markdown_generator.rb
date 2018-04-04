require 'active_support/inflector'

module Changelog
  class MarkdownGenerator
    attr_reader :version, :entries

    def initialize(version, entries)
      @version = version
      @entries = entries.select(&:valid?)
    end

    def to_s
      markdown = StringIO.new

      if !entries.empty?
        markdown.puts header
        markdown.puts
        markdown.puts formatted_entries
      end

      markdown.string
    end

    private

    def header
      "## #{version.to_s}"
    end

    # Select entries where the `author` field is not empty.
    # This field is filled in only by community contributors.
    def entries_from_community(entries)
      entries.select(&:author)
    end

    # Select entries for given type.
    def entries_grouped_by_type(type)
      entries_sorted_by_id.select { |entry| entry.type == type }
    end

    # Sort entries in ascending order by ID
    #
    # Entries without an ID are placed last
    def entries_sorted_by_id
      entries.sort do |a, b|
        (a.id || 999_999).to_i <=> (b.id || 999_999).to_i
      end
    end

    # Group entries by type found in the `Changelog::Entry::TYPES`.
    # Output example:
    #
    # ### Fixed (52 changes, 16 of them are from community)
    # - Fix 404 errors in API caused when the branch name had a dot. !14462 (gvieira37)
    def formatted_entries
      result = ''

      Changelog::Entry::TYPES.each do |type|
        grouped_entries = entries_grouped_by_type(type)
        changes_count = grouped_entries.size

        # Do nothing if no changes are presented for the current type.
        next unless changes_count.positive?

        community_entries_count = entries_from_community(grouped_entries).size

        # Prepare the group header.
        # Example:
        # ### Added (54 changes, 15 of them are from the community)
        changes = [changes_count, 'change'.pluralize(changes_count)].join("\s")

        if community_entries_count.positive?
          verb = community_entries_count > 1 ? 'are' : 'is'
          changes << ", #{community_entries_count} of them #{verb} from the community"
        end

        result << "### #{type.capitalize} (#{changes})\n\n"

        # Add entries to the group.
        grouped_entries.each { |entry| result << "- #{entry}\n" }

        result << "\n"
      end

      result
    end
  end
end
