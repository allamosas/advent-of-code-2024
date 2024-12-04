# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 06:00:18 2024

@author: allam
"""
matrix = []

def horizontal_search(matrix):
    count = 0
    #Se comprueba en que dirección se busca
        
    for line in matrix: #Por cada linea se busca que aparezca SAMX
        for i, char in enumerate(line):
            if i + 3 < len(line):
                if (line[i] == 'S' 
                    and line[i+1] == 'A' 
                    and line[i+2] == 'M' 
                    and line[i+3] == 'X'
                        ):
                    count += 1  
                    
    for line in matrix: #Por cada linea se busca que aparezca XMAS
        for i, char in enumerate(line):
            if i + 3 < len(line):
                if (line[i] == 'X' 
                    and line[i+1] == 'M' 
                    and line[i+2] == 'A' 
                    and line[i+3] == 'S'
                        ):
                    count += 1    
    return count
    
def vertical_search(matrix, reverse = False):
    #Para evitarme dos minutos de programar, voy a transponer la matriz xddd
    transposed = [list(line) for line in zip(*matrix)]
    count = horizontal_search(transposed)  
    
    return count
    
    
def r_diagonal_search(matrix):
    count = 0
    
    for y, line in enumerate(matrix): #Se itera en vertical
        for x, char in enumerate(line): #Se itera en horizontal
            if x + 3 < len(matrix) and y + 3 < len(line): #sin salirse
                if (matrix[x][y] == 'X'
                    and matrix[x+1][y+1] == 'M'
                    and matrix[x+2][y+2] == 'A'
                    and matrix[x+3][y+3] == 'S'
                    ):
                    count += 1                    
    
    for y, line in enumerate(matrix): #Se itera en vertical
        for x, char in enumerate(line): #Se itera en horizontal
            if x + 3 < len(matrix) and y + 3 < len(line): #sin salirse
                if (matrix[x][y] == 'S'
                    and matrix[x+1][y+1] == 'A'
                    and matrix[x+2][y+2] == 'M'
                    and matrix[x+3][y+3] == 'X'
                    ):
                    count += 1   
    
    return count
    
    
def l_diagonal_search(matrix):
    #voy a reflejar la matriz para ahorrarme otros dos minutos xdddd
    #quien me iba a decir que el hijoputa de javi iba a enseñarme algo util
    #voy a amortizar calculo al final y todo
    reflected = [line[::-1] for line in matrix]
    count = r_diagonal_search(reflected)  
    
    return count
    

#Se recogen los valores del input en una lista y se introduce cada lista en una lista anidada
with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        matrix.append(list(line.strip())) # Se crea una matriz de filas
                                          # evitando introducir el retorno
                                          # de carro con strip()
                                                         
            
count = ( horizontal_search(matrix) 
         + vertical_search(matrix) 
         + r_diagonal_search(matrix) 
         + l_diagonal_search(matrix))

print(count)
