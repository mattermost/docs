Backup
======

To back up you Mattermost server: 

1. Backup your Mattermost database using standard commands for MySQL or PostgreSQL.
2. Backup server settings stored in your `config/config.json` file.
3. Backup files shared by users, including profile pics, stored in one of the following locations: 
   - S3, if you store files in S3
   - Your `./data` directory if you use local storage in the default location
   - If you're using local storage and set a custom directory in your `config/config.json` file using the `Directory` setting, back up that directory.
