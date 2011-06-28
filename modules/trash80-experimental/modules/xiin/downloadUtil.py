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

class xiinDownloadModule(object):

    def __init__(self):
        self = self
        self.urlHome        = 'http://inxi.googlecode.com'
        self.urlDirectory   = '/svn/modules/trash80-experimental/modules/xiin'
    #end

    def downloadModule(self, module):
        """
        Download a new version of a module
        """

        urlFull = '{0}{1}/{2}'
        urlFull = urlFull.format(self.urlHome, self.urlDirectory, module)

        connection  = urllib2.urlopen(urlFull)
        with open(module, 'w') as localFile:
            localFile.write(connection.read())
    #end

    def testSuccessfulDownload(self, module):
        pass
    #end
#end
