require 'spec_helper'

load File.expand_path('../../scripts/manage_version.rb', __dir__)

describe 'scripts/manage_version.rb' do
  describe VersionUpdater do
    let(:chart_file) { instance_double("ChartFile") }
    let(:options) { Options.new }

    before do
      allow_any_instance_of(described_class).to receive(:subcharts).and_return([])
      allow_any_instance_of(described_class).to receive(:chart).and_return(chart_file)
      allow_any_instance_of(described_class).to receive(:working_dir).and_return(nil)
    end

    describe 'populate_chart_version' do
      context 'chart_version and app_version provided' do
        it 'sets the correct versions' do
          stub_versions(new_version: 'chart-version', new_app_version: 'app-version')

          expect(chart_file).to receive(:update_versions).with('chart-version', 'app-version')
          described_class.new(options)
        end
      end

      context 'app_version not provided' do
        it 'sets the correct versions' do
          stub_versions(new_version: 'chart-version')

          expect(chart_file).to receive(:update_versions).with('chart-version', nil)
          described_class.new(options)
        end
      end

      context 'chart_version not provided' do
        it 'exits if app_version has not changed' do
          stub_versions(app_version: '0.0.1', new_app_version: '0.0.1')

          expect do
            expect { described_class.new(options) }.to output.to_stdout
          end.to raise_error(SystemExit)
        end

        context 'from master branch' do
          it 'increases chart patch when receiving an app patch' do
            stub_versions(version: '0.0.1', app_version: 'master', new_app_version: '10.8.1')

            expect(chart_file).to receive(:update_versions).with('0.0.2', '10.8.1')
            described_class.new(options)
          end

          it 'increases chart minor when receiving an app minor' do
            stub_versions(version: '0.0.1', app_version: 'master', new_app_version: '10.8.0')

            expect(chart_file).to receive(:update_versions).with('0.1.0', '10.8.0')
            described_class.new(options)
          end

          it 'increases chart major when receiving an app major' do
            stub_versions(version: '0.0.1', app_version: 'master', new_app_version: '11.0.0')

            expect(chart_file).to receive(:update_versions).with('1.0.0', '11.0.0')
            described_class.new(options)
          end

          it 'increases chart version when receiving RC in a way that matches non-RC behaviour' do
            stub_versions(version: '0.0.1', app_version: 'master', new_app_version: '11.0.0-rc1')

            expect(chart_file).to receive(:update_versions).with('1.0.0', '11.0.0-rc1')
            described_class.new(options)
          end
        end

        it 'increases chart patch when receiving an app patch' do
          stub_versions(version: '0.0.1', app_version: '10.8.0', new_app_version: '10.8.1')

          expect(chart_file).to receive(:update_versions).with('0.0.2', '10.8.1')
          described_class.new(options)
        end

        it 'increases chart minor when receiving an app minor' do
          stub_versions(version: '0.0.1', app_version: '10.7.5', new_app_version: '10.8.1')

          expect(chart_file).to receive(:update_versions).with('0.1.0', '10.8.1')
          described_class.new(options)
        end

        it 'increases chart major when receiving an app major' do
          stub_versions(version: '0.0.1', app_version: '10.8.5', new_app_version: '11.1.5')

          expect(chart_file).to receive(:update_versions).with('1.0.0', '11.1.5')
          described_class.new(options)
        end

        it 'completely chart version changes when app version has only changed by RC' do
          stub_versions(version: '0.0.1', app_version: '11.0.0-rc1', new_app_version: '11.0.0-rc2')

          expect(chart_file).to receive(:update_versions).with('0.0.1', '11.0.0-rc2')
          described_class.new(options)
        end
      end
    end
  end
end

def stub_versions(new_version: nil, version: '0.0.1', new_app_version: nil, app_version: '0.0.1')
  options.chart_version = Version.new(new_version) if new_version
  options.app_version = Version.new(new_app_version) if new_app_version

  allow(chart_file).to receive(:version).and_return(Version.new(version)) if version
  allow(chart_file).to receive(:app_version).and_return(Version.new(app_version)) if app_version
  allow(chart_file).to receive(:update_versions).and_return(true)
end
