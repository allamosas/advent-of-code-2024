# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 06:00:18 2024

@author: allam
"""
matrix = []
    
    
def x_search(matrix):
    count = 0
    
    # M M | M S
    #  A  |  A
    # S S | M S
    for y, line in enumerate(matrix): #Se itera en vertical
        for x, char in enumerate(line): #Se itera en horizontal
            if x + 2 < len(matrix) and y + 2 < len(line): #sin salirse
                if (matrix[x][y] == 'M'
                    and matrix[x+1][y+1] == 'A'
                    and matrix[x+2][y+2] == 'S'
                    ):
                    if((matrix[x+2][y] == 'S' and matrix[x][y+2] == 'M') #Se buscan si las esquinas son coincidentes
                       or (matrix[x+2][y] == 'M' and matrix[x][y+2] == 'S')):
                        count +=1
    
    # S M | S S
    #  A  |  A
    # S M | M M    
    for y, line in enumerate(matrix): #Se itera en vertical
        for x, char in enumerate(line): #Se itera en horizontal
            if x + 2 < len(matrix) and y + 2 < len(line): #sin salirse
                if (matrix[x][y] == 'S'
                    and matrix[x+1][y+1] == 'A'
                    and matrix[x+2][y+2] == 'M'
                    ):
                    if((matrix[x+2][y] == 'S' and matrix[x][y+2] == 'M') 
                       or (matrix[x+2][y] == 'M' and matrix[x][y+2] == 'S')):
                        count +=1
    
    return count

#Se recogen los valores del input en una lista y se introduce cada lista en una lista anidada
with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        matrix.append(list(line.strip())) # Se crea una matriz de filas
                                          # evitando introducir el retorno
                                          # de carro con strip()
                                                         
count = x_search(matrix)

print(count)
