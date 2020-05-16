##############################################################################
# Memetic Algorithm for Multidimensional Two-Way Number Partitioning Problem #
# Autor: Luis Balderas Ruiz                                                  #
##############################################################################


import pandas as pd
import numpy as np

def lecturaDatos(nombre_archivo):
    data = pd.read_csv(nombre_archivo,header=None)
    return(data.to_numpy())


def MA_MDTWNPP(nombre_archivo, generaciones, n_poblacion, descendientes):
    data = lecturaDatos(nombre_archivo)
    poblacion = generaPoblacion(n_poblacion)
