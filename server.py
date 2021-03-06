#!/usr/bin/env python
# server.py
   
"""A basic FTP server which uses a DummyAuthorizer for managing 'virtual
users', setting a limit for incoming connections.
"""
   
import os
from pyftpdlib import DummyAuthorizer, FTPServer, FTPHandler, __ver__

###############Configuration################################
HOMEDIR = "d:"+os.sep+"ftp"
PORT = 21
HOSTIP = ""
MaxCons = 256
MasConsPerIp = 5
############################################################

if __name__ == "__main__":
    
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()
   
    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('user', '12345', HOMEDIR, perm='elradfmw')
    authorizer.add_user('user1', '12345', HOMEDIR, perm='elradfmw')
    # anonymous only can read
    authorizer.add_anonymous(HOMEDIR)
   
    # Instantiate FTP handler class
    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer
   
    # Define a customized banner (string returned when client connects)
    ftp_handler.banner = "pyftpdlib %s based ftpd ready." %__ver__
   
    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #ftp_handler.masquerade_address = '151.25.42.11'
    #ftp_handler.passive_ports = range(60000, 65535)
   
    # Instantiate FTP server class and listen to 0.0.0.0:21
    address = (HOSTIP, PORT)
    ftpd = FTPServer(address, ftp_handler)
   
    # set a limit for connections
    ftpd.max_cons = MaxCons
    ftpd.max_cons_per_ip = MasConsPerIp
    
    # start ftp server
    ftpd.serve_forever()
    