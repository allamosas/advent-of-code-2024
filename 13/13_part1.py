# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:36:26 2024

@author: allam
"""

grid = []

def main():    
    with open('example1.txt', 'r', encoding='utf-8') as puzzle_input:
        for line in puzzle_input:
            grid.append(list(line.strip())) # Se crea una matriz de filas
                                              # evitando introducir el retorno
                                              # de carro con strip()