#!/bin/sh

PW_FILE='/tmp/initial/password'

# If the password file exists, set the admin password using the contents
if [ -r "$PW_FILE" ]; then
    echo "GitLab shim: Setting admin username to root"
    export GF_SECURITY_ADMIN_USER="root"

    read -r line < "$PW_FILE"
    echo "GitLab shim: Setting admin password in environment"
    export GF_SECURITY_ADMIN_PASSWORD="$line"
fi

# Start up the full grafana service
exec /run.sh
