# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

@author: 000420606, 000416688, 000437946
"""

import socket
import numpy as np

usuarioPermitidos = []
permitirAcceso = 0
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

while True:
    clientsocket,addr = serversocket.accept()
    
    idCliente = clientsocket.recv(1024)
    mensaje = int.from_bytes(idCliente, 'big')
    
    if(mensaje in usuarioPermitidos):   
        if (not(mensaje in adentro)):
            permitirAcceso = bytes(1)
            
            if(len(adentro)<=aforo):
                permitirAcceso = bytes(1)
            else:
                permitirAcceso = bytes(0) 
         
        else: 
            permitirAcceso = bytes(0)
    else: 
        permitirAcceso = bytes(0)
        
    #Evaluacion del Aforo

    
    clientsocket.send(permitirAcceso)
    clientsocket.close()

print('--DESCONECTADO--')


