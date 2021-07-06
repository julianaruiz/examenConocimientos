# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:40:14 2021

@author: Juliana

1.	Realizar un seudo código (algoritmo) que determine si una palabra que recibe por parámetro es 
palíndroma o no (Palíndroma es una palabra que leída de izquierda a derecha es igual que al leerla 
de derecha a izquierda). El parámetro que recibe la función es un vector, y en cada posición de éste 
se encuentra almacenada una letra de la palabra.
"""
print("Programa que muestra si una palabra es palíndroma o no \n")

def palindroma (palabra):
    palabraCopia = palabra[:]
    palabraCopia.reverse()
    tamanio = len(palabra)
    res = 1
    for i in range(0,tamanio):
        if palabra[i] != palabraCopia[i]:
            res = 0
    return res
    
palabra = input("Ingrese una palabra: ")

res = palindroma(list(palabra))      

if res == 1:
    print("Es palíndroma")
else:
    print("No es palíndroma")