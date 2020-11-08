#!/usr/bin/env python3
#Autor: Miguel Alejandro Juarez Gonzalez

from ftplib import FTP, FTP_PORT
import os
ftp = FTP('ftp.us.debian.org')
ftp.login()
os.system("mkdir carpeta_TXT")

for line in ftp.retrlines('LIST'):
    
    if line.startswith('dr') == 1:
        os.system(line+" cv carpeta_TXT")

ftp.close()