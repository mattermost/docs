#!/usr/bin/env ruby
#
# Generate a changelog entry file in the correct location.
#
# Automatically stages the file and amends the previous commit if the `--amend`
# argument is used.

require_relative 'lib/changelog'

manager = Changelog::Manager.new(File.realpath(ARGV[0]))
release = ChangelogVersion.new(Time.new.strftime("%Y-%m-%d"))
manager.release(release)

# vim: ft=ruby
