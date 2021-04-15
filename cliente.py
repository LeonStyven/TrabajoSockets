# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

@author: 000420606, 000416688, 000437946
"""
import socket
import random as rd
import time 
import numpy as np 
import matplot.pyplot as plt


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

promedio = 8.0

N = 1000

solicitud = [0]

for k in range(N):
	valor = rd.expovariate(1.0/promedio)
	solicitud.append(valor)

plt.hist(solicitud)
np.mean(solicitud)

solicitud[-1]