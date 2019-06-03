# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as py 
import pandas as pd
import matplotlib.pyplot as plt


contenido = pd.read_csv('starwars.csv')
print(contenido.keys())
    
columnas_a_usar = ['name','gender','homeworld','species']

df = pd.read_csv(
        'starwars.csv',
        usecols=columnas_a_usar)
#print(df.keys())
#print(df)



#especie = df.groupby(['Tatooine','human'])

valores =[]
valor=[]


generos = df.groupby(['gender'])

for genero,personaje in generos :
    print(genero)
    print(personaje)
    print(len(personaje))
    homeworlds = personaje.groupby(["homeworld"])
    valores.append(len(personaje))
    print("valores",valores)
    for homeworld,personaje in homeworlds :
        print("Mundos",homeworld)
        valor.append(len(personaje))
        print("valor",valor)
    plt.xlabel('En x')
    plt.xlabel('En y')
    
    plt.plot([1,2,3],[1,2,4])

"""

homeworlds = df.groupby(['homeworld'])

for homeworld, personaje in  homeworlds :
    print(homeworld)    
    print(personaje)
    generos = personaje.groupby(['gender'])
    for genero,personaje in generos :
        print("Generos",genero)
"""



    
#print(especie)

#index = pd.MultiIndex.f .from_arrays(arrays,name =(''))