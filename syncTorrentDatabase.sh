#!/bin/bash

find /mnt/torrents | grep -e torrent$ | xargs -i -0 -d '\n' /mnt/bin/dbtorrent/addrelease.sh '{}'
