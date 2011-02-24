#!/usr/bin/python2.5

import sys
import torrent

if torrent.isTorrentFile(sys.argv[1]) :
     print torrent.getBasepath(sys.argv[1])
