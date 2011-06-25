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

class XiinUploader(object):
    """
    Uploads a specified file to a specified ftp sight.  \
    [Usage: uploader <source> <target> <uname> <password> ] \
    [Example: uploader /home/myhome/.inxi/some.txt somedomain.com anon anon ]
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
    #end

    def uploadXiinInfo(self, xiinArgDict):
        """
        Uploads debugging information
        """

        destinationServer = os.path.split(xiinArgDict.ftpDestination)[0]
        destinationFolder = os.path.split(xiinArgDict.ftpDestination)[1]

        try:
            ftp = ftplib.FTP(destinationServer)
        except:
            print('ERROR: connection failed')
            exit(3)

        try:
            if xiinArgDict.ftpUname == 'anon':
                ftp.login()
            else:
                ftp.login(xiinArgDict.ftpUname, xiinArgDict.ftpPwd)
        except:
            print('ERROR: login failed')
            exit(4)

        print(ftp.getwelcome())
        if ftp.getwelcome().find('220') >= 0:
            print('Connected...')
        else:
            print('ERROR: connection error')
            exit(3)

        try:
            if destinationFolder is not None:
                ftp.cwd(destinationFolder)
                print('Opening ' + destinationFolder)
        except:
            print('ERROR: destination folder not found')
            exit(5)

        self.upload(ftp, xiinArgDict.ftpSource)

        ftp.quit()
        print('SUCCESS: file uploaded')
        exit(0)
    #end

    def upload(self, ftp, file):
        """
        Does the upload work.
        """

        extension = os.path.splitext(file)[1]
        origDir = os.getcwd()
        workingDir = os.path.split(file)[0]
        workingFile = os.path.split(file)[1]

        savedFileName = self.savedFileName(workingFile, ftp)

        print('file: ' + workingFile)

        if extension in ('.tar.gz'):
            try:
                os.chdir(workingDir)
                print(ftp.pwd())
                ftp.storbinary('STOR ' + savedFileName, open(workingFile))
                os.chdir(origDir)
            except IOError:
                print('ERROR: could not save file')
                exit(2)
        else:
            print('ERROR: Incorrect file')
            exit(1)
    #end

    def savedFileName(self, workingFile, ftp):
        """
        Check the server for a same file name.
        """

        fileList = ftp.nlst()

        for file in fileList:
            if file == workingFile:
                workingFile = self.renameFile(workingFile)

        return workingFile
    #end

    def renameFile(self, file):
        """
        Renames a file so that it no longer conflicts.
        """

        file = file.split('.', 1)
        extension = str(time.time()).split('.', 1)[0]
        newName = file[0] + '-' + extension + '.' + file[1]

        return newName
    #end
#end