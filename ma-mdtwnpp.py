##############################################################################
# Memetic Algorithm for Multidimensional Two-Way Number Partitioning Problem #
# Autor: Luis Balderas Ruiz                                                  #
##############################################################################


import pandas as pd
import numpy as np

def is_arr_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if elem is myarr), False)

def lecturaDatos(nombre_archivo):
    data = pd.read_csv(nombre_archivo,header=None)
    return(data.to_numpy())

def generaPoblacion(n_poblacion,n):
    poblacion = []
    while len(poblacion) < n_poblacion:
        l = np.random.rand(n)
        l[l<0.5] = 0
        l[l>0.5] = 1
        if not(is_arr_in_list(l,poblacion)):
            poblacion.append(l)
    return(np.array(poblacion))


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

def MA_MDTWNPP(nombre_archivo, generaciones, n_poblacion, descendientes):
    data = lecturaDatos(nombre_archivo)
    poblacion = generaPoblacion(n_poblacion,data.shape[1])
