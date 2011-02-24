#
# Database wrapper

from sys import version
from os.path import realpath
from torrent import isTorrentFile, bendecode

try :
    if version[:3] == '2.6' :
        import _mysql as MySQLdb
    elif version[:3] == '2.5' :
        import MySQLdb
except ImportError, e :
    print "ERROR: mysql module not installed"
    raise e
 

class wrapper :

    def __init__(self, host, user, passwd, db) :
        self.dbh = MySQLdb.connection(host, user, passwd, db)
        
    #
    def addrelease(self, torrent) :
           
        if not isTorrentFile(torrent) :
            print "Error: %s is not a torrentfile" %(torrent)
            return
        
        try :
            base = bendecode(torrent)
            base = base['info']['name']
        except (IOError, BTFailure, KeyError), e:
            print "Error: " + e
            return
        
        if self.execute("SELECT `id` FROM `torrent` WHERE `file` = '%s' LIMIT 1" 
                        %(self.dbescape(torrent))).num_rows() :
            print "INFO: Torrentfile exist, bailing out"
            return

        # look for basepath
        res = self.execute("SELECT `id` FROM `basepath` WHERE `path` = '"+self.dbescape(base)+"' LIMIT 1")
        
        if res.num_rows() == 0 :
	        # insert basepath
            self.execute("INSERT INTO `basepath` ("
                  "`id`,"  
                  "`path`,"   
                  "`complete`"
               ") VALUES ("
                  "null,"
                  "'%s',"  
                  "default"   
            ")" %(self.dbescape(base)))

            pid = self.dbh.insert_id()
        else :
	        # fetch pid from query.
            pid = int(res.fetch_row()[0][0])
            

        # insert torrentfile
        self.dbh.query("INSERT INTO `torrent` ("
                "`id`,"
                "`file`,"
                "`basepath`"
            ") VALUES ("
                "null,"
                "'%s',"
                "'%d'"
        ")" %(self.dbescape(torrent), pid))
            
    #
    def delrelease(self, torrent) :
        
        if not isTorrentFile(torrent) :
            return
        
        # search for basepath
        res = self.execute("SELECT `basepath` FROM `torrent` WHERE file = '%s' LIMIT 1" %(self.dbescape(torrent)))
        
        if res.num_rows() == 0 :
            # no torrent with that name exists, return.
            return 
        
        bp = int(res.fetch_row()[0][0])
        
        # delete the torrentfile
        self.dbh.query("DELETE FROM `torrent` WHERE file = '%s' LIMIT 1" %(self.dbescape(torrent)))
        
        # find torrents that is connected to the same basepath.
        res = self.execute("SELECT id FROM `torrent` WHERE basepath = %d LIMIT 1" %(bp))
        
        if res.num_rows() == 0 :
            # no torrents are connected to the basepath. delete it.
            self.dbh.query("DELETE FROM `basepath` WHERE id = %d LIMIT 1" %(bp))
            
        return 1
    
    # Check to see if a basepath exists or not
    def checkbase(self, basepath):
        q = self.execute("SELECT id FROM `basepath` WHERE `path` = '%s' LIMIT 1" %(self.dbescape(basepath)))
        return int(q.num_rows())

    # reset the database, WARNING: will remove all the data.
    def truncate(self) :
	self.execute("TRUNCATE TABLE `torrent`");
        self.execute("ALTER TABLE `torrent` AUTO_INCREMENT = 0");

	self.execute("TRUNCATE TABLE `basepath`");
        self.execute("ALTER TABLE `basepath` AUTO_INCREMENT = 0");
    
    #
    def execute(self, q) :
        self.dbh.query(q)
        return self.dbh.store_result()
    
    def dbescape(self, str) :
	    return self.dbh.escape_string(str)
    
    def close(self) :
        self.dbh.close()
        
    def __del__(self) :
        self.close()



        
