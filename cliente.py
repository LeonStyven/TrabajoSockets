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
import random as rd
import time 
import numpy as np 
import matplotlib.pyplot as plt

#NOTA: LA CANTIDAD DE REPETICIONES EN EL CLIENTE, DEBE SER LA MISMA QUE EL NUMERO DE VECES QUE SE EJECUTA EL FOR EN EL SERVIDOR


#Declaracion de variables

idCliente = 0           #ID del usuario que ingresa
promedio = 0.1          #Valor promedio en segundos para el acceso de usuarios
solicitud = [0]         #Variable que almacena el tiempo que el servidor espera antes de la siguiente consulta
repeticiones = 120      #Numero de solicitudes al servidor

#Informcion local para el manejo de la direccion del servidor
host = socket.gethostname()
port = 9999


#Al entrar en el while, el cliente comienza a generar eventos al servidor

while(repeticiones>0):
    
    #Creacion del Socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Obtener el ID del cliente de forma aleatoria
    idCliente = rd.randint(0, 119)
    mensaje = idCliente.to_bytes(2, 'big')
    
    #Obtener tiempo que el servidor debe esperar antes de la siguiente consulta
    tiempoEspera = rd.expovariate(1.0/promedio)
    solicitud.append(tiempoEspera)
    repeticiones -= 1
    
    #Conexion con el servidor
    clientsocket.connect((host, port))
    
    #Comunicacion con el servidor
    clientsocket.send(mensaje)
    permitirAcceso = clientsocket.recv(1024)
    
    
    #Según la respuesta del servidor, el programa evalua si permite o no la entrada del usuario
    if (permitirAcceso == bytes(1)):
        print(str(idCliente) + ' ACCESO CONCEDIDO')
    elif(permitirAcceso== bytes(0)):
        print(str(idCliente) + ' ACCESO DENEGADO')
    else:
        print(str(idCliente) + ' Saliendo...')
    time.sleep(tiempoEspera)
    
    #Cerrar la conexion con el servidor
    clientsocket.close()
    
