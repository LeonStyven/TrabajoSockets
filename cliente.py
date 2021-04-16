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


idCliente = 0
promedio = 1
solicitud = [0]
repeticiones = 120





#get local machine name
host = socket.gethostname()
port = 9999



#Obtener el tiempo entre cada evento
'''for k in range(N):
	tiempoEspera = rd.expovariate(1.0/promedio)
	solicitud.append(tiempoEspera)

plt.hist(solicitud, 100)
np.mean(solicitud)'''


#El servidor espera el tiempo que le indique la variable tiempoEspera

while(repeticiones>0):
    #create a socket object
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    idCliente = rd.randint(0, 119)
    mensaje = idCliente.to_bytes(2, 'big')
    
    tiempoEspera = rd.expovariate(1.0/promedio)
    solicitud.append(tiempoEspera)
    repeticiones -= 1
    
    #connection to hostname on the port
    clientsocket.connect((host, port))
    clientsocket.send(mensaje)
    
    #receive no more than 1024 bytes
    permitirAcceso = clientsocket.recv(1024)
    
    if (permitirAcceso == bytes(1)):
        print(str(idCliente) + ' ACCESO CONCEDIDO')
    else:
        print(str(idCliente) + ' ACCESO DENEGADO')
        
    time.sleep(tiempoEspera)
    
    clientsocket.close()
    
