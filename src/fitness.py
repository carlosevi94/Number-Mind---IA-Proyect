# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:30:09 2017

@author: Carlos
"""
from llamalista import cargaArchivo

def fitnessChecker(listaAJudgar, listaFichero, aciertos):               
        check=0
        for i in range(len(listaFichero)):           
            if (check > aciertos):
                return False
            if (listaAJudgar[i] == listaFichero[i]):                
                check=check+1
        if(check != aciertos):
            return False
        else:
            return True
        
def fitnessTotal(lista):
    #totalDeArchivos=22
    fitnessQueHaceBien=0
    for i in range(22):
        pista, acierto = cargaArchivo(i)        
        valor=fitnessChecker(lista,pista,acierto)
        if(valor==True):
            #print("CON ESTA LISTA FUNCIONO PORQUE SOY UN CREMA")
            #print(pista)
            #print(acierto)
            fitnessQueHaceBien=fitnessQueHaceBien+1
    
    return fitnessQueHaceBien

#print("Fitness total: ")
#print(fitnessTotal([9, 2, 8, 1, 2, 3, 2, 7, 1, 8, 8, 9, 1, 4, 1, 9]))
#print("---------------------")
#print("Fitness total: ")
#print(fitnessTotal([2, 2, 8, 1, 9, 3, 2, 1, 7, 8, 8, 9, 1, 4, 1, 9]))