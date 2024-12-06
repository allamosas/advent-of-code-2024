# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 05:37:21 2024

@author: allam
"""

map = []
pos_x = -1
pos_y = -1
obstacles_found = []
infinite_loop = False

directions = { #El tuto de hoy es de diccionarios. a ver que tal
    0: (0, -1),   # Mover en -y N
    1: (1, 0),    # Mover en +x E
    2: (0, 1),    # Mover en +y S
    3: (-1, 0)    # Mover en -x W
}

guard_dir = 0


#Funcion que calcula si lo que hay delante es un obstaculo
def is_obstacle(guard_dir, pos_x, pos_y):
    
        global infinite_loop 
        dx, dy = directions.get(guard_dir) #Se suma el vector de direccion
        pos_x += dx
        pos_y += dy
        
        if is_inbounds(pos_x, pos_y): #Si no se sale del mapa
            if map[pos_y][pos_x] == '#': #Si hay un obstaculo
                if [pos_x, pos_y, guard_dir] not in obstacles_found: #Se hace un seguimiento del obstaculo y la direccion que llevaba el guardia
                    obstacles_found.append([pos_x, pos_y, guard_dir])
                else: #Si el guardia ya ha pasado por ahi en la misma dirección, es un bucle infinito
                    infinite_loop = True
                return True                
        else: #Si no, hay via libre
            return False
      
#Función que calcula para una x e y si se han salido del mapa o no
def is_inbounds(pos_x, pos_y):              
    if pos_x > 0 and pos_x < map_size[0] and pos_y > 0 and pos_y < map_size[1]:
        return True
    else:
        return False

#Función que calcula la ruta del guardia   
def patrol(pos_x, pos_y, guard_dir):
    
    global infinite_loop
    global obstacles_found
    obstacles_found = [] #Se reinicia la lista de obstaculos encontrados por el guardia
    
    walk_count = 0 #Esto ya no serviría en esta parte    
    while is_inbounds(pos_x, pos_y): #Se calcula la ruta mientras siga dentro del mapa
        
        if is_obstacle(guard_dir, pos_x, pos_y):
            guard_dir = (guard_dir + 1) % len(directions) #Se rota 90 grados a la siguiente direccion
            #Lo que he hecho para que la lista sea circular es usar modulos, 
            #de forma que si la dirección es 3, al calcularlo en mod 4, la 
            #nueva dirección 3+1 vuelve a ser 0 (norte)
            
        else:
            walk_count += 1            
            dx, dy = directions.get(guard_dir) #Se suma el vector de direccion
            pos_x += dx #Se actualizan las nuevas posiciones del guardia
            pos_y += dy
            
        if infinite_loop: #Si el flag del bucle es True, se reinicia y se encuentra un bucle infinito
            infinite_loop = False
            return True
    return False #Si no, es que se ha salido del mapa



with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        map.append(list(line.strip())) # Se crea una matriz de filas
                                          # evitando introducir el retorno
                                          # de carro con strip()
    
map_size = [len(map[0]), len(map)] #Dimensiones del mapa para posteriores calculos        
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
    
loops = 0
progress = 0 #Variable para calcular el progreso aproximado de la ejecucion y echar una meada
for y, line in enumerate(map): #Se recorre el mapa
    for x, cell in enumerate(line): 
        if cell == '.':         #Si se encuentra un sitio vacio y no esta en la boca del guardia
            map[y][x] = '#'     #Se coloca un obstaculo
            
            if patrol(pos_x, pos_y, guard_dir): #Se calcula la patrulla del guardia
                loops += 1
                print(f'Se han encontrado {loops} bucles infinitos')
                
            map[y][x] = '.'     #Se quita el obstaculo
            
        print(f'{int(progress/(map_size[0] * map_size[1]) * 100)}% ({progress}/{len(map) * len(map[0])})') #Progreso de la ejecucion
        progress+=1
        
print(f'Se han encontrado {loops} bucles infinitos')    


        
    
            
        
        
    
                                                 