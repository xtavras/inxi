#!/usr/bin/env python
__version__     = '2011.06.27-01'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

import os
import urllib2
from datetime import date
from HTMLParser import HTMLParser

class xiinRemoteServer(object):

    def __init__(self):
        self = self
        self.urlHome        = 'http://inxi.googlecode.com'
        self.urlDirectory   = '/svn/modules/trash80-experimental/modules/xiin'
        self.remoteModule     = '/reader.py'
        pass
    #end

    def remote_server_module_dict(self):
        """
        Creates a dictionary of module(key):version(value) of server side modules
        """
        moduleDict = {}
        remoteModuleList = self.get_server_module_list()
        for moduleName in remoteModuleList:
            moduleVersion = self.get_server_module_version(moduleName)
            moduleDict[str(moduleName)] = str(moduleVersion)

        return moduleDict
    #end

    def get_server_module_list(self):
        """
        Creates a list of server side modules
        """
        listUrl     = '{0}{1}'
        parser      = xiinHTMLParser()
        connection  = urllib2.urlopen(listUrl.format(self.urlHome, self.urlDirectory))
        response    = connection.read()

        parser.feed(response)
        parser.close()

        return parser.get_parser_list()
    #end

    def get_server_module_version(self, module):
        """
        Returns the version of a module
        """
        # home, directory, module
        urlFull = '{0}{1}/{2}'
        urlFull = urlFull.format(self.urlHome, self.urlDirectory, module)

        connection = urllib2.urlopen(urlFull)
        version = connection.readlines()[1]

        cleanVersion = xiinVersionClean()
        remoteVersion = cleanVersion.clean(version)
        
        return remoteVersion
    #end
#end

class xiinHTMLParser(HTMLParser):
# http://stackoverflow.com/questions/1699634/how-to-retrieve-a-directory-of-files-from-a-remote-server
    remoteList = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    ext = value.split('.')[1]
                    if ext == 'py':
                        self.remoteList.append(value)
    #end

    def get_parser_list(self):
        return self.remoteList

#end

class xiinLocalServer(object):

    def __init__(self):
        self = self
        self.xiinDir = os.getcwd()
    #end

    def local_module_dict(self):
        """

        """
        localmoduleDict = {}

        localmoduleList = self.get_local_module_list()

        for localmodule in localmoduleList:
            localmoduleVersion = self.get_local_module_version(localmodule)
            localmoduleDict[localmodule] = localmoduleVersion

        return localmoduleDict
    #end

    def get_local_module_list(self):
        """

        """

        localmoduleList = []

        for root, dirs, modules in os.walk(self.xiinDir):
            for remotemodule in modules:
                if not '.svn' in remotemodule:
                    splitmoduleName = remotemodule.split('.')
                    moduleNameLength = len(splitmoduleName)
                    if moduleNameLength > 1:
                        ext = splitmoduleName[moduleNameLength - 1]
                        if ext == 'py':
                            localmoduleList.append(remotemodule)
                            
        return localmoduleList
    #end

    def get_local_module_version(self, module):
        """

        """
        module = '{0}/{1}'.format(self.xiinDir, module)

        cleanVersion = xiinVersionClean()

        try:
            with open(module, 'r') as currentModule:
                localVersion = currentModule.readlines()[1]
                return cleanVersion.clean(localVersion)
        except:
            pass
    #end
#end

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

        print('localDict: ' + str(localModuleDict))
        print('remoteDict: ' + str(remoteModuleDict))

        downloadList = self.buildDownloadList(localModuleDict, remoteModuleDict)

        print('downloadList: ' + str(downloadList))
    #end

    def buildDownloadList(self, localModuleDict, remoteModuleDict):
        """

        """
        versionDate = xiinVersionClean()

        downloadList = []

        # if localModuleDict is empty, then we need all the modules

        for remoteModule in remoteModuleDict:
            if len(localModuleDict) == 0 or remoteModule not in localModuleDict:
                downloadList.append(remoteModule)
            else:
                localVersion = versionDate.toDate(localModuleDict[remoteModule])
                remoteVersion = versionDate.toDate(remoteModuleDict[remoteModule])

                if localVersion[0] == remoteVersion[0]:
                    if localVersion[1] < remoteVersion[1]:
                        downloadList.append(remoteModule)

                if localVersion[0] < remoteVersion[0]:
                    downloadList.append(remoteModule)

        return downloadList
#end

class xiinVersionClean(object):

    def clean(self, version):
        version = version.replace('\\n','')
        version = version.replace('=',':')
        version = version.replace('\'','')
        version = version.split(':', 1)[1]
        return version.strip()
    #end

    def toDate(self, version):
        """

        """
        versionYYMMDD = version.split('.')
        versionYear = int(versionYYMMDD[0])
        versionMonth = int(versionYYMMDD[1])
        versionDay = int(versionYYMMDD[2].split('-')[0])
        versionPatch = int(versionYYMMDD[2].split('-')[1])

        versionDate = date(versionYear,versionMonth,versionDay)

        return versionDate, versionPatch
    #end
#end

if __name__ == '__main__':
    downloadListSelector = xiinModuleSelector()
    downloadListSelector.getDownloadList()
#end
