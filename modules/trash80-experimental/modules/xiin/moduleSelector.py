#!/usr/bin/env python
__version__     = '2011.06.27-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from remoteServerUtil import xiinRemoteServer
from localServerUtil import xiinLocalServer
from moduleUtil import xiinModuleUtil

class xiinModuleSelector(object):

    def __init__(self):
        self = self
        pass
    #end

    def getDownloadList(self):
        remoteModule = xiinRemoteServer()
        localModule = xiinLocalServer()

        localModuleDict = localModule.local_module_dict()
        remoteModuleDict = remoteModule.remote_server_module_dict()
        
        downloadList = self.buildDownloadList(localModuleDict, remoteModuleDict)

        return downloadList
    #end

    def buildDownloadList(self, localModuleDict, remoteModuleDict):
        """

        """
        versionDate = xiinModuleUtil()

        downloadList = []

        # if localModuleDict is empty, then we need all the modules

        for remoteModule in remoteModuleDict:
            if len(localModuleDict) == 0 or remoteModule not in localModuleDict:
                downloadList.append(remoteModule)
            else:
                localVersion = versionDate.convertToDate(localModuleDict[remoteModule])
                remoteVersion = versionDate.convertToDate(remoteModuleDict[remoteModule])

                if localVersion[0] == remoteVersion[0]:
                    if localVersion[1] < remoteVersion[1]:
                        downloadList.append(remoteModule)

                if localVersion[0] < remoteVersion[0]:
                    downloadList.append(remoteModule)

        return downloadList
#end