require 'open-uri'

module Gitlab
  def self.included(klass)
    klass.extend(TestHelper)
  end

  module TestHelper
    def full_command(cmd)
      "kubectl exec -it #{pod_name} -- #{cmd}"
    end

    def wait_until_app_ready(retries:30, interval: 10)
      begin
        URI.parse(gitlab_url).read
      rescue
        sleep interval
        retries -= 1
        retry if retries > 0
      end
    end

    def sign_in
      visit '/users/sign_in'

      # Return if already signed in
      return if has_selector?('.qa-user-avatar')

      fill_in 'Username or email', with: 'root'
      fill_in 'Password', with: ENV['GITLAB_PASSWORD']
      click_button 'Sign in'
      page.save_screenshot("/tmp/screenshots/sign_in.png")
    end

    def enforce_root_password(password)
      rails_dir = ENV['RAILS_DIR'] || '/srv/gitlab'
      cmd = full_command("#{rails_dir}/bin/rails runner \"user = User.find(1); user.password='#{password}'; user.password_confirmation='#{password}'; user.save!\"")

      stdout, status = Open3.capture2e(cmd)
      return [stdout, status]
    end

    def gitlab_url
      protocol = ENV['PROTOCOL'] || 'https'
      instance_url = ENV['GITLAB_URL'] || "gitlab.#{ENV['GITLAB_ROOT_DOMAIN']}"
      "#{protocol}://#{instance_url}"
    end

    def registry_url
      ENV['REGISTRY_URL'] || "registry.#{ENV['GITLAB_ROOT_DOMAIN']}"
    end

    def restore_from_backup
      backup = ENV['BACKUP_TIMESTAMP'] || '0_11.3.4-ee'
      cmd = full_command("backup-utility --restore -t #{backup}")
      stdout, status = Open3.capture2e(cmd)

      return [stdout, status]
    end

    def backup_instance
      cmd = full_command("backup-utility --backup -t test-backup")
      stdout, status = Open3.capture2e(cmd)

      return [stdout, status]
    end

    def run_migrations
      cmd = full_command("gitlab-rake db:migrate")

      stdout, status = Open3.capture2e(cmd)
      return [stdout, status]
    end

    def pod_name
      filters = 'app=task-runner'

      if ENV['RELEASE_NAME']
        filters="#{filters},release=#{ENV['RELEASE_NAME']}"
      end

      @pod ||= `kubectl get pod -l #{filters} -o jsonpath="{.items[0].metadata.name}"`
    end

    def object_storage
      return @object_storage if @object_storage

      if ENV['S3_CONFIG_PATH']
        s3_access_key = File.read("#{ENV['S3_CONFIG_PATH']}/accesskey")
        s3_secret_key = File.read("#{ENV['S3_CONFIG_PATH']}/secretkey")
      end

      s3_access_key ||= ENV['S3_ACCESS_KEY']
      s3_secret_key ||= ENV['S3_SECRET_KEY']

      conf = {
        region: ENV['S3_REGION'] || 'us-east-1',
        access_key_id: s3_access_key,
        secret_access_key: s3_secret_key,
        endpoint: ENV['S3_ENDPOINT'],
        force_path_style: true
      }

      @object_storage = Aws::S3::Client.new(conf)
    end

    def ensure_backups_on_object_storage
      storage_url = 'https://storage.googleapis.com/gitlab-charts-ci/test-backups'
      backup_file_names = ['11.3.4-ee_gitlab_backup.tar']
      backup_file_names.each do |file_name|
        file = open("#{storage_url}/#{file_name}").read
        object_storage.put_object(
          bucket: 'gitlab-backups',
          key: "0_#{file_name}",
          body: file
        )
        puts "Uploaded #{file_name}"
      end
    end
  end
end
