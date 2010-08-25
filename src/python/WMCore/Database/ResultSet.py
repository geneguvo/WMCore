"""
_ResultSet_

A class to read in a SQLAlchemy result proxy and hold the data, such that the 
SQLAlchemy result sets (aka cursors) can be closed. Make this class look as much
like the SQLAlchemy class to minimise the impact of adding this class.
"""

__revision__ = "$Id: ResultSet.py,v 1.6 2009/05/14 14:51:27 mnorman Exp $"
__version__ = "$Revision: 1.6 $"

class ResultSet:
    def __init__(self):
        self.data = []
        self.keys = []
        self.rowcount = 0
        #Oracle has no lastrowid, so this is only set if it exists.  See add()
        self.lastrowid = None

    def close(self):
        return
    
    def fetchone(self):
        return self.data[0]
    
    def fetchall(self):
        return self.data
    
    def add(self, resultproxy):
        if resultproxy.closed:
            return
        
        for r in resultproxy:
            if len(self.keys) == 0:
                self.keys.extend(r.keys())
            self.data.append(r)

        #Has to be there to provide some Oracle functionality
        #Oracle resultproxy doesn't have lastrowid
        if hasattr(resultproxy, 'lastrowid'):
            self.lastrowid = resultproxy.lastrowid
        self.rowcount = len(self.data)
        
        return
