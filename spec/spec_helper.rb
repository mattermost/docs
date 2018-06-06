RSpec.configure do |config|
  config.run_all_when_everything_filtered = true
  config.filter_run :focus
  config.order = 'random'

  config.mock_with :rspec do |mocks|
    mocks.verify_partial_doubles = true
  end

  config.around(:example, :silence_stdout) do |example|
    expect { example.run }.to output.to_stdout
  end

  config.around(:example, :silence_stderr) do |example|
    expect { example.run }.to output.to_stderr
  end
end
