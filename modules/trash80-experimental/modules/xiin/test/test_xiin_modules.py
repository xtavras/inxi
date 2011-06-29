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

import subprocess

def test_sequence():
    test_remote_server_util()
    test_local_module_list()
    test_download_util()
    test_module_selector()
    test_xiin_updater()
#    pass
#end

def test_xiin_updater():
    subprocess.call('/home/scott/Applications/inxi/modules/trash80-experimental/modules/xiin/xiinUpdater.py')
#end

def test_module_selector():
    from moduleSelector import xiinModuleSelector

    list = xiinModuleSelector()
    moduleList = list.get_download_list()

    if len(moduleList) < 1:
        print('No files found')
    else:
        print('test_module_selector.Success ModuleList: {0}'.format(moduleList))
#end

def test_remote_server_util():
    from remoteModuleDictionaryUtil import xiinRemoteModuleDictionary

    dict        = xiinRemoteModuleDictionary()
    remoteDict  = dict.get_remote_server_module_dict()

    if len(remoteDict) < 1:
        print('No files found')
    else:
        print('test_remote_server_util.Success RemoteDict: {0}'.format(remoteDict))
#end

def test_local_module_list():
    from localModuleDictionaryUtil import xiinLocalModuleDictionary

    dict        = xiinLocalModuleDictionary()
    localDict   = dict.get_local_module_dict()

    if len(localDict) < 1:
        print('No files found')
    else:
        print('test_local_module_list.Success localDict: {0}'.format(localDict))
#end

def test_download_util():
    from moduleDownloadUtil import xiinDownloadModuleUtil

    downld = xiinDownloadModuleUtil()

    modName = 'inxi'

    source = 'http://inxi.googlecode.com/svn/trunk/' + modName
    destination = '/home/scott/xiinTest/' + modName

    result = downld.download(source, destination)
    if (result):
        print('test_download_util.Success: {0}'.format(result))
        return
    else:
        print('Module test failed: {0}'.format(result))
        exit(1)
#end

if __name__ == '__main__':
    test_sequence()
#end