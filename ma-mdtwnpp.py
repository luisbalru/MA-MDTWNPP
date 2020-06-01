##############################################################################
# Memetic Algorithm for Multidimensional Two-Way Number Partitioning Problem #
# Autor: Luis Balderas Ruiz                                                  #
##############################################################################


import pandas as pd
import numpy as np
import random
import time


def is_arr_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if elem is myarr), False)

def lecturaDatos(nombre_archivo):
    data = pd.read_csv(nombre_archivo,header=None)
    return(data.to_numpy(dtype=np.float32))

def arraytostr(arr):
    s = ""
    for i in range(len(arr)):
        s = s + str(arr[i]) + ','
    s = s[:-1]
    return(s)

def generaPoblacion(n_poblacion,n,data):
    poblacion = {}
    while len(poblacion) < n_poblacion:
        l = np.random.rand(n)
        l[l<0.5] = 0
        l[l>0.5] = 1
        l = l.astype(int)
        s = arraytostr(l)
        if s not in poblacion:
            _,poblacion[s] = fitness(l,data)
    return(poblacion)

def torneo(poblacion):
    a = random.randint(0,len(poblacion)-1)
    b = a
    while b == a:
        b = random.randint(0,len(poblacion)-1)
    cr1 = poblacion[list(poblacion.keys())[a]]
    cr2 = poblacion[list(poblacion.keys())[b]]
    if cr1 < cr2:
        return(list(poblacion.keys())[a])
    else:
        return(list(poblacion.keys())[b])


def crossover(crom1,crom2):
    crom1 = np.fromstring(crom1, dtype=int,sep=',')
    crom2 = np.fromstring(crom2, dtype=int,sep=',')
    desc = ""
    for i in range(len(crom1)):
        l = random.random()
        if l < 0.5:
            desc = desc + str(crom1[i]) + ','
        else:
            desc = desc + str(crom2[i]) + ','
    desc = desc[:-1]
    return(desc)

def mutacion(crom,porcentaje):
    arr = np.fromstring(crom,dtype=int,sep=',')
    tasa_mutacion = porcentaje * len(arr)
    cambios = random.sample(range(0,len(arr)),int(tasa_mutacion))
    for i in cambios:
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = 0
    return(arraytostr(arr))

def fitness(cromosoma,data):
    df0 = np.argwhere(cromosoma == 0)
    df1 = np.argwhere(cromosoma == 1)
    df0 = df0.reshape(df0.shape[0]).tolist()
    df1 = df1.reshape(df1.shape[0]).tolist()
    df0 = data[df0,:]
    df1 = data[df1,:]
    suma0 = np.sum(df0,axis=0)
    suma1 = np.sum(df1,axis=0)
    dif = np.abs(suma0-suma1)
    argmax = np.argmax(dif)
    max = np.max(dif)
    return(argmax,max)

def busquedaLocal(cromosoma,data,arg,fitness):
    df1 = np.argwhere(cromosoma == 1)
    df1 = df1.reshape(df1.shape[0]).tolist()
    df1 = data[df1,:]
    columna = df1[:,arg]
    fila = np.argmin(np.abs(columna-fitness))
    cromosoma[fila] = 0
    desc = arraytostr(cromosoma)
    return(desc)

def MA_MDTWNPP(nombre_archivo, generaciones, n_poblacion, porcentaje_mutacion):
    data = lecturaDatos(nombre_archivo)
    start = time.time()
    poblacion = generaPoblacion(n_poblacion,data.shape[1],data)
    for i in range(generaciones):
        prog1 = torneo(poblacion)
        prog2 = prog1
        while prog1 == prog2:
            prog2 = torneo(poblacion)
        desc = crossover(prog1, prog2)
        desc = mutacion(desc,0.2)
        arg_max,fitness_desc = fitness(np.fromstring(desc,dtype=int, sep=','),data)
        desc = busquedaLocal(np.fromstring(desc,dtype=int, sep=','),data,arg_max,fitness_desc/2)
        _,fitness_desc = fitness(np.fromstring(desc,dtype=int, sep=','),data)
        list_fitness = list(poblacion.values())
        list_fitness = np.array(list_fitness)
        max = np.max(list_fitness)
        arg_max = np.argmax(list_fitness)
        if max > fitness_desc:
            poblacion[desc] = fitness_desc
            del poblacion[list(poblacion.keys())[arg_max]]
    end = time.time()
    tiempo = end-start
    lista_final = list(poblacion.values())
    lista_final = np.array(lista_final)
    min = np.min(lista_final)
    mean = np.mean(lista_final)
    arg_min = np.argmin(lista_final)
    print("######################")
    print(nombre_archivo)
    print("######################")
    print("MEJOR DIVISIÓN")
    print(list(poblacion.keys())[arg_min])
    print("Fitness")
    print(min)
    print("MEDIA FITNESS")
    print(mean)
    print("TIEMPO")
    print(tiempo)


MA_MDTWNPP('data/mdgtw500_20a.txt',10000,5000,0.1)
MA_MDTWNPP('data/mdgtw500_20b.txt',10000,5000,0.1)
MA_MDTWNPP('data/mdgtw500_20c.txt',10000,5000,0.1)
MA_MDTWNPP('data/mdgtw500_20d.txt',10000,5000,0.1)
MA_MDTWNPP('data/mdgtw500_20e.txt',10000,5000,0.1)
