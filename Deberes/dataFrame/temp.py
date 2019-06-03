# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


contenido = pd.read_csv('starwars.csv')
#print(contenido.keys())
    
columnas_a_usar = ['name','gender','homeworld','species']

df = pd.read_csv(
        'starwars.csv',
        usecols=columnas_a_usar)
#print(df.keys())
#print(df)

    

#especie = df.groupby(['Tatooine','human'])

generos = df.groupby('gender')
tipo_generos = []
total_generos_personajes = []



for genero,personaje in generos:
    print(genero)    
    print(len(personaje))
    tipo_generos.append(genero)
    total_generos_personajes.append(len(personaje)) 
 
    
index = np.arange(len(tipo_generos)) 
plt.bar(index,total_generos_personajes)   
plt.xlabel('generos')
plt.ylabel('Numero de personajes')

plt.xticks(index,tipo_generos,rotation=90)
 
plt.show()



homeworlds = df.groupby('homeworld')
mundos = []
total_humanos = []


for homeworld,species in homeworlds:
    print(homeworld)
    print(len(species['species']== 'Human'))
    mundos.append(homeworld)
    total_humanos.append(len(species['species']== 'Human'))
    
    
index = np.arange(len(mundos)) 
plt.bar(index,total_humanos)   
plt.xlabel('Mundos')
plt.ylabel('Humanos')

plt.xticks(index,mundos,rotation=90)
plt.show()
  

mundosGenero = []
femenino = []

for homeworld,gender in homeworlds: 
    print(homeworld)
    print(len(gender['gender']=='female'))
    mundosGenero.append(homeworld)
    femenino.append(len(gender['gender']=='female'))

index = np.arange(len(mundosGenero)) 
plt.bar(index,femenino)   
plt.xlabel('Mundos')
plt.ylabel('Femeninos')

plt.xticks(index,mundos,rotation=90)
plt.show()
    


"""
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