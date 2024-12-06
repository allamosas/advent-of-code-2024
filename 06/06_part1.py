# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 05:37:21 2024

@author: allam
"""

map = []
pos_x = -1
pos_y = -1

directions = { #El tuto de hoy es de diccionarios. a ver que tal
    0: (0, -1),   # Mover en -y N
    1: (1, 0),    # Mover en +x E
    2: (0, 1),    # Mover en +y S
    3: (-1, 0)    # Mover en -x W
}

guard_dir = 0

def is_obstacle(guard_dir, pos_x, pos_y):    
        dx, dy = directions.get(guard_dir) #Se suma el vector de direccion
        pos_x += dx
        pos_y += dy
        
        if is_inbounds(pos_x, pos_y):
            if map[pos_y][pos_x] == '#':
                return True
            elif map[pos_y][pos_x] == '.' or map[pos_y][pos_x] == 'X':
                return False
            else:
                print("Se ha encontrado un obstaculo extraño")
                return False
        else:
            return False
            
def is_inbounds(pos_x, pos_y):              
    if pos_x > 0 and pos_x < map_size[0] and pos_y > 0 and pos_y < map_size[1]:
        return True
    else:
        return False


with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        map.append(list(line.strip())) # Se crea una matriz de filas
                                          # evitando introducir el retorno
                                          # de carro con strip()
            
#Se busca la roomba
found = False
for y, line in enumerate(map):
    for x, guard in enumerate(line):
        if guard == "^":
            print(f"Guardia encontrado en la posición [{x}, {y}] mirando hacia el Norte")
            guard_dir = 0
            found = True
            break
        if guard == ">":
            print(f"Guardia encontrado en la posición [{x}, {y}] mirando hacia el Este")
            guard_dir = 1
            found = True
            break
        if guard == "v":
            print(f"Guardia encontrado en la posición [{x}, {y}] mirando hacia el Sur")
            guard_dir = 2
            found = True
            break
        if guard == "<":
            print(f"Guardia encontrado en la posición [{x}, {y}] mirando hacia el Oeste")
            guard_dir = 3
            found = True
            break
    if found:
        pos_x = x
        pos_y = y
        break    
    
#Se procede a buscar la ruta    

hit_count = 0
walk_count = 0
map_size = [len(map[0]), len(map)]

while is_inbounds(pos_x, pos_y):
    
    if is_obstacle(guard_dir, pos_x, pos_y):
        guard_dir = (guard_dir + 1) % len(directions) #Se rota 90 grados a la siguiente direccion
        hit_count += 1
        
        print(f'La rumba se la ha pegado contra un objeto en [{pos_x},{pos_y}]')
        
    else:
        walk_count += 1
        map[pos_y][pos_x] = 'X'
        
        dx, dy = directions.get(guard_dir) #Se suma el vector de direccion
        pos_x += dx
        pos_y += dy
        
        
        print(f'La rumba sigue derechita por [{pos_x},{pos_y}]')
        
print(f'Se han dado {walk_count} pasos')

area_explored = sum(line.count('X') for line in map) 

print(f'Se han explorado {area_explored} casillas')      
            
        
        
    
                                                 