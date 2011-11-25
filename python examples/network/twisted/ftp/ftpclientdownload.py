# file: ftpclientdownload.py

import ftputil                                      #1

host = ftputil.FTPHost('localhost',                 #2
                       'anonymous', '')
names = host.listdir(host.curdir)                   #3
for name in names:                                  #4
    if host.path.isfile(name):                      #5
        host.download(name, name, 'b')              #6
