#!/bin/bash

##Configuration - please adapt it to your environment
#path to mattermost directory
mattermostdir=/usr/mattermost2
#path for backup
backupdir=/usr
#temporary path for download
downloaddir=/tmp
#Team or Enterprise edition? Set 1 for team edition
teamedition=0
#start with plugins? Set 1 for starting with plugins active
plugins=0
#########

##set version number from argument
version=$1

#set variable for echo output
if [ $teamedition -ne 0 ]; then
        edition=Team
        downloadlocation=https://releases.mattermost.com/$version/mattermost-team-$version-linux-amd64.tar.gz
else
        edition=Enterprise
        downloadlocation=https://releases.mattermost.com/$version/mattermost-$version-linux-amd64.tar.gz
fi

#delete old backup folder
if [ -d "$backupdir/mattermost-backup" ]; then
        echo Deleting old mattermost backup
        rm -rf $backupdir/mattermost-backup
fi

###Get the file
echo Downloading Mattermost $edition $version
wget $downloadlocation -P $downloaddir -q

#Stop if download fails
if [ $? -ne 0 ]; then
        echo Mattermost download failed
        exit 1
fi
echo Download successfull

#unpack the tar file
echo unpacking
tar -x --transform='s,^[^/]\+,\0-upgrade,' -f $downloaddir/mattermost*.gz -C $downloaddir

#stopping mattermost service
echo Stopping Mattermost service
if [ -f /bin/systemctl ];  then
        servicecommand="systemctl stop mattermost"
else
        servicecommand="service mattermost stop"
fi
$servicecommand

#check if mattermost is still running
if pgrep mattermost > /dev/null
then
        echo Mattermost still running. Update not possible.
        echo cleaning
        rm -rf $downloaddir/mattermost-upgrade/
        rm -f $downloaddir/mattermost*.gz
        exit 1
fi

echo Create backup of mattermost directory
cp -ra $mattermostdir/ $backupdir/mattermost-backup/

#get file owner and group
echo Preparing update
USER=$(stat -c '%U' $mattermostdir/bin/mattermost)
GROUP=$(stat -c '%G' $mattermostdir/bin/mattermost)
chown -hR $USER:$GROUP $downloaddir/mattermost-upgrade/
#clean up mattermost directory
find $mattermostdir/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path $mattermostdir/config -o -path $mattermostdir/logs -o -path $mattermostdir/plugins -o -path $mattermostdir/data \) -prune \) | sudo xargs rm -r

#rename plugin directory
if [ $plugins -eq 0 ];  then
        echo Renaming plugin folder
        mv $mattermostdir/plugins/ $mattermostdir/plugins~
fi

#copy update
echo Updating
cp -an $downloaddir/mattermost-upgrade/. $mattermostdir

#cleaning
echo Cleaning
rm -rf $downloaddir/mattermost-upgrade/
rm -f $downloaddir/mattermost*.gz

if [ -f /bin/systemctl ];  then
        servicecommand="systemctl start mattermost"
else
        servicecommand="service mattermost start"
fi
echo Starting Mattermost service
$servicecommand
echo Mattermost successfully updated
