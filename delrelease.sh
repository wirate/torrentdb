#!/bin/bash

#path=$@
#path=`/bin/echo $path | /usr/bin/replace "(" "\("`
#path=`/bin/echo $path | /usr/bin/replace ")" "\)"`
#path=`/bin/echo $path | /usr/bin/replace "]" "\]"`
#path=`/bin/echo $path | /usr/bin/replace "[" "\["`

echo "deleting torrentfile (from db): $@"
/mnt/bin/dbtorrent/dbtorrent.py del "$@"
