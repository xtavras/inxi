#!/usr/bin/env python
__version__     = '2011.06.29-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from moduleSelector import xiinModuleSelector
from moduleDownloadUtil import xiinDownloadModuleUtil

if __name__ == '__main__':
    print('Please wait while xiin checks for updates...')
    print('')

    xiinUpdater     = xiinDownloadModuleUtil()
    xiinSelector    = xiinModuleSelector()
    xiinModList     = xiinSelector.get_download_list()

    source = 'http://inxi.googlecode.com/svn/modules/trash80-experimental/modules/xiin/source/'
    destination = '/home/scott/xiinTest/'

    if len(xiinModList) > 0:
        for xiinMod in xiinModList:
            print('Updating {0}'.format(xiinMod))
            print('')
            xiinUpdater.download(source + xiinMod, destination + xiinMod)
    else:
        print('Nothing to update.')
        print('')

    print('Continuing...')
    print('')
#end
