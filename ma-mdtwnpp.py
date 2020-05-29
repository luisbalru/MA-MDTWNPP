##############################################################################
# Memetic Algorithm for Multidimensional Two-Way Number Partitioning Problem #
# Autor: Luis Balderas Ruiz                                                  #
##############################################################################


import pandas as pd
import numpy as np
import random


def is_arr_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if elem is myarr), False)

def lecturaDatos(nombre_archivo):
    data = pd.read_csv(nombre_archivo,header=None)
    return(data.to_numpy())

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
        s = arraytostr(l)
        if s not in poblacion:
            poblacion[s] = fitness(l,data)
    return(poblacion)

def torneo(poblacion):
    a = random.randint(0,len(poblacion))
    b = a
    while b == a:
        b = random.randint(0,len(poblacion))
    cr1 = poblacion[poblacion.keys()[a]]
    cr2 = poblacion[poblacion.keys()[b]]
    if cr1 > cr2:
        return(poblacion.keys()[a])
    else:
        return(poblacion.keys()[b])


def crossover(crom1,crom2):
    desc = ""
    for i in range(len(crom1)):
        l = random.random()
        if l < 0.5:
            desc = desc + crom1[i] + ','
        else:
            desc = desc + crom2[i] + ','
    desc = desc[:-1]
    return(desc)

def mutacion(crom,porcentaje):
    arr = np.fromstring(crom,dtype=int,sep=',')
    pop = np.arange(0,len(arr))
    cambios = random.sample(pop,porcentaje*len(arr))
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
    df0 = data[clase0,:]
    df1 = data[clase1,:]
    suma0 = np.sum(df0,axis=0)
    suma1 = np.sum(df1,axis=0)
    return(max(abs(suma0-suma1)))

def MA_MDTWNPP(nombre_archivo, generaciones, n_poblacion, n_descendientes,porcentaje_mutacion):
    data = lecturaDatos(nombre_archivo)
    poblacion = generaPoblacion(n_poblacion,data.shape[1],data)
    for i in range(generaciones):
        prog1 = torneo(poblacion)
        prog2 = prog1
        while prog1 == prog2:
            prog2 = torneo(poblacion)
        desc = crossover(prog1, prog2)
        desc = mutacion(desc,0.2)
        
