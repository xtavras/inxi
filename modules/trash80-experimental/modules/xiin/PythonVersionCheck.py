#!/usr/bin/env python
__version__     = '2011.06.26-0'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """


import sys

class PythonVersionCheck(object):
    # http://stackoverflow.com/questions/1093322/how-do-i-check-what-version-of-python-is-running-my-script

    def __init__(self, lowestVersion = 0x02060000):        
        self = self
        self.lowestVersion = lowestVersion
    #end

    def check(self):
        """
        Detects Python compatibility.
        """

        pythonVersionText = 'Detecting Python version...[version 2.6+ required]...'
        pythonVersionErrorText = 'ERROR: Incorrect Python version: 2.6+ is required'
        pythonVersionPassText = 'Passed...continuing'

        print('')
        print(pythonVersionText)

        if sys.hexversion < self.lowestVersion:
            print('')
            print(pythonVersionErrorText)
            exit(1)
        else:
            print(pythonVersionPassText)
            print('')
            return
    #end

    def setMinimumVersion(self, lowestVersion):
        """
        lowestVersion:  The minimum python version required. [Default: 2.6 ]
        """

        self.lowestVersion = lowestVersion
    #end
#end

################################################################################
####
####        test method, don't use in code
####
################################################################################

if __name__ == '__main__':
    version = PythonVersionCheck()
    version.check()
#end
