require 'spec_helper'
require_relative '../../../scripts/lib/version_fetcher.rb'

describe VersionFetcher do
  let(:repo_url) { 'https://gitlab.com/gitlab-org/gitlab-ce' }
  let(:uri_response) { URI.parse(repo_url) }
  let(:version_fetcher) { VersionFetcher.new('v11.8.0', repo_url) }

  before do
    allow(URI).to receive(:parse).and_return(uri_response)
    allow(uri_response).to receive(:read).and_return("1.2.3\n")
    allow(version_fetcher).to receive(:gitlab_shell).and_call_original
    allow(version_fetcher).to receive(:gitaly).and_call_original
  end

  describe '#gitlab_shell' do
    it 'returns correct value' do
      expect(version_fetcher.gitlab_shell).to eq('1.2.3')
    end

    describe '#gitaly' do
      it 'returns correct value' do
        expect(version_fetcher.fetch('gitaly')).to eq('1.2.3')
      end
    end

    describe '#fetch' do
      it 'callse subchart methods' do
        expect(version_fetcher).to receive(:gitlab_shell)
        expect(version_fetcher).to receive(:gitaly)
        version_fetcher.fetch('gitlab-shell')
        version_fetcher.fetch('gitaly')
      end
    end
  end
end
