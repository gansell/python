# file: ftpclientupload.py

import ftputil

host = ftputil.FTPHost('localhost', 'python',
                       'python')
try:
    host.mkdir('newdir')                            #1
except ftputil.ftp_error.PermanentError:
    print 'Directory already exists.'
    print 'Skipping creation of directory.'
source = host.file('data5.txt', 'r')            #2
target = host.file('newdir/data5.txt', 'w')     #3
host.copyfileobj(source, target)                #4
source.close()
target.close()