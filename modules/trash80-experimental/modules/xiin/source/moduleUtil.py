#!/usr/bin/env python
__version__     = '2011.06.27-00'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers 
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """

from datetime import date

class xiinModuleUtil(object):
    """
    A Utility for functions that don't belong in other modules.
    """

    def clean(self, version):
        """
        Remove unneeded characters.
        """
        version = version.replace('\\n','')
        version = version.replace('=',':')
        version = version.replace('\'','')
        version = version.split(':', 1)[1]

        return version.strip()
    #end

    def convertToDate(self, version):
        """
        Convert the version to a date and patch number.
        """
        versionYYMMDD   = version.split('.')
        versionYear     = int(versionYYMMDD[0])
        versionMonth    = int(versionYYMMDD[1])
        versionDay      = int(versionYYMMDD[2].split('-')[0])
        versionPatch    = int(versionYYMMDD[2].split('-')[1])
        versionDate     = date(versionYear,versionMonth,versionDay)

        return versionDate, versionPatch
    #end
#end