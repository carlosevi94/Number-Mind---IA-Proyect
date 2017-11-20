import random

def seleccionPorTorneo(listaDeIndividuos, numeroIndividuosASeleccionar, k):
    
    
    listaAuxiliar=listaDeIndividuos[:]
    listaDeSelecciados=[]
    torneo=[]
    listaFitness=[]
    individuoSeleccionado=[]
    indice=0
     
    if(numeroIndividuosASeleccionar >= len(listaDeIndividuos) or numeroIndividuosASeleccionar<=0 or numeroIndividuosASeleccionar%2==1):
        numeroIndividuosASeleccionar=int(len(listaDeIndividuos)/2)
        if(numeroIndividuosASeleccionar%2==1):
            numeroIndividuosASeleccionar-=1
        
    for i in range(numeroIndividuosASeleccionar):
        for j in range(k):
            num=int(len(listaAuxiliar))
            aleatorio = random.randrange(num)
            individuoSeleccionado=listaAuxiliar.pop(aleatorio)
            torneo.append(individuoSeleccionado)
            listaFitness.append(individuoSeleccionado.getCalidad()) 
        indice=listaFitness.index(max(listaFitness),0,k)  
        individuoSeleccionado=torneo.pop(indice)
        listaAuxiliar.extend(torneo)        
        del torneo[:]
        del listaFitness[:]
        listaDeSelecciados.append(individuoSeleccionado)    
    
    return listaDeSelecciados


def calcularListaFitness(listaDeIndividuos):
    listaFitness=[]
    for i in range(len(listaDeIndividuos)):
        listaFitness.append(listaDeIndividuos[i].getCalidad())    
    return listaFitness

def calcularListaFitnessAcumulativa(listaDeFitness):
    res=[]
    res.append(listaDeFitness[0])    
    for i in range(len(listaDeFitness)-1):
        res.append(res[i]+listaDeFitness[i+1])        
    return res

def seleccionPorRuleta(listaDeIndividuos, numeroIndividuosASeleccionar):
    res=listaDeIndividuos[:]    
    listaFitness=calcularListaFitness(listaDeIndividuos)
    listaFitnessAcumulativa=calcularListaFitnessAcumulativa(listaFitness)
    
    aux=[]    
    indice=0
    total=0
    
    while(total<numeroIndividuosASeleccionar):
        r=random.randrange(listaFitnessAcumulativa[(len(listaFitnessAcumulativa)-1)]-1)
        indice=0
        for i in range(len(listaFitness)):
            if r > listaFitnessAcumulativa[i]:
                indice=indice+1
            else:
                break
            
        if aux.count(indice) <1:
            aux.append(indice)
            total=total+1            
        
    for i in aux:
        res.append(listaDeIndividuos[i])   
    
    return res