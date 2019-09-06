require 'spec_helper'

describe "Restoring a backup" do
  before(:all) do
    stdout, status = wait_for_dependencies
    fail stdout unless status.success?

    wait_until_app_ready
    ensure_backups_on_object_storage
    stdout, status = restore_from_backup
    fail stdout unless status.success?

    # We run migrations once early to get the db into a place where we can set the runner token
    # Ignore errors, we will run the migrations again after the token
    run_migrations

    stdout, status = set_runner_token
    fail stdout unless status.success?

    stdout, status = run_migrations
    fail stdout unless status.success?

    stdout, status = enforce_root_password(ENV['GITLAB_PASSWORD']) if ENV['GITLAB_PASSWORD']
    fail stdout unless status.success?

    stdout, status = restart_unicorn
    fail stdout unless status.success?

    # Wait for the site to come up after the restore/migrations
    wait_until_app_ready
  end

  describe 'Restored gitlab instance' do
    before { sign_in }

    it 'Home page should show projects' do
      visit '/'
      expect(page).to have_content 'Projects'
      expect(page).to have_content 'Administrator / testproject1'
    end

    it 'Navigating to testproject1 repo should work' do
      visit '/root/testproject1'
      expect(page).to have_content 'Dockerfile'
    end

    it 'Should have runner registered' do
      visit '/admin/runners'
      expect(page).to have_css('#content-body div[id^=\'runner_\']', minimum: 1)
    end

    it 'Issue attachments should load correctly' do
      visit '/root/testproject1/issues/1'

      image_selector = 'div.md > p > a > img.js-lazy-loaded'

      # Image has additional classes added by JS async
      wait(reload: false) do
        has_selector?(image_selector)
      end

      expect(page).to have_selector(image_selector)
      image_src = page.all(image_selector)[0][:src]
      open(image_src) do |f|
        expect(f.status[0]).to eq '200'
      end
    end

    it 'Could pull image from registry' do
      stdout, status = Open3.capture2e("docker login #{registry_url} --username root --password #{ENV['GITLAB_PASSWORD']}")
      expect(status.success?).to eq true
      fail "Login failed: #{stdout}" unless status.success?

      stdout, status = Open3.capture2e("docker pull #{registry_url}/root/testproject1/master:d88102fe7cf105b72643ecb9baf41a03070c9f1b")
      fail "Pulling image failed: #{stdout}" unless status.success?
    end

  end

  describe 'Backups' do
    it 'Should be able to backup an identical tar' do
      stdout, status = backup_instance
      fail stdout unless status.success?

      object_storage.get_object(
        response_target: '/tmp/original_backup.tar',
        bucket: 'gitlab-backups',
        key: '0_11.11.3_gitlab_backup.tar'
      )

      cmd = 'mkdir -p /tmp/original_backup && tar -xf /tmp/original_backup.tar -C /tmp/original_backup'
      stdout, status = Open3.capture2e(cmd)
      fail stdout unless status.success?

      object_storage.get_object(
        response_target: '/tmp/test_generated_backup.tar',
        bucket: 'gitlab-backups',
        key: 'test-backup_gitlab_backup.tar'
      )
      cmd = 'mkdir -p /tmp/test_backup && tar -xf /tmp/test_generated_backup.tar -C /tmp/test_backup'
      stdout, status = Open3.capture2e(cmd)
      fail stdout unless status.success?

      Dir.glob("/tmp/original_backup/*") do |file|
        expect(File.exist?("/tmp/test_backup/#{File.basename(file)}")).to be_truthy
        # extract every tar file
        if File.extname(file) == 'tar'
          cmd = "tar -xf #{file} -C /tmp/original_backup"
          stdout, status = Open3.capture2e(cmd)
          fail stdout unless status.success?

          cmd = "tar -xf #{file.gsub('original_backup', 'test_backup')} -C /tmp/test_backup"
          stdout, status = Open3.capture2e(cmd)
          fail stdout unless status.success?
        end
      end

      Dir.glob("/tmp/original_backup/**/*") do |file|
        next if ['tar', '.gz'].include? File.extname(file)
        next if File.directory?(file)
        next if File.basename(file) == 'backup_information.yml'

        test_counterpart = file.gsub('original_backup', 'test_backup')

        expect(File.exist?(test_counterpart)).to be_truthy, "Expected #{test_counterpart} to exist"
        expect(Digest::MD5.hexdigest(File.read(file))).to eq(Digest::MD5.hexdigest(File.read(test_counterpart))),
          "Expected #{file} to equal #{test_counterpart}"
      end
    end
  end
end
