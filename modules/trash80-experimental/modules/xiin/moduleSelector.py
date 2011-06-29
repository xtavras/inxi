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
    """
    Compare the list of server module versions with local module version. Return
    a list of out of date modules.
    """

    def __init__(self):
        self = self
        self.xiinRemoteStatus   = 'Checking latest versions of xiin modules...'
        self.xiinLocalStatus    = 'Checking local xiin module version...'
    #end

    def getDownloadList(self):
        """
        Returns a list of modules requiring updates.
        """
        remoteModule = xiinRemoteServer()
        localModule = xiinLocalServer()


        print(self.xiinLocalStatus)
        print('')
        localModuleDict = localModule.local_module_dict()

        print(self.xiinRemoteStatus)
        print('')
        remoteModuleDict = remoteModule.remote_server_module_dict()
        
        downloadList = self.buildDownloadList(localModuleDict, remoteModuleDict)

        return downloadList
    #end

    def buildDownloadList(self, localModuleDict, remoteModuleDict):
        """
        Compare the versions of local and server modules to create a list of
        outdated modules.
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
#end