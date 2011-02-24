#!/bin/bash

/mnt/bin/dbtorrent/dbtorrent.py check "$@"

if [ $? -eq 0 ]; then
	echo "> DELETE: $@"

	#path=$@
	#path=`/bin/echo $path | /usr/bin/replace "(" "\("`
	#path=`/bin/echo $path | /usr/bin/replace ")" "\)"`
	#path=`/bin/echo $path | /usr/bin/replace "]" "\]"`
	#path=`/bin/echo $path | /usr/bin/replace "[" "\["`
	#path=`/bin/echo $path | /usr/bin/replace "{" "\{"`
	#path=`/bin/echo $path | /usr/bin/replace "}" "\}"`
	#path=`/bin/echo $path | /usr/bin/replace "'" "\'"`
	#path=`/bin/echo $path | /usr/bin/replace " " "\ "`

	/bin/rm -fr /mnt/downloads/"$@"

	if [ $? -eq 1 ]; then
		echo "CAN'T REMOVE: $@"
	fi
else
	echo ">>> SKIPPING: $@"
fi

