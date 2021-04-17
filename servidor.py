# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:40:30 2021

Autores:

Julian Styven Colorado Agudelo - 000420606
Pablo Loaiza Mejia - 000416688
Santiago Sanchez Giraldo - 000437946

"""

#Importacion de librerias
import socket
import numpy as np
import matplotlib.pyplot as plt

#NOTA: LA CANTIDAD DE REPETICIONES EN EL CLIENTE, DEBE SER LA MISMA QUE EL NUMERO DE VECES QUE SE EJECUTA EL FOR EN EL SERVIDOR



#Declaracion de variables
usuariosPermitidos = []         #Lista de IDs de usuarios que pueden entrar
permitirAcceso = 0              #Variable que determina sin una persona puede o no entrar a la universidad
aforo = 100                     #Aforo maximo de la U
adentro = []                    #Listado de IDs de personas dentro de la universidad
cantidadUsuarios = []           #Numero de usuarios dentro de la Universidad


#Generacion de lista de usuarios permitidos = aforo
while(len(usuariosPermitidos)<aforo):
    usuarioAleatorio = np.random.randint(0, 119)
    if(not(usuarioAleatorio in usuariosPermitidos)):
        usuariosPermitidos.append(usuarioAleatorio)
    
    
print(usuariosPermitidos)
    
#Creacion del socket por parte del servidor
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Obtener dereccion del servidor segun la informacion del propio equipo
host = socket.gethostname()
port = 9999


#Establecer host y puerte en el va a trabajar el servidor
serversocket.bind((host, port))

#Cola para clientes entrantes
serversocket.listen(5)

#Comunicacion con el cliente
for k in range(120):
    
    #Establecer conexion con el cliente
    clientsocket,addr = serversocket.accept()
    
    #Comunicacion con cliente
    idCliente = clientsocket.recv(1024)
    mensaje = int.from_bytes(idCliente, 'big')
    
    #Evaluacion del ID del usuario 
    if(mensaje in usuariosPermitidos):   
        if (not(mensaje in adentro)):
            permitirAcceso = bytes(1)
            if(len(adentro)<=aforo):
                permitirAcceso = bytes(1)
                adentro.append(mensaje)
                cantidadUsuarios.append(len(adentro))
            else:
                permitirAcceso = bytes(0)
        else: 
            permitirAcceso = bytes(2)
            adentro.remove(mensaje)
            cantidadUsuarios.append(cantidadUsuarios[-1]-1)   
    else: 
        permitirAcceso = bytes(0)
        
    #Enviar el resultado de la evaluacion, y cerrar la conexion
    clientsocket.send(permitirAcceso)
    clientsocket.close()

#Grafica de la cantidad de usuarios dentro de la universidad a lo largo del tiempo
plt.grid(True)
plt.plot(cantidadUsuarios)
plt.show()

