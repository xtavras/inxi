#!/usr/bin/env python

#    author: Scott Rogers
#    stability: alpha
#    copying: 'Copyright (C) 2011 W. Scott Rogers
#              This program is free software.
#              You can redistribute it and/or modify it under the terms of the
#              GNU General Public License as published by the Free Software Foundation;
#              version 2 of the License.
#
#   Special thanks: h2, aka Harald Hope

import os
import sys
import optparse

################################################################################
####
####        Main xiin class
####
################################################################################

class XIIN(object):

    def __init__(self):
        self = self
    #end

    def read(self, xiinArg):
        """
        Starts the read capabilities
        """
        # http://docs.python.org/library/optparse.html

        check = PythonVersionCheck()
        check.check()

        xiinDesc = """ xiin is a directory parser meant to help debug inxi(www.inxi.org) bugs.
            xiin will take a given directory, usually /sys or /proc and write the contents
            to a specified file in key:value format where key is the directory/filename
            and value is the contents of key."""

        xiinUsage   = "%prog [-d] <directory to read> [-f] <file to write>"

        xiinVersion = "%prog 2011.06.24-4-alpha"

    #    defaultFile = os.environ['HOME'] + '/xiin.txt'
    #    defaultDir = '/sys'
    #    defaultDisplay = False

        dirHelp     = 'Directory containing files. \
                        [Usage:  ] \
                        [Example:  ]'
        fileHelp    = 'If used write report to file, otherwise write output to the screen. \
                        [Usage:  ] \
                        [Example:  ]'
        displayHelp = 'Prints to terminal not to a file.  Cannot use with -f option. \
                        [Usage:  ] \
                        [Example:  ]'
        grepHelp    = 'Grep-like function. Can be sent to display(default) or file. \
                        [Usage: unused at this time] \
                        [Example: ]'
        uploadHelp  = 'Uploads a specified file to a specified ftp sight.  \
                        [Usage: xiin -u <source> <target> <uname> <password> ] \
                        [Example: xiin -u /home/myhome/.inxi/some.txt somedomain.com anon anon ]'

        parser = optparse.OptionParser(description = xiinDesc, usage = xiinUsage, version = xiinVersion)

        parser.add_option('-d', '--directory', dest = 'directory', help = dirHelp)
        parser.add_option('-f', '--file', dest = 'filename', help = fileHelp)
        parser.add_option('-o', '--out', action = 'store_true', dest = 'display', help = displayHelp)
        parser.add_option('-g', '--grep', dest = 'grep', help = grepHelp)
        parser.add_option('-u', '--upload', nargs=4, dest = 'upload', help = uploadHelp)

        (options, args) = parser.parse_args()

        options.args = xiinArg

        xiinUseChecker(options)
        xiinSwitch(options)

        exit(0)
    #end

    def xiinUseChecker(self, xiinArgDict):
        """
        Checks for use errors.
        """

        if xiinArgDict.upload is None:
        # no arguements specified, so display helpful error
            if len(xiinArgDict.args) < 2:
                parser.error('Nothing to do. Try option -h or --help.')
                exit(2)

        # no output specified
            elif xiinArgDict.filename is None and xiinArgDict.display is None and xiinArgDict.grep is None:
                parser.error('specify to display output or send to a file')
                exit(3)

        # reading /proc will hang system for a while, it's a big deep virtual-directory
            elif xiinArgDict.directory == '/proc':
                parser.error('xiin can not walk /proc')
                exit(4)

        # the directory needed when option used
            elif xiinArgDict.directory is None:
                parser.error('xiin needs a directory')
                exit(5)
        else:
            print('Using xiin upload feature')
    #        xiin.ftp = {'source': '', 'destination': '', 'uname': '', 'password': ''}
            xiinArgDict.ftpSource      = xiinArgDict.upload[0]
            xiinArgDict.ftpDestination = xiinArgDict.upload[1]
            xiinArgDict.ftpUname       = xiinArgDict.upload[2]
            xiinArgDict.ftpPwd         = xiinArgDict.upload[3]
    #end

    def xiinSwitch(self, xiinArgDict):
        """
        Traffic director.
        """

    # only display output
        if xiinArgDict.display is True and xiinArgDict.filename is None:
            print('Starting xiin...')
            print('')
            displayXiinInfo(xiinArgDict)

    # only write output
        elif xiinArgDict.display is None and xiinArgDict.filename is not None:
            print('Starting xiin...')
            print('')
            print('Using options: ' + str(xiinArgDict))
            print('')
            writeXiinInfo(xiinArgDict)

        elif xiinArgDict.grep is not None:
            print('Starting xiin...')
            print('')
            print('Searching files...')
            print('')
            grepXiinInfo(xiinArgDict.grep)

        elif xiinArgDict.upload is not None:
            uploader = XiinUploader()
            print('Starting xiin...')
            print('')
            print('Uploading debugging information...')
            print('')
            uploader.uploadXiinInfo(xiinArgDict)

    #end

    def displayXiinInfo(xiinArgDict):
        """
        Opens the write file and directs the walker, also displays output.
        """

        print("Getting info")
        print('')

        for root, dirs, files in os.walk(xiinArgDict.directory):
            for file in files:
                xiinArgDict.fullPathFile = os.path.join(root, file)
                xiinOpenFile(xiinArgDict)
    #end

    def writeXiinInfo(xiinArgDict):
        """
        Opens the write file and directs the walker, also displays output.
        """

        print("Getting info")
        print('')

        with open(xiinArgDict.filename, 'w') as xiinArgDict.outputFile:
            xiinDirectoryWalker(xiinArgDict)
    #end

    def xiinDirectoryWalker(xiinArgDict):
        """
        Walks the directory.
        """

        spinner = Spinner()

        count = 1

        for root, dirs, files in os.walk(xiinArgDict.directory):
            for file in files:
                spinner.render(count)
                count = count + 1
                xiinArgDict.fullPathFile = os.path.join(root, file)
                xiinOpenFile(xiinArgDict)
    #end

    def xiinOpenFile(xiinArgDict):
        """
        Opens a file and prep to read.
        """

        #  reading some file in /sys will turn off some monitors, so we do this:
        if xiinArgDict.directory == '/sys':
            try:
                if os.stat(xiinArgDict.fullPathFile).st_size:
                    with open(xiinArgDict.fullPathFile, 'r') as xiinArgDict.someFile:
                        xiinReadFileContents(xiinArgDict)
            except:
                pass
        else:
            # other files seem alright
            try:
                with open(xiinArgDict.fullPathFile, 'r') as xiinArgDict.someFile:
                    xiinReadFileContents(xiinArgDict)
            except IOError:
                pass
    #end

    def xiinReadFileContents(xiinArgDict):
        """
        Read file contents and either display them or write them to a file.
        """

        contents = []
        try:
            contents = xiinArgDict.someFile.readlines()
        except:
            pass

        if contents:
            key = str(xiinArgDict.fullPathFile)#.replace('/', '.').replace('.', '', 1)

            value = str(contents).replace('\\n','')

            if value != '[\'\']':
                if xiinArgDict.display:
                    print(key + ':' + value)
                else:
                    xiinArgDict.outputFile.writelines(key + ':' + value + ':' + '\n')
    #end
#end

if __name__ == '__main__':
    xiin = XIIN()
    xiin.read(sys.argv)
#end