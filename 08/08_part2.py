# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:15:20 2024

@author: allam
"""

import itertools

grid = []
antinode_grid = []


def main():    
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        for line in puzzle_input:
            grid.append(list(line.strip())) # Se crea una matriz de filas
                                              # evitando introducir el retorno
                                              # de carro con strip()
    
    antinode_grid = find_antinodes(grid)
    
    total_antinodes = sum(line.count('#') for line in antinode_grid)
    print(f'Se han encontrado {total_antinodes} antinodos')
    
            
           
def find_antinodes(grid):  
    antinode_grid = [['' for _ in range(len(grid[0]))] for _ in range(len(grid))] #Se crea un grid de antinodos para poder rellenarlo más tarde
    #De esta manera, se puede llevar el recuendo de los antinodos que coinciden con nodos   
    
    #Se buscan los diferentes nodos y sus posiciones
    nodes = find_different_nodes(grid)
    
    for key in nodes.keys(): #Por cada clase de nodo
        permutations = list(itertools.permutations(nodes[key], 2)) #Se calculan las permutaciones entre sus nodos
        #Con set se pueden eliminar las permutaciones duplicadas
        unique_permutations = set(tuple(sorted(p)) for p in permutations)
        
        #Ahora estan casi listos para ser sumados y restados
        for tupla in unique_permutations: #Por cada tupla
            vector = [v1 - v2 for v1, v2 in zip(tupla[0], tupla[1])]
            print(f'{tupla[0]} + {vector}')
            
            #Vaya cacao llevo encima
            #Hay que cambiar el formato de datos de lista a tupla del vector para que se puedan sumar y restar
            #De forma alternativa, se pueden sumar y restar elemento a elemento:
            antinodo1 = [a + b for a, b in zip(tupla[0], vector)] #Se suma el vector al primer nodo
            antinodo2 = [a - b for a, b in zip(tupla[1], vector)] #Se resta el vector al segundo nodo
            
            #Vale, para este segundo ejercicio, en lugar de crear un antinodo, se calculan todos los armonicos
            #De forma que se van marcando todos los armonicos hasta que se salgan del mapa
            while is_inbounds(antinodo1[0],antinodo1[1], antinode_grid):
                antinode_grid[antinodo1[1]][antinodo1[0]] = '#'
                antinodo1 = [a + b for a, b in zip(antinodo1, vector)] #Se vuelve a sumar el vector al primer nodo
                
            while is_inbounds(antinodo2[0],antinodo2[1], antinode_grid):
                antinode_grid[antinodo2[1]][antinodo2[0]] = '#'
                antinodo2 = [a - b for a, b in zip(antinodo2, vector)] #Se vuelve a restar el vector al segundo nodo
                
            #Además, hay que añadir un antinodo en la antena SI esta no es la unica de su frecuencia
            #Es decir:
            if len(nodes[key]) != 1:
                antinode_grid[tupla[0][1]][tupla[0][0]] = '#'
                antinode_grid[tupla[1][1]][tupla[1][0]] = '#'
                
            
        print_grid(antinode_grid)
        
    return antinode_grid

                                          
def find_different_nodes(grid):
    nodes = {} #Se inicia un diccionario y se recorre el input buscando los nodos
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != '.':
                if char not in nodes: #Si no está, se inicia una lista vacia
                    nodes[char] = []
                nodes[char].append((x,y)) #Se añade la posicion a la lista
    return nodes
                                              
        
            
def is_inbounds(pos_x, pos_y, grid):                  
    if pos_x >= 0 and pos_x < len(grid[0]) and pos_y >= 0 and pos_y < len(grid):
        return True
    else:
        return False                                              
                 

def print_grid(grid):
    for row in grid:
        for char in row:
            if char == '':
                char = ' '
            print(char,end='')
        print()    
        
                                              
main()                                              