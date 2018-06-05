#!/usr/bin/env ruby

require 'optparse'
require 'yaml'

require_relative 'lib/version'

Options = Struct.new(
  :working_dir,
  :app_version,
  :chart_version
)

class VersionOptionsParser
  class << self
    def parse(argv)
      options = Options.new()
      options.working_dir = Dir.pwd

      OptionParser.new do |opts|
        opts.banner = "Usage: #{__FILE__} [options] \n\n"

        opts.on("--app-version [string]", String, "GitLab Application Version") do |value|
          options.app_version = Version.new(value)
        end

        opts.on("--chart-version [string]", String, "Chart Package Version") do |value|
          options.chart_version = Version.new(value)
        end

        opts.on("-d", "--directory [string]", String, "Working directory for the script") do |value|
          options.working_dir = value
        end

        opts.on('-h', '--help', 'Print help message') do
          $stdout.puts opts
          exit
        end
      end.parse!

      unless (options.app_version && options.app_version.valid?) || (options.chart_version && options.chart_version.valid?)
        $stderr.puts "Must specify a valid --app-version or --chart-version in the syntax 'x.x.x' eg: 11.0.0"
        exit 1
      end

      unless Dir.exist?(options.working_dir)
        $stderr.puts "Must provide a valid working directory"
        exit 1
      end

      options
    end
  end
end

# Grab current Chart versions
class ChartFile
  attr_reader :metadata

  def initialize(filepath)
    unless filepath && File.exist?(filepath)
      $stderr.puts "Chart file must exist"
      exit 1
    end
    @filepath = filepath

    $stdout.puts "Reading #{@filepath}"
    @metadata = YAML.load(File.read(@filepath))
  end

  def version
    Version.new(@metadata['version'])
  end

  def appVersion
    Version.new(@metadata['appVersion'])
  end

  def update_versions(chart_version = nil, app_version = nil)
    @metadata['version'] = chart_version.to_s if chart_version
    @metadata['appVersion'] = app_version.to_s if app_version

    $stdout.puts "Updating #{@filepath}"
    File.write(@filepath, YAML.dump(@metadata))
  end
end

class VersionUpdater
  def initialize(options)
    @chart_version = options.chart_version
    @app_version = options.app_version
    @working_dir = options.working_dir

    @chart = ChartFile.new(File.join(@working_dir, 'Chart.yaml'))

    populate_chart_version

    # Set versions
    $stdout.puts "# New Versions\n# version: #{@chart_version}\n# appVersion: #{@app_version}"
    @chart.update_versions(@chart_version, @app_version)
  end

  def populate_chart_version
    # If we were not passed the new chart version, use the gitlab version to bump it
    unless @chart_version
      app_change = @chart.appVersion.diff(@app_version)

      # NoOp if app version has not changed
      unless app_change
        $stdout.puts "Version already updated"
        exit
      end

      # If the existing app version isn't semver, we are likely branching from master
      # and are branching to prep for release. Bump the chart version based on the type
      # of release we are doing
      unless @chart.appVersion.valid?
        if @app_version.minor.zero? && @app_version.patch.zero?
          app_change = Version::MAJOR
        elsif @app_version.patch.zero?
          app_change = Version::MINOR
        else
          app_change = Version::PATCH
        end
      end

      case app_change
      when Version::MAJOR
        @chart_version = Version.new("#{chart.version.major+1}.0.0")
      when Version::MINOR
        @chart_version = Version.new(chart.version.next_minor)
      when Version::PATCH
        @chart_version = Version.new(chart.version.next_patch)
      else
        @chart_version = chart.version
      end
    end
  end
end

# Only auto-run when called as a script, and not included as a lib
if $0 == __FILE__
  options = VersionOptionsParser.parse(ARGV)
  VersionUpdater.new(options)
  $stdout.puts "Complete"
end
