require 'rugged'

require_relative 'config'
require_relative 'entry'
require_relative 'markdown_generator'
require_relative 'updater'

module Changelog
  # Manager collects the unreleased changelog entries from a Version's stable
  # branch, and then performs the following actions:
  #
  # 1. Compiles their contents into Markdown, updating the overall changelog
  #    document(s).
  # 2. Removes them from the repository.
  # 3. Commits the changes.
  #
  # These steps are performed on both the stable _and_ the `master` branch,
  # keeping them in sync.
  #
  # Because `master` is never merged into a `stable` branch, we aren't concerned
  # with the commits differing.
  #
  # In the case of an EE release, things get slightly more complex. We perform
  # the same steps above with the EE paths (e.g., `CHANGELOG-EE.md` and
  # `changes/unreleased-ee/`), then perform them _again_ but with the CE paths
  # (e.g., `CHANGELOG.md` and `changes/unreleased/`).
  #
  # This is necessary because by the time this process is performed, CE has
  # already been merged into EE without the consolidated `CHANGELOG.md`.
  class Manager
    attr_reader :repository, :version

    # repository - Rugged::Repository object or String path to repository
    def initialize(repository)
      case repository
      when String
        @repository = Rugged::Repository.new(repository)
      when Rugged::Repository
        @repository = repository
      else
        raise "Invalid repository: #{repository}"
      end
    end

    def release(version)
      @unreleased_entries = nil
      @version = version

      perform_release('master')
    end

    #private

    attr_reader :ref, :commit, :tree, :index

    def changelog_file
      Config.log
    end

    def unreleased_paths
      Config.paths
    end

    def perform_release(branch_name)
      checkout(branch_name)

      update_changelog

      remove_processed_entries
      create_commit
    end

    # Checkout the specified branch and update `ref`, `commit`, `tree`, and
    # `index` with the current state of the repository.
    #
    # branch_name - Branch name to checkout
    def checkout(branch_name)
      @ref    = repository.checkout(branch_name)
      @commit = @ref.target.target
      @tree   = @commit.tree
      @index  = repository.index

      @index.read_tree(commit.tree)
    end

    # Updates `changelog_file` with the Markdown built from the individual
    # unreleased changelog entries.
    #
    # Raises `NoChangelogError` if the changelog blob does not exist.
    def update_changelog
      blob = repository.blob_at(repository.head.target_id, changelog_file)

      raise ::Changelog::NoChangelogError.new(changelog_file) if blob.nil?

      updater  = Updater.new(blob.content, version)
      markdown = MarkdownGenerator.new(version, unreleased_entries).to_s

      changelog_oid = repository.write(updater.insert(markdown), :blob)
      index.add(path: changelog_file, oid: changelog_oid, mode: 0o100644)
    end

    def remove_processed_entries
      return if unreleased_entries.empty?

      index.remove_all(unreleased_entries.collect(&:path))
    end

    def create_commit
      Rugged::Commit.create(
        repository,
        tree: index.write_tree(repository),
        message: "Update #{changelog_file} for #{version}\n\n[ci skip]",
        parents: [commit],
        update_ref: 'HEAD'
      )

      repository.checkout_head(strategy: :force)
    end

    # Build an Array of `Changelog::Entry` objects
    #
    # Raises `RuntimeError` if the repository tree could not be read.
    #
    # Returns an Array
    def unreleased_entries
      return @unreleased_entries if @unreleased_entries

      raise "Cannot gather changelog blobs." unless tree

      @unreleased_entries = []

      tree.walk(:preorder) do |root, entry|
        next unless unreleased_paths.any? { |path| root.start_with?("#{path}/") }
        next unless entry[:name].end_with?(Config.extension)

        @unreleased_entries << Entry.new(
          File.join(root, entry[:name]),
          repository.lookup(entry[:oid])
        )
      end

      @unreleased_entries
    end
  end
end
