try :
    if version[:3] == '2.6' :
        import _mysql as MySQLdb
    elif version[:3] == '2.5' :
        import MySQLdb
except ImportError, e :
    print "ERROR: mysql module not installed"
    raise e
