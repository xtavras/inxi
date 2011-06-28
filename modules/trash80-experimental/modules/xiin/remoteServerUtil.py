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

        cleanVersion = xiinModuleUtil()
        remoteVersion = cleanVersion.clean(version)

        return remoteVersion
    #end
#end
