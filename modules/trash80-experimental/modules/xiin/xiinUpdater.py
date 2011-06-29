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

from moduleSelector import xiinModuleSelector
from downloadUtil import xiinDownloadModule

if __name__ == '__main__':
    print('Please wait while xiin checks for updates...')
    print('')
    
    downloadList = xiinModuleSelector()
    xiinModList = downloadList.getDownloadList()
    updateFile = xiinDownloadModule()

    if len(xiinModList) > 0:
        for xiinMod in xiinModList:
            print('Updating {0}'.format(xiinMod))
            print('')
            updateFile.downloadModule(xiinMod)
            # TODO: add module to install new modules
    else:
        print('Nothing to update.')
        print('')

    print('Continuing...')
    print('')
#end
