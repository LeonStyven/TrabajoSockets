# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

@author: 000420606, 000416688, 000437946
"""
import socket



#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



#get local machine name
host = socket.gethostname()
port = 9999



#connection to hostname on the port
s.connect((host, port))



#receive no more than 1024 bytes
tm = s.recv(1024)



s.close()



print('\b El tiempo recibido desde el servidor es %s' % tm.decode('ascii'))