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

import urllib2
from htmlParser import xiinHTMLParser
from moduleUtil import xiinModuleUtil

class xiinRemoteModuleDictionary(object):

    def __init__(self):
        self = self
        self.urlHome        = 'http://inxi.googlecode.com'
        self.urlDirectory   = '/svn/modules/trash80-experimental/modules/xiin'

    #end

    def get_remote_server_module_dict(self):
        """
        Creates a dictionary of module(key):version(value) of server side modules.
        """
        moduleDict       = {}
        listUrl          = '{0}{1}'.format(self.urlHome, self.urlDirectory)
        remoteModuleList = self.get_server_module_list(listUrl)

        for moduleName in remoteModuleList:
            urlFull = '{0}{1}/{2}'.format(self.urlHome, self.urlDirectory, moduleName)
            moduleVersion = self.get_server_module_version(urlFull)
            moduleDict[str(moduleName)] = str(moduleVersion)

        return moduleDict
    #end

    def get_server_module_list(self, xiinUrlDir):
        """
        Creates a list of server side modules.
        """
        parser      = xiinHTMLParser()
        connection  = urllib2.urlopen(xiinUrlDir)
        response    = connection.read()

        parser.feed(response)
        parser.close()

        return parser.get_parser_list()
    #end

    def get_server_module_version(self, xiinUrlMod):
        """
        Returns the version of a module.
        """
        cleaner         = xiinModuleUtil()
        connection      = urllib2.urlopen(xiinUrlMod)
        dirtyVersion    = connection.readlines()[1]
        version         = cleaner.clean(dirtyVersion)

        return version
    #end

    def set_url_home(self, xiinUrl):
        self.urlHome = xiinUrl
    #end

    def get_url_home(self):
        return self.urlHome
    #end

    def set_url_directory(self, xiinDir):
        self.urlDirectory = xiinDir
    #end

    def get_url_directroy(self):
        return self.urlDirectory
    #end
#end
