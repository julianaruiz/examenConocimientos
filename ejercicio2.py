#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:44:05 2021

@author: Juliana

2.	Dados 2 vectores X y W que contienen N y M números enteros positivos respectivamente, ordenados de mayor a menor 
en cada uno de los vectores, realizar una función en cualquier lenguaje .NET que me permita llenar otro vector Z con 
la mezcla ordenada de los dos vectores anteriores.
"""

X = [9,7,5,3,1] 
W = [16,14,12,10,8,6,4,2]

def vector(X, W):
    Z = X + W
    Z.sort(reverse=True)
    print(Z)

vector(X, W)