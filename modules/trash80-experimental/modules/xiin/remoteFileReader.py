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

import os
import urllib2
from datetime import date
from HTMLParser import HTMLParser

class xiinRemoteServer(object):

    def __init__(self):
        self = self
        self.urlHome        = 'http://inxi.googlecode.com'
        self.urlDirectory   = '/svn/modules/trash80-experimental/modules/xiin'
        self.remoteFile     = '/reader.py'
        pass
    #end

    def remote_server_file_dict(self):
        """
        
        """
        fileDict = {}
        remoteFileList = self.get_server_file_list()
        for fileName in remoteFileList:
            fileVersion = self.get_server_file_version(fileName)
            fileDict[str(fileName)] = str(fileVersion)

        return fileDict
    #end

    def get_server_file_list(self):
        """

        """
        listUrl     = '{0}{1}'
        parser      = xiinHTMLParser()
        connection  = urllib2.urlopen(listUrl.format(self.urlHome, self.urlDirectory))
        response    = connection.read()

        parser.feed(response)
        parser.close()

        return parser.get_parser_list()
    #end

    def get_server_file_version(self, file):
        """

        """
        # home, directory, file
        urlFull = '{0}{1}/{2}'
        urlFull = urlFull.format(self.urlHome, self.urlDirectory, file)

        connection = urllib2.urlopen(urlFull)
        version = connection.readlines()[1]

        cleanVersion = xiinVersionClean()
        remoteVersion = cleanVersion.clean(version)

        # TODO: convert the version to epoch
        
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

    def local_file_dict(self):
        """

        """
        localFileDict = {}

        localFileList = self.get_local_file_list()

        for localFile in localFileList:
            localFileVersion = self.get_local_file_version(localFile)
            localFileDict[localFile] = localFileVersion

        return localFileDict
    #end

    def get_local_file_list(self):
        """

        """

        localFileList = []

        for root, dirs, files in os.walk(self.xiinDir):
            for remoteFile in files:
                if not '.svn' in remoteFile:
                    splitFileName = remoteFile.split('.')
                    fileNameLength = len(splitFileName)
                    if fileNameLength > 1:
                        ext = splitFileName[fileNameLength - 1]
                        if ext == 'py':
                            localFileList.append(remoteFile)
                            
        return localFileList
    #end

    def get_local_file_version(self, file):
        """

        """
        modFile = '{0}/{1}'.format(self.xiinDir, file)

        cleanVersion = xiinVersionClean()

        try:
            with open(modFile, 'r') as currentModFile:
                localVersion = currentModFile.readlines()[1]
                return cleanVersion.clean(localVersion)
        except:
            pass
    #end
#end

class xiinFileSelector(object):

    def __init__(self):
        self = self
        pass
    #end

    def getDownloadList(self):
        remoteFile = xiinRemoteServer()
        localFile = xiinLocalServer()

        localFileDict = localFile.local_file_dict()
        remoteFileDict = remoteFile.remote_server_file_dict()

        print('localDict: ' + str(localFileDict))
        print('remoteDict: ' + str(remoteFileDict))

        downloadList = self.buildDownloadList(localFileDict, remoteFileDict)

        print('downloadList: ' + str(downloadList))
    #end

    def buildDownloadList(self, localFileDict, remoteFileDict):
        """

        """
        versionDate = xiinVersionClean()

        downloadList = []

        # if localFileDict is empty, then we need all the files

        for remoteFile in remoteFileDict:
            if len(localFileDict) == 0 or remoteFile not in localFileDict:
                downloadList.append(remoteFile)
            else:
                localVersion = versionDate.toDate(localFileDict[remoteFile])
                remoteVersion = versionDate.toDate(remoteFileDict[remoteFile])

                if localVersion[0] == remoteVersion[0]:
                    if localVersion[1] < remoteVersion[1]:
                        downloadList.append(remoteFile)

                if localVersion[0] < remoteVersion[0]:
                    downloadList.append(remoteFile)

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
    downloadListSelector = xiinFileSelector()
    downloadListSelector.getDownloadList()
#end
