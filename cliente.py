# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

@author: 000420606, 000416688, 000437946
"""
import socket
import random as rd
import time 
import numpy as np 
import matplotlib.pyplot as plt


idCliete = 0
promedio = 1
N = 1000
solicitud = [0]
repeticiones = 50

#Obtener el tiempo entre cada evento
for k in range(N):
	tiempoEspera = rd.expovariate(1.0/promedio)
	solicitud.append(tiempoEspera)

plt.hist(solicitud, 100)
np.mean(solicitud)


#El servidor espera el tiempo que le indique la variable tiempoEspera

while(N >= repeticiones and repeticiones>0):
    idCliente = rd.randint(0, 119)
    tiempoEspera = rd.expovariate(1.0/promedio)
    solicitud.append(tiempoEspera)
    repeticiones -= 1
    time.sleep(tiempoEspera)


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
#Obtener un ID para enviar a verificacion






