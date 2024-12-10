# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:46:30 2024

@author: allam
"""

grid = []

directions = {
    0: (0, -1),   # Mover en -y N
    1: (1, 0),    # Mover en +x E
    2: (0, 1),    # Mover en +y S
    3: (-1, 0)    # Mover en -x W
}


def main():    
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        for line in puzzle_input:
            grid.append(list(map(int, line.strip()))) # Se crea una matriz de filas
                                              # evitando introducir el retorno
                                              # de carro con strip()
        
    trail_number = count_trails(grid)
    print('\n'.join(str(line) for line in grid))
    print(f'Se han encontrado {trail_number} senderos')
    
    
def count_trails(grid):
    trails = 0
    for y, row in enumerate(grid):
        for x, level in enumerate(row):
            if level == 0:
                print('Se ha encontrado el inicio de un sendero')
                trail_score = find_path(x, y, grid)
                trails += trail_score
                print(f'El sendero de ({x}, {y}) tiene una puntuación de {trail_score}')
                
    return trails

def find_path(x, y, grid, prev_level = -1):
    level = grid[y][x]
    if level - prev_level != 1: #Se comprueba que el sendero es continuo
        return 0
    if level == 9: #Se comprueba si se ha llegado a la cima
        print('Se ha llegado a la cima del sendero')
        return 1
    #Se marca el nodo como visitado para evitar ciclos infinitos
    grid[y][x] = -1
    trail_count = 0
    #Se sigue avanzando en todas las direcciones
    for dx, dy in directions.values():
        nx, ny = x+dx, y+dy
        if is_inbounds(nx, ny, grid) and grid[ny][nx] != -1: #Se comprueba que no se sale del mapa ni se visitan nodos ya visitados
            trail_count += find_path(nx, ny, grid, level)
    
    #Se restaura el valor original del nivel
    grid[y][x] = level
    return trail_count
    
            
def is_inbounds(pos_x, pos_y, grid):                  
    return pos_x >= 0 and pos_x < len(grid[0]) and pos_y >= 0 and pos_y < len(grid)
    
    
main()