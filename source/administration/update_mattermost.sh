#!/usr/bin/env bash
set -o errexit

################################################################################
# Configuration - please adapt it to your environment
################################################################################

# Path to mattermost directory
mattermostdir="/opt/mattermost"

# Path for backup
backupdir="/opt"

# Temporary path for download
downloaddir="/tmp"

# Specify the edition you use
edition="Team"
#edition="Enterprise"

# Start with plugins? Set 1 for starting with plugins active
plugins=0

# Set 1 for overriding the database backup question
backupdatabase=0

################################################################################

# Check dependencies
#
if ((EUID != 0)); then
    echo "[-] This script needs to be run as root to work properly. Aborting..."
    exit 1
fi

if ! type "systemctl" >/dev/null 2>&1 && ! type "service" >/dev/null 2>&1; then
    echo "[-] Access to the daemon manager (systemd or sysvinit) is not accessible. Aborting..."
    exit 1
fi

if ! type "wget" >/dev/null 2>&1 && ! type "curl" >/dev/null 2>&1; then
    echo "[-] Access to a download tool like (wget or curl) is not accessible. Aborting..."
    exit 1
fi

# Check requirements
if [[ "$edition" != "Team" ]] && [[ "$edition" != "Enterprise" ]]; then
    echo "[-] The edition must aither be \"Team\" or \"Enterprise\"."
    exit 1
fi

# Ask for database backup
if [ $backupdatabase -eq 0 ]; then
    read -r -p "[?] Do you have a current backup of the Mattermost database? [Y/n] " input

    case $input in
        [yY])
            echo "[+] Starting the update process of Mattermost..."
        ;;
        *)
            echo "[-] Please create a backup and start again"
            exit 1
        ;;
    esac
fi

# Check if mattermost exists in the path provided above
if [ ! -f "$mattermostdir/bin/mattermost" ];  then
    echo "Mattermost not found please check the path for the Mattermost directory"
    exit 1
fi

# Get version from argument
if [ -z "$1" ]; then
    echo "Please specify the version of Mattermost to download"
    exit 1
fi
version="$1"

if [[ "$edition" == "Team" ]]; then
    url="https://releases.mattermost.com/$version/mattermost-team-$version-linux-amd64.tar.gz"
else
    url="https://releases.mattermost.com/$version/mattermost-$version-linux-amd64.tar.gz"
fi

# Main

# Delete old backup folder
if [ -d "$backupdir/mattermost-backup" ]; then
    echo "[+] Deleting old mattermost backup..."
    rm -rf "$backupdir/mattermost-backup" 2>/dev/null
fi

# Get the file
echo "[+] Downloading Mattermost $edition \"$version\"..."
if type "curl" >/dev/null 2>&1; then
    if ! curl -LC - "$url" -o "$downloaddir/mattermost-upgrade.tar.gz"; then
        echo "[-] An issue occurred when downloading the Mattermost update package."
        exit 1
    fi
else
    if ! wget "$url" -o "$downloaddir/mattermost-upgrade.tar.gz"; then
        echo "[-] An issue occurred when downloading the Mattermost update package."
        exit 1
    fi
fi

echo "[+] The Mattermost update package has been downloaded with successful"

echo "[+] Extracting Mattermost update package..."
mkdir -p "$downloaddir/mattermost-upgrade"
tar -xf "$downloaddir/mattermost-upgrade.tar.gz" -C "$downloaddir/mattermost-upgrade/"

echo "[+] Stopping Mattermost service..."
if type systemctl >/dev/null 2>&1;  then
    systemctl stop mattermost
else
    service mattermost stop
fi

if pgrep mattermost > /dev/null; then
    echo "[-] Mattermost is still running. Update not possible. Aborting..."
    rm -rf "$downloaddir/mattermost-upgrade"
    rm -f "$downloaddir/mattermost-upgrade.tar.gz"
    exit 1
fi

echo "[+] Creating backup of Mattermost..."
cp -ra "$mattermostdir" "$backupdir/mattermost-backup"

echo "[+]] Preparing update..."
USER="$(stat -c '%U' $mattermostdir/bin/mattermost)"
GROUP="$(stat -c '%G' $mattermostdir/bin/mattermost)"
chown -hR "$USER":"$GROUP" $downloaddir/mattermost-upgrade/

# Clean up mattermost directory
find "$mattermostdir" -mindepth 1 -maxdepth 1 -not \( -path "$mattermostdir/config" -o -path "$mattermostdir/logs" -o -path "$mattermostdir/plugins" -o -path "$mattermostdir/data" \) -delete

# Rename plugin directory
if [ $plugins -eq 0 ];  then
    echo "[+] Renaming plugin folder..."
    mv "$mattermostdir/plugins/" "$mattermostdir/plugins~"
    mv "$mattermostdir/client/plugins/" "$mattermostdir/client/plugins~"
fi

echo "[+] Updating Mattermost..."
cp -an $downloaddir/mattermost-upgrade/. $mattermostdir

echo "[+] Cleaning Mattermost temporary files..."
rm -rf "$downloaddir/mattermost-upgrade/"
rm -f "$downloaddir/mattermost-upgrade.gz"

echo "[+] Starting Mattermost service..."
if type systemctl >/dev/null 2>&1;  then
    systemctl start mattermost
else
    service mattermost start
fi

echo "[+] Mattermost updated with successful"

if [ $plugins -eq 0 ];  then
    echo "*************************************************"
    echo "Dont forget to activate your plugins"
    echo "mv \"$mattermostdir/plugins~\" \"$mattermostdir/plugins\""
    echo "mv \"$mattermostdir/client/plugins\" \"$mattermostdir/client/plugins~\""
    echo "*************************************************"
fi
