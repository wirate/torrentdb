
from os.path import isabs

try :
    import bcodeparser.bencode as bencode
except ImportError :
    print "ERROR: Bencode parser not found"


def isTorrentFile(file):
    
    if not file[len(file)-8:len(file)] == '.torrent' :
        return False
        
    return True

# Exceptions:
# IOError
# BTFailure
def bendecode(file) :
    h = open(file, 'r')
    bstr = h.read()
    h.close()
    
    return bencode.bdecode(bstr)
