#!/usr/bin/python3
#Autor: Miguel Alejandro Juarez Gonzalez
#script para hacer una peticion a un servidor ftp y descarga el archivo .msg
RUTA_SERVIDOR_FTP = 'ftp.us.debian.org'
import ftplib
def conexion(serv, nom_usu, correo):
    ftp = ftplib.FTP(serv, nom_usu, correo)
    print ("Archivos disponibles en %s:" %serv)
    archivos = ftp.dir()
    print (archivos)
    ftp.retrbinary('RETR welcome.msg', open ('welcome.msg', 'wb').write)
    ftp.quit()

if __name__ == '__main__':
    conexion(serv=RUTA_SERVIDOR_FTP, nom_usu='anonymous',correo='nobody@nourl.com', )