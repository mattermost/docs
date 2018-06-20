#!/usr/bin/env ruby

require 'optparse'
require 'yaml'

require_relative 'lib/version'
require_relative 'lib/version_fetcher'

Options = Struct.new(
  :working_dir,
  :app_version,
  :chart_version,
  :include_subcharts,
  :dry_run
)

class VersionOptionsParser
  class << self
    def parse(argv)
      options = Options.new

      # defaults
      options.working_dir = Dir.pwd
      options.include_subcharts = false

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

        opts.on("-a", "--include-subcharts", "Attempt to update subcharts as well") do |value|
          options.include_subcharts = value
        end

        opts.on('-n', '--dry-run', "Don't actually write anything, just print") do |value|
          options.dry_run = value
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
    @metadata = YAML.safe_load(File.read(@filepath))
  end

  def name
    @metadata['name']
  end

  def version
    Version.new(@metadata['version'])
  end

  def app_version
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
    @options = options

    populate_chart_version

    msg = ["# New Versions\n# version: #{@chart_version}"]
    msg << "# appVersion: #{@app_version}" if @app_version
    $stdout.puts msg.join("\n")

    populate_subchart_versions if @options.include_subcharts

    return if options.dry_run

    chart.update_versions(@chart_version, @app_version)

    if @options.include_subcharts
      @subchart_versions.each do |sub_chart, update_app_version|
        sub_chart.update_versions(@chart_version, update_app_version)
      end
    end
  end

  def working_dir
    @working_dir ||= File.realpath(@options.working_dir)
  end

  def chart
    @chart ||= ChartFile.new(File.join(working_dir, 'Chart.yaml'))
  end

  def subcharts
    @subcharts ||= Dir[File.join(working_dir, 'charts', 'gitlab', 'charts', '*', 'Chart.yaml')].map { |path| ChartFile.new(path) }
  end

  def populate_subchart_versions
    @subchart_versions = subcharts.map do |sub_chart|
      [ sub_chart, VersionFetcher.fetch(sub_chart.name, @app_version) ]
    end
  end

  def populate_chart_version
    # If we were not passed the new chart version, use the gitlab version to bump it
    unless @chart_version
      app_change = chart.app_version.diff(@app_version)

      # NoOp if app version has not changed
      unless app_change
        $stdout.puts "Version already updated"
        exit
      end

      # If the existing app version isn't semver, we are likely branching from master
      # and are branching to prep for release. Bump the chart version based on the type
      # of release we are doing
      unless chart.app_version.valid?
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
        @chart_version = Version.new("#{chart.version.major + 1}.0.0")
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
