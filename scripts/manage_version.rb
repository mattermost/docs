#!/usr/bin/env ruby

require 'optparse'
require 'yaml'

require_relative 'lib/version'

# Grab current versions
class ChartFile
  attr_reader :metadata

  def initialize(filepath)
    unless filepath && File.exist?(filepath)
      $stderr.puts "Chart file must exist"
      exit 1
    end
    @filepath = filepath

    @metadata = YAML.load(File.read(filepath))
  end

  def version
    Version.new(@metadata['version'])
  end

  def appVersion
    Version.new(@metadata['appVersion'])
  end
end

# Set versions


# Accept chart version or gitlab app version
options = {
  working_dir: Dir.pwd
}

OptionParser.new do |opts|
  opts.banner = "Usage: #{__FILE__} [options] \n\n"

  opts.on("--app-version [string]", String, "GitLab Application Version") do |value|
    options[:app_version] = Version.new(value)
  end

  opts.on("--chart-version [string]", String, "Chart Package Version") do |value|
    options[:chart_version] = Version.new(value)
  end

  opts.on("-d", "--directory [string]", String, "Working directory for the script") do |value|
    options[:working_dir] = value
  end

  opts.on('-h', '--help', 'Print help message') do
    $stdout.puts opts
    exit
  end
end.parse!

unless (options[:app_version] && options[:app_version].valid?) && (options[:chart_version] && options[:chart_version].valid?)
  $stderr.puts "Must specify a valid --app-version or --chart-version in the syntax 'x.x.x' eg: 11.0.0"
  exit 1
end

unless Dir.exist?(options[:working_dir])
  $stderr.puts "Must provide a valid working directory"
  exit 1
end

chart = ChartFile.new(File.join(options[:working_dir], 'Chart.yaml'))

# If we were not passed the new chart version, use the gitlab version to bump it
unless options[:chart_version]
  # No Op if app version has not changed
  if options[:app_version] == chart.appVersion
    $stdout.puts "Version already updated"
    exit
  end
end

$stdout.puts "#{chart.version} + #{chart.appVersion}"
