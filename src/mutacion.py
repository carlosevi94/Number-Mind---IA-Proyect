# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 12:53:30 2017

@author: Carlos
"""
from random import *
from Individuo import *

# OPERADORES DE MUTACION


def intercambioAleatorio(indiv,cambioporparametro):
    cambios=0
    listaNuestra=indiv.getLista()    
    
    if (cambioporparametro > 16) or (cambioporparametro == 0):
        cambios = randint(1,16)
        
    else:
        cambios = cambioporparametro
    
    for i in range(cambios):
        pos1=randint(0,15)
        pos2=randint(0,15)
        
        numero1=listaNuestra[pos1]
        numero2=listaNuestra[pos2]
        
        listaNuestra[pos1] = numero2
        listaNuestra[pos2] = numero1
    
    res = Individuo(listaNuestra)
    
    return res

def mutacionUniforme(indiv, probabilidadDeMutacion):
    mutacion=indiv.getLista()
    
    if(not(probabilidadDeMutacion>0 and probabilidadDeMutacion<10)):
        probabilidadDeMutacion=randint(0,10)
    
    for i in range(0,len(mutacion)-1):
        aleatorio2=randint(0,10)
        if(aleatorio2>probabilidadDeMutacion):
            mutacion[i]=randint(0,10)
    
    res = Individuo(mutacion)
    return res



