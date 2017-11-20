# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:08:43 2017

@author: Carlos
"""

from Individuo import *
import random
from mutacion import *
from operadoresDeVariacion import *
from estrategiasSeleccionRemplazo import *

def nuevoMain(tamanopoblacion,algoritmoDeMutacion,algoritmoDeCruce, estrategiaDeSeleccion, iteracionesMaximas):
    
    poblacion=[]
    poblacionElegida=[]
    granpoblacion=[]
    proximapoblacion=[]
    selectorMutacion=algoritmoDeMutacion
    selectorCruce=algoritmoDeCruce
    selectorSeleccion=estrategiaDeSeleccion
    fin=False
    esPrimerArranque=True
    
    IndividuoDePrueba=Individuo([5, 2, 9, 7, 2, 2, 3, 8, 3, 5, 9, 5, 4, 9, 9, 1])
    
    
    individuoMejorPorAhora=IndividuoDePrueba
    individuoGanador=0
    calidadMejorPorAhora=0
    contadorVueltas=0
    
    
    listaParaMediaDeFitness=[]
    
    def primerArranque():
        for i in range(22):
            padre1,aciertospadre1 = cargaArchivo(i)
            x = Individuo(padre1)
            poblacion.append(x)
        tamanopoblacionrestante=tamanopoblacion-22
        
        while (len(poblacion) < tamanopoblacion):
            x = random.randint(1,5)  
            randomselector=random.randint(0,21)
            randomselector2=random.randint(0,21)
            if(x==1):
                beta=poblacion[randomselector]                
                individuoAguardar=intercambioAleatorio(beta,0)
                poblacion.append(individuoAguardar)
            if(x==2):
                beta=poblacion[randomselector]                
                individuoAguardar=mutacionUniforme(beta,0)
                poblacion.append(individuoAguardar)
            if(x==3):
                alfa=poblacion[randomselector]
                beta=poblacion[randomselector2] 
                individuoAguardar1,individuoAguardar2 = recombinacionEnUnPunto(alfa,beta)
                poblacion.append(individuoAguardar1)
                poblacion.append(individuoAguardar2)
            if(x==4):
                alfa=poblacion[randomselector]
                beta=poblacion[randomselector2] 
                individuoAguardar1,individuoAguardar2 = recombinacionEnDosPuntos(alfa,beta)
                poblacion.append(individuoAguardar1)
                poblacion.append(individuoAguardar2)
            if(x==5):
                alfa=poblacion[randomselector]
                beta=poblacion[randomselector2] 
                individuoAguardar1,individuoAguardar2 = recombinacionUniforme(alfa,beta,5)
                poblacion.append(individuoAguardar1)
                poblacion.append(individuoAguardar2)
    
       
    
    while (fin==False):
        
        mejorPorVuelta=IndividuoDePrueba
        calidadMejorPorVuelta=0
        
        if (algoritmoDeMutacion == 0):
            selectorMutacion=random.randint(1,2)
     
        if (algoritmoDeCruce == 0):
            selectorCruce=random.randint(1,3)
        
        if (selectorSeleccion == 0):
            selectorSeleccion=random.randint(1,2)
    
        
        
        
        if (esPrimerArranque==True):
            primerArranque() 
            esPrimerArranque=False
         
        #print("Longitud poblacion "+str(len(poblacion)))    
        mitad=int(len(poblacion)/2)
        #Primer Paso: Seleccion
        if (selectorSeleccion == 1):
            poblacionElegida=seleccionPorTorneo(poblacion, mitad,2)
        elif (selectorSeleccion == 2):            
            poblacionElegida=seleccionPorRuleta(poblacion, mitad)
        
        #print("Longitud poblacion elegida "+str(len(poblacionElegida)))
        
        
        #Cruzamos individuos        
        condicion=False
        while(condicion==False):
     
           # print("Tamano antes del primer padre "+str(len(poblacionElegida)))
            al1=random.randint(0,len(poblacionElegida)-1)
            #print(al1)
            padre1=poblacionElegida.pop(al1)
            
            #print("Tamano antes del segundo padre "+str(len(poblacionElegida)))
            al2=random.randint(0,len(poblacionElegida)-1)
            #print(al2)
            padre2=poblacionElegida.pop(al2)
            
            #print("Tamano final "+str(len(poblacionElegida)))
            
            
            
            
            
            if (selectorCruce == 1):                
                indiv1,indiv2=recombinacionEnUnPunto(padre1,padre2)
            elif(selectorCruce == 2):
                indiv1,indiv2=recombinacionEnDosPuntos(padre1,padre2)
            elif(selectorCruce == 3):
                indiv1,indiv2=recombinacionUniforme(padre1,padre2,5)
            granpoblacion.append(indiv1)
            granpoblacion.append(indiv2)
            if(len(poblacionElegida)==0):
                condicion=True
            
            
        #Mutamos individuos  
        longitudParaSegundoFor=len(granpoblacion)
        contadorMutaciones=0
        for i in range(longitudParaSegundoFor):      
            #print("Estoy mutando")
            padre1=granpoblacion[i]      
            if (selectorMutacion == 1):
                indiv=intercambioAleatorio(padre1,5)
            elif(selectorMutacion==2):
                indiv=mutacionUniforme(padre1,5)
            granpoblacion.append(indiv)
            #print(contadorMutaciones)
            contadorMutaciones=contadorMutaciones+1
    
        #Buscamos al mejor
        #print("Antes del for")
        #print(len(granpoblacion))
        for a in granpoblacion:
            #print("Dentro del for")
            if(a.getCalidad()==22):
                individuoGanador=a
                fin=True
                print("---------------------------------------")
                print("------------Fin del Algoritmo----------")
                print("SE HA ENCONTRADO UNA SOLUCION ")
                print(individuoGanador.getLista())
                print("Con un fitness de: "+str(individuoGanador.getCalidad()))
                print("---------------------------------------")
                
            if(a.getCalidad()>calidadMejorPorAhora):
                individuoMejorPorAhora=a
                calidadMejorPorAhora=a.getCalidad()
            if(a.getCalidad()>calidadMejorPorVuelta):
                mejorPorVuelta=a
                calidadMejorPorVuelta=a.getCalidad()
                listaParaMediaDeFitness.append(calidadMejorPorVuelta)
                #print(a)
        #print("Despues del for")
        
        
        print("---------------------------------------")
        print("Iteracion: "+str(contadorVueltas))
        print("Mejor Fitness encontrado = "+str(calidadMejorPorAhora))
        print("Mejor Fitness encontrado en esta iteracion = "+str(calidadMejorPorVuelta))
        
        
        #Comprobamos las vueltas
        if(contadorVueltas==iteracionesMaximas):
            fin=True
            print("---------------------------------------")
            print("------------Fin del Algoritmo----------")
            print("No se ha encontrado una solucion exacta, pero el mejor candidato es: ")
            print(individuoMejorPorAhora.getLista())
            print("Con un fitness de: "+str(individuoMejorPorAhora.getCalidad()))
            print("---------------------------------------")
            print("La media de fitness por Generacion es de")
            total=0
            for i in listaParaMediaDeFitness:
                total=total+i
            res=total/len(listaParaMediaDeFitness)
            print(res)
        contadorVueltas=contadorVueltas+1
            
        #Reemplazo
        proximapoblacion.extend(poblacion)
        proximapoblacion.extend(granpoblacion)
        
        
        
        proximapoblacion.sort(key=lambda individuo: individuo.calidad, reverse=True)
        aux=proximapoblacion[0:tamanopoblacion]
        poblacion=aux[:]
        granpoblacion=[]
    
    
    
    
    
    
def lanzador():
    print("----------- NUMBER MIND------------------")
    print("Bienvenido a Number Mind. Trabajo realizado por Carlos Sevilla Barcelo y Francisco Javier Fernandez Montero")    
    print("Este programa dispone de 2 metodos de lanzamiento. Uno que permite elegir parametros sobre el funcionamiento del algoritmo, y otro que lanza el algoritmo con las opciones seleccionada de forma aleatoria")
    print("Si introduce un 0, se inicia el modo parametrizado.")
    print("Si introduce un 1, se inicia poblacion 200; 200 iteraciones; usando Intercambio Aleatorio, Recombinacion en un punto y seleccion por Torneo ")
    print("Si introduce un 2, se inicia poblacion 200; 200 iteraciones; usando Intercambio Aleatorio, Recombinacion Uniforme y seleccion por Ruleta ")
    print("Si introduce un 3, se inicia con poblacion 200; 200 iteraciones; usando Mutacion uniforme, Recombinacion Uniforme y seleccion por Ruleta ")
    
    eleccion=input("Introduce su eleccion: ")
    
    if(eleccion=="3"):
        print("Poblacion de 200. Iteraciones maximas: 200; Mutacion uniforme, Recombinacion Uniforme y seleccion por ruleta ")
        nuevoMain(200,2,3, 2, 200)
    if(eleccion=="1"):
        print("Poblacion de 100. Iteraciones maximas: 200; Intercambio Aleatorio, Recombinacion en un punto y seleccion por Torneo")
        nuevoMain(100,1,3, 2, 200)
    if(eleccion=="2"):
        print("Poblacion de 100. Iteraciones maximas: 200; Intercambio Aleatorio, Recombinacion Uniforme y seleccion por Ruleta ")
        nuevoMain(100,1,1, 1, 200)
        
    if(eleccion=="0"):
        print("Lanzamiento parametrizado")
        print("---------------------------")
        tamano=input("Introduzca la poblacion del algoritmo ")
        print("---------------------------")
        print("Operaciones de mutacion")
        print("Introduce 1 si desea utilizar Intercambio Aleatorio")
        print("Introduce 2 si desea utilizar Mutacion Uniforme")
        mutation=input("Introduzca la opcion que desea: ")
        print("---------------------------")
        print("Operaciones de cruzamiento")
        print("Introduce 1 si desea utilizar Recombinacion en un punto")
        print("Introduce 2 si desea utilizar Recombinacion en dos punto")
        print("Introduce 3 si desea utilizar Recombinacion uniforme")
        cruzamiento=input("Introduzca la opcion que desea: ")
        print("---------------------------")
        print("Estrategia de Seleccion")
        print("Introduce 1 si desea utilizar seleccion por Torneo") 
        print("Introduce 2 si desea utilizar seleccion por Ruleta")
        selec=input("Introduzca la opcion que desea: ")
        print("---------------------------")
        itemax=input("Intoduzca el numero de iteraciones maximas que realiza el algoritmo: ")
        nuevoMain(int(tamano),int(mutation),int(cruzamiento), int(selec), int(itemax))
        
        
    
    
lanzador() 
    
    
        