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

def test_sequence():
    test_remote_server_util()
#    test_local_module_list()
#    test_download_util()
    pass
#end

def test_remote_server_util():
    from remoteModuleDictionaryUtil import xiinRemoteModuleDictionary

    dict        = xiinRemoteModuleDictionary()
    remoteDict  = dict.get_remote_server_module_dict()

    if len(remoteDict) < 1:
        print('No files found')
    else:
        print('Success RemoteDict: {0}'.format(remoteDict))

    pass
#end

def test_download_util():
    from downloadUtil import xiinDownloadUtil

    downld = xiinDownloadUtil()

    modName = 'inxi'

    source = 'http://inxi.googlecode.com/svn/trunk/' + modName
    destination = '/home/scott/' + modName

    result = downld.download(source, destination)
    if (result):
        print('Success: {0}'.format(result))
        return
    else:
        print('Module test failed: {0}'.format(result))
        exit(1)
#end

def test_local_module_list():
    from localModuleDictionaryUtil import xiinLocalModuleDictionary

    dict        = xiinLocalModuleDictionary()
    localDict   = dict.get_local_module_dict()

    if len(localDict) < 1:
        print('No files found')
    else:
        print('Success localDict: {0}'.format(localDict))
#end

if __name__ == '__main__':
    test_sequence()
#end