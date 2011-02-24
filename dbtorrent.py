#!/usr/bin/python
# coding: UTF-8

import sys
import db

dbo = db.wrapper('localhost', 'torrentuser', 'xc3sdo2i16s', 'torrents')

if   sys.argv[1] == 'add' :
    sys.exit( dbo.addrelease(sys.argv[2]) )
elif sys.argv[1] == 'del' :
    sys.exit( dbo.delrelease(sys.argv[2]) )
elif sys.argv[1] == 'check' :
    sys.exit( dbo.checkbase(sys.argv[2]) )
elif sys.argv[1] == 'init' :

    for line in sys.stdin.readlines() :
        dbo.addrelease(line.strip())

else :
    print "Invalid argument"
    sys.exit(-1)
