#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:43:42 2017

@author: javi
"""
import random
from Individuo import *
#OPERADORES DE CRUZAMIENTO

#def recombinacionEnUnPunto(genotipo1, genotipo2):
#    
#    
#    
#    hijo1 = genotipo1[:]
#    hijo2 = genotipo2[:]
#    
#    aleatorio=random.randrange(1,len(genotipo1))
#
#
#    for i in range(aleatorio,len(genotipo1)):
#        hijo1[i]=genotipo2[i]
#        hijo2[i]=genotipo1[i]
#    
#    return [hijo1,hijo2]

def recombinacionEnUnPunto(indiv1, indiv2):
    genotipo1 = indiv1.getLista()
    genotipo2 = indiv2.getLista()
    
    hijo1 = genotipo1[:]
    hijo2 = genotipo2[:]
    
    aleatorio=random.randrange(1,len(genotipo1))


    for i in range(aleatorio,len(genotipo1)):
        hijo1[i]=genotipo2[i]
        hijo2[i]=genotipo1[i]
    
    
    hijo1=Individuo(hijo1)
    hijo2=Individuo(hijo2)
    
    return hijo1,hijo2              
        
def recombinacionEnDosPuntos(indiv1, indiv2):
    genotipo1 = indiv1.getLista()
    genotipo2 = indiv2.getLista()       
    
    hijo1 = genotipo1[:]
    hijo2 = genotipo2[:]
    
    aleatorio1=random.randrange(1,len(genotipo1))
    aleatorio2=random.randrange(aleatorio1,len(genotipo1))
    
    #print('aleatorio1 = ', aleatorio1)
    #print('aleatorio2 = ', aleatorio2)
    
    for i in range(aleatorio1,len(genotipo1)):
        if (i>=aleatorio1 and i<=aleatorio2):
            hijo1[i]=genotipo2[i]
            hijo2[i]=genotipo1[i]
    
    
    hijo1=Individuo(hijo1)
    hijo2=Individuo(hijo2)
    
    return hijo1,hijo2


def recombinacionUniforme(padre1, padre2,probabilidadDeMutacion):
    padre1=padre1.getLista()
    padre2=padre2.getLista()
    
    hijo1 = padre1[:]
    hijo2 = padre2[:]
    
    if(not(probabilidadDeMutacion>0 and probabilidadDeMutacion<10)):
        probabilidadDeMutacion=random.randrange(10)
    
    for i in range(0,len(padre1)-1):
        aleatorio2=random.randrange(10)
        if(aleatorio2>probabilidadDeMutacion):
            hijo1[i]=padre2[i]
            hijo2[i]=padre1[i]
    
    hijo1=Individuo(hijo1)
    hijo2=Individuo(hijo2)
        
    return hijo1,hijo2
    


#def pruebaRecombinacionEnUnPunto():
#    genotipo1=[1,2,3,4,5]
#    genotipo2=[6,7,8,9,0]
#    
#    hijo1,hijo2=recombinacionEnUnPunto(genotipo1,genotipo2)
#    
#    print('Padre 1: ',genotipo1)
#    print('Padre 2: ',genotipo2)
#    
#    print('Hijo 1: ',hijo1)
#    print('Hijo 2: ',hijo2)
#
#
#def pruebaRecombinacionEnDosPuntos():
#    genotipo1=[1,2,3,4,5]
#    genotipo2=[6,7,8,9,0]
#    
#    hijo1,hijo2=recombinacionEnDosPuntos(genotipo1,genotipo2)
#    
#    print('Padre 1: ',genotipo1)
#    print('Padre 2: ',genotipo2)
#    
#    print('Hijo 1: ',hijo1)
#    print('Hijo 2: ',hijo2)
#
#
#pruebaRecombinacionEnUnPunto()    
#pruebaRecombinacionEnDosPuntos()

#def compruebaMutacionUniforme():
#    genotipo1=[1,2,3,4,5]
#    print('Genotipo inicial: ', genotipo1)
#
#    mutado=mutacionUniforme(genotipo1,98)   
#    print('Genotipo mutado: ', mutado)


#def pruebaRecombinacionUniforme():
#    genotipo1=[1,2,3,4,5]
#    genotipo2=[6,7,8,9,0]
#    
#    hijo1,hijo2=recombinacionUniforme(genotipo1,genotipo2,5)
#   
#    print('Padre 1: ',genotipo1)
#    print('Padre 2: ',genotipo2)
#    
#    print('Hijo 1: ',hijo1)
#    print('Hijo 2: ',hijo2)

    
    
    