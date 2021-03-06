'''

'''
from WMCore.WMStats.DataStructs.DataCache import DataCache
from WMCore.WMStats.CherryPyThreads.CherryPyPeriodicTask import CherryPyPeriodicTask
from WMCore.Services.WMStats.WMStatsReader import WMStatsReader

class DataCacheUpdate(CherryPyPeriodicTask):

    def __init__(self, rest, config):

        CherryPyPeriodicTask.__init__(self, config)

    def setConcurrentTasks(self, config):
        """
        sets the list of functions which
        """
        self.concurrentTasks = [{'func': self.gatherActiveDataStats, 'duration': 300}]

    def gatherActiveDataStats(self, config):
        """
        gather active data statistics
        """
        try:
            if DataCache.islatestJobDataExpired():
                wmstatsDB = WMStatsReader(config.wmstats_url, config.reqmgrdb_url, 
                                          reqdbCouchApp = "ReqMgr")
                jobData = wmstatsDB.getActiveData(jobInfoFlag = True)
                DataCache.setlatestJobData(jobData)
                self.logger.info("DataCache is updated: %s" % len(jobData))
        except Exception as ex:
            self.logger.error(str(ex))
        return