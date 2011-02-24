#!/bin/bash

path=$@

/bin/echo "(DATABASE) adding torrentfile: $@"
/mnt/bin/dbtorrent/dbtorrent.py add "$@"
