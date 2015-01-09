#coding:utf-8
import ftplib

#Public define
FILE_NAME = "README"
FTP_SERVER = '127.0.0.1'
PORT = 21

USER = "mjh"
PASSWORD = "mjh"


def download(file_name=FILE_NAME, user="", passwd=""):
    print "Download %s start ..." % file_name
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_SERVER, PORT)
        ftp.login(user, passwd)
        ftp.retrbinary('RETR '+file_name, open(file_name,'wb').write)
        ftp.quit()
        print "Download %s successfully." % file_name
    except Exception, e:
        print "Download %s failed(reseaon:%s)" % (file_name, e)
    

def upload(file_name=FILE_NAME, user="", passwd=""):
    print "Upload %s start ..." % file_name
    try:
        ftp = ftplib.FTP()
        ftp.connect(FTP_SERVER, PORT)
        ftp.login(user, passwd)
        ftp.storbinary("STOR "+file_name, open(file_name, 'rb'))
        ftp.quit()
        print "Upload %s successfully." % file_name
    except Exception, e:
        print "Upload %s failed(reseaon:%s)." % (file_name, e)
    
#download("360safe.zip", USER, PASSWORD)
upload("README", USER, PASSWORD)

