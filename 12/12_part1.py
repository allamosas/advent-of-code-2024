# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 06:11:03 2024

@author: allam
 _____   ____  ____   ___ ___       _____ ____  ___ ___  __ __  _       ____  ______   ___   ____  
|     | /    ||    \ |   |   |     / ___/|    ||   |   ||  |  || |     /    ||      | /   \ |    \ 
|   __||  o  ||  D  )| _   _ |    (   \_  |  | | _   _ ||  |  || |    |  o  ||      ||     ||  D  )
|  |_  |     ||    / |  \_/  |     \__  | |  | |  \_/  ||  |  || |___ |     ||_|  |_||  O  ||    / 
|   _] |  _  ||    \ |   |   |     /  \ | |  | |   |   ||  :  ||     ||  _  |  |  |  |     ||    \ 
|  |   |  |  ||  .  \|   |   |     \    | |  | |   |   ||     ||     ||  |  |  |  |  |     ||  .  \
|__|   |__|__||__|\_||___|___|      \___||____||___|___| \__,_||_____||__|__|  |__|   \___/ |__|\_|


                    ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                           ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                           ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                     ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░ 
                    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
                    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░ 
                    ░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░      ░▒▓█▓▒░
"""

import copy

grid = []
explored_tiles = []

directions = {
    0: ( 0, -1),   # Mover en -y N
    1: ( 1,  0),   # Mover en +x E
    2: ( 0,  1),   # Mover en +y S
    3: (-1,  0)    # Mover en -x W
}

def main():    
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        for line in puzzle_input:
            grid.append(list(line.strip())) # Se crea una matriz de filas
                                              # evitando introducir el retorno
                                              # de carro con strip()
    #En explored_tiles se van tachando los cultivos que se cuenten                                          
    explored_tiles = copy.deepcopy(grid)
    
    total_price = 0
    perimeter = 0
    area = 0
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            perimeter, area = measure(x, y, grid, explored_tiles)
            if area!= 0:
                print(f'El perimetro de {grid[y][x]} es de {perimeter}')      
                print(f'El area de {grid[y][x]} es de {area}')            
                total_price += perimeter * area
        
    print(f'El coste total del huerto es {total_price} monedas de oro')
           


def measure(x, y, grid, explored_tiles, prev_crop = ''):
    crop = grid[y][x]
    perimeter = 0
    area = 0
    
    #Se comprueba que no se ha explorado ya
    if explored_tiles[y][x] == '.': 
        return 0, 0
    
    #Si se continua por el mismo cultivo o es el primero: 
    if prev_crop == crop or prev_crop == '':
        #Se marca como explorado
        explored_tiles[y][x] = '.' 
        area += 1
        
        #Se sigue avanzando en todas las direcciones
        for dx, dy in directions.values():
            nx, ny = x+dx, y+dy
            #Si se sale del mapa o el cultivo no coincide, aumenta el perimetro
            if not(is_inbounds(nx, ny, grid) and grid[ny][nx] == crop): 
                perimeter += 1
                
            if is_inbounds(nx, ny, grid): #Se comprueba que no se sale del mapa
                r_perimeter, r_area = measure(nx, ny, grid, explored_tiles, crop)
                perimeter += r_perimeter
                area += r_area
    
    return perimeter, area

          
            
def is_inbounds(pos_x, pos_y, grid):                  
    return pos_x >= 0 and pos_x < len(grid[0]) and pos_y >= 0 and pos_y < len(grid)     

        
        
main()