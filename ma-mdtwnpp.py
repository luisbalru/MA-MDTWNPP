##############################################################################
# Memetic Algorithm for Multidimensional Two-Way Number Partitioning Problem #
# Autor: Luis Balderas Ruiz                                                  #
##############################################################################


import pandas as pd
import numpy as np
from random import randint

def lecturaDatos(nombre_archivo):
    data = pd.read_csv(nombre_archivo,header=None)
    return(data.to_numpy())

def generaPoblacion(data,n_poblacion,n):
    poblacion = []
    for i in range(n_poblacion):
        l = []
        for j in range(n):
            l.append(randint(0,1))
        poblacion.append(l)
    return(np.array(poblacion))


def fitness(clase0,clase1,data):
    df0 = data[clase0,:]
    df1 = data[clase1,:]
    suma0 = np.sum(df0,axis=0)
    suma1 = np.sum(df1,axis=0)
    return(max(abs(suma0-suma1)))

def MA_MDTWNPP(nombre_archivo, generaciones, n_poblacion, descendientes):
    data = lecturaDatos(nombre_archivo)
    poblacion = generaPoblacion(data,n_poblacion)
