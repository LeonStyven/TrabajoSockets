# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

@author: 000420606, 000416688, 000437946
"""

import socket
import numpy as np

usuarioPermitidos = []
permitirAcceso = False
aforo = 100
adentro = [1, 5, 6]

#usuarios permitidos por lista de acceso o por posicion
for k in range(aforo):
    usuarioPermitidos.append(np.random.randint(0, 119))
    
#create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()
port = 9999

#bind to the port
serversocket.bind((host, port))

#queue up to 5 requests
serversocket.listen(5)

    
idCliente = serversocket.recv(1024)

if(idCliente in usuarioPermitidos):   
    if (not(idCliente in adentro)):
        permitirAcceso = True
    else: 
        permitirAcceso = False
else: 
    permitirAcceso = False
    
#Evaluacion del Aforo

if(len(adentro)<=aforo-1):
    permitirAcceso = True
else:
    permitirAcceso = False

serversocket.send(permitirAcceso)
        

print('--DESCONECTADO--')