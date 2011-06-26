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


import os
import sys
import ftplib

class XiinUploader(object):
    """
    Uploads a specified file to a specified ftp sight.  \
    [Usage: uploader <source> <target> <uname> <password> ] \
    [Example: uploader /home/myhome/.inxi/some.txt somedomain.com/directory anon anon ]
    """

    # exit(0): success
    # exit(1): incorrect file
    # exit(2): saving file error
    # exit(3): connection error
    # exit(4): login error
    # exit(5): error finding directory

    # http://effbot.org/librarybook/ftplib.htm
    # http://postneo.com/stories/2003/01/01/beyondTheBasicPythonFtplibExample.html
    # http://docs.python.org/library/ftplib.html

    def __init__(self):
        self = self

        # Success
        self.successFileUploaded        = 'SUCCESS: file uploaded'

        # Error
        self.errorConnectionFail        = 'ERROR: connection failed'
        self.errorPasswordMissing       = 'ERROR: password missing'
        self.errorLoginFail             = 'ERROR: login failed'
        self.errorConnectionError       = 'ERROR: connection error'
        self.errorDestinationNotFound   = 'ERROR: destination folder not found'
        self.errorFileNotSaved          = 'ERROR: file not saved'
        self.errorIncorrectFileType     = 'ERROR: Incorrect file type'
    #end

    def upload(self, source, target, uname = None, password = None):
        """
        Uploads debugging information
        """

        destination = os.path.split(target)

        destinationServer = destination[0]
        if len(destination) > 1:
            destinationFolder = destination[1]

        try:
            ftp = ftplib.FTP(destinationServer)
        except:
            print(self.errorConnectionFail)
            exit(3)

        try:
            if uname is None:
                ftp.login()
            else:
                if password is not None:
                    ftp.login(uname, password)
                else:
                    print(self.errorPasswordMissing)
        except:
            print(self.errorLoginFail)
            exit(4)

        print(ftp.getwelcome())

        if ftp.getwelcome().find('220') >= 0:
            print('Connected...')
        else:
            print(self.errorConnectionError)
            exit(3)


        if destinationFolder is not None:
            try:
                ftp.cwd(destinationFolder)
                print('Opening ' + destinationFolder)
            except:
                print(self.errorDestinationNotFound)
                exit(5)

        self.do_upload(ftp, source)

        ftp.quit()
        print(self.successFileUploaded)
        exit(0)
    #end

    def do_upload(self, ftp, file):
        """
        Upload the file.
        """

        extension       = os.path.splitext(file)[1]
        origDir         = os.getcwd()
        workingDir      = os.path.split(file)[0]
        workingFile     = os.path.split(file)[1]
        savedFileName   = self.check_file_name(workingFile, ftp)

        print('file: ' + workingFile)

        if extension in ('.tar.gz'):
            try:
                os.chdir(workingDir)
                print(ftp.pwd())
#                ftp.storbinary('STOR ' + savedFileName, open(workingFile))
                os.chdir(origDir)
            except IOError:
                print(self.errorFileNotSaved)
                exit(2)
        else:
            print(self.errorIncorrectFileType)
            exit(1)
    #end

    def check_file_name(self, workingFile, ftp):
        """
        Check the server for a same file name.
        """

        fileList = ftp.nlst()

        for file in fileList:
            if file == workingFile:
                workingFile = self.rename_file(workingFile)

        return workingFile
    #end

    def rename_file(self, file):
        """
        Renames a file so that it no longer conflicts.
        """

        file = file.split('.', 1)
        extension = str(time.time()).split('.', 1)[0]
        newName = file[0] + '-' + extension + '.' + file[1]

        return newName
    #end
#end

################################################################################
####
####        test method, don't use in code
####
################################################################################

if __name__ == '__main__':
    source      = None
    target      = None
    uname       = None
    password    = None
    if len(sys.argv) > 2:
        source      = sys.argv[1]
        target      = sys.argv[2]
    else:
        print('')
        print('No options given')
        print('[Usage: uploader <source> <target> <uname> <password> ]')
        print('')
        exit(0)
    if len(sys.argv) > 3:
        uname       = sys.argv[3]
        password    = sys.argv[4]

    uploader    = XiinUploader()
    uploader.upload(source, target, uname, password)
#end