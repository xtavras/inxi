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

class xiinDownloadModuleUtil(object):

    def __init__(self, blocksize = 8192):
        self = self
        self.blockSize = blocksize
    #end

    def download(self, source, destination): #moduleURIName):
        """
        Download a new version of a module
        """
        connection  = urllib2.urlopen(source)

        try:
            with open(destination, 'w') as localFile:
                while True:
                    modLine = connection.read(self.blockSize)
                    if not modLine:
                        break
                    localFile.write(modLine)
            return True
        except:
            return False
    #end

    def setBlockSize(self, blocksize):
        self.blockSize = blocksize
    #end

    def getBlockSize(self):
        return self.blockSize
    #end
#end