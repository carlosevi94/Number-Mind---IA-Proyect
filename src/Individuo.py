# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:58:05 2017

@author: Carlos
"""
from fitness import *

class Individuo(): 
    
    lista=[]
    calidad=0
    
    def __init__(self, lista):
        self.lista = lista
        self.calidad = fitnessTotal(lista)
        
    def getLista(self):
        return self.lista
    
    def getCalidad(self):
        return self.calidad
        


  
        
    

    