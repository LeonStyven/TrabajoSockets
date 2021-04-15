# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

@author: user
"""

import socket

#create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()
port = 9999

#bind to the port
serversocket.bind((host, port))

#queue up to 5 requests
serversocket.listen(5)

print('--DESCONECTADO--')