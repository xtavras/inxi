#!/usr/bin/env python
__version__     = '2011.06.28-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from remoteModuleDictionaryUtil import xiinRemoteModuleDictionary
from localModuleDictionaryUtil import xiinLocalModuleDictionary
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

    def build_download_list(self, localModuleDict, remoteModuleDict):
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

    def get_download_list(self):
        """
        Returns a list of modules requiring updates.
        """
        remoteModule = xiinRemoteModuleDictionary()
        localModule = xiinLocalModuleDictionary()


        print(self.xiinLocalStatus)
        print('')
        localModuleDict = localModule.get_local_module_dict()

        print(self.xiinRemoteStatus)
        print('')
        remoteModuleDict = remoteModule.get_remote_server_module_dict()
        
        downloadList = self.build_download_list(localModuleDict, remoteModuleDict)

        return downloadList
    #end
#end