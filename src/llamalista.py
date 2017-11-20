# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:19:42 2017

@author: Carlos
"""
import json

def cargaArchivo(numero):
    archivo = open("Grupo-072.txt", "r")  
    linea = archivo.readlines()    
    splitear=linea[numero]    
    lista,aciertos=splitear.split()        
    #Lista
    listanueva=json.loads(lista)
    #Acierto
    nuevoacierto=aciertos[1]    
    numerofinal=int(nuevoacierto)
    
   
      
    return listanueva, numerofinal
    
    archivo.close()


