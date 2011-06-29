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
                    
import os
from moduleUtil import xiinModuleUtil

class xiinLocalModuleDictionary(object):

    def __init__(self, xiinDir = os.getcwd()):
        self = self
        self.xiinDir = xiinDir
    #end

    def get_local_module_dict(self):
        """
        Returns a dictionary of local modules with versions.
        """
        
        localmoduleDict = {}
        localmoduleList = self.get_local_module_list(self.xiinDir)

        for localmodule in localmoduleList:
            localmoduleVersion = self.get_local_module_version(localmodule)
            localmoduleDict[localmodule] = localmoduleVersion

        return localmoduleDict
    #end

    def get_local_module_list(self, dir):
        """
        Returns a list of local modules.
        """

        localmoduleList = []

        for module in os.listdir(dir):
            if not '.svn' in module:
                splitmoduleName = module.split('.')
                moduleNameLength = len(splitmoduleName)
                if moduleNameLength > 1:
                    ext = splitmoduleName[moduleNameLength - 1]
                    if ext == 'py' or ext == 'yml':
                        localmoduleList.append(module)

        return localmoduleList
    #end

    def get_local_module_version(self, module):
        """
        Get the version for each local module.
        """
        module = '{0}/{1}'.format(self.xiinDir, module)

        cleanVersion = xiinModuleUtil()

        try:
            with open(module, 'r') as currentModule:
                localVersion = currentModule.readlines()[1]
                return cleanVersion.clean(localVersion)
        except:
            pass
    #end

    def set_local_dir(self, dir):
        self.xiinDir = dir
    #end

    def get_local_dir(self):
        return self.xiinDir
    #end
#end