# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:39:04 2024

@author: allam
"""

def main():
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        disk_map = puzzle_input.read().strip()

    #disk_map = '2333133121414131402'
    
    disk = generate_blocks(disk_map)
    print('Disco generado:')
    print(disk)
    
    freed_disk = free_disk(disk)
    print('Disco liberado:')  
    print(freed_disk)    
        
        
    print(f'El checksum del disco es: {checksum(freed_disk)}')
        
        
def generate_blocks(disk_map):
    disk = [] #MEUNDOS HIJOS DE PUTA. HAY QUE HACERLO CON UN ARRAY DE INTS PORQUE SI NO ELCONSUMO DE ESPACIO DE STRINGS SE SALE DEL BUFFER
    current_id = 0
    update_id = False
    for i, char in enumerate(disk_map):
        if i%2 == 0:
            if update_id:
                current_id = (current_id + 1) #Son unos cabrones. No dicen nada sobre los ids
                update_id = False
            for j in range(int(char)):
                disk.append(current_id)
        else:
            update_id = True
            for j in range (int(char)):
                disk.append('.')
    return disk


def free_disk(disk):
    
    freed_disk = disk.copy()
    free_space = disk.count('.')
    iterator = 0
    r_iterator = -1
    occupied_space = len(disk) - free_space
    
    #1 Se busca el siguiente bloque de la derecha
    #2 Se busca un hueco donde pueda encajar
        #Si se encuentra
            #3 Se sustituye el hueco por el bloque
        #Si no
            #4 Se sigue buscando hasta llegar al sitio en el que esta el bloque
    condicion = True    
    while condicion:
        #1 Se busca el siguiente bloque de la derecha
        if disk[r_iterator] != '.':
            print('Se ha encontrado un bloque')
            #Se recoge el bloque
            block = []
            block.append(disk[r_iterator])
            while block[0] == disk[r_iterator - 1] and disk[r_iterator -1] != disk[0]: #Se mira si coincide el siguiente elemento
                r_iterator -= 1
                block.append(disk[r_iterator])
            print(f'El bloque {block} es de longitud {len(block)}')
            #2 Se busca un hueco donde pueda encajar
            gap = 0 #Se cuenta el tamaño del hueco
            for iterator in range(len(disk) + r_iterator): #Se busca hasta llegar al sitio en el que esta el bloque
                if disk[iterator] == '.':
                    gap += 1
                    
                    if gap == len(block): #Si se encuentra un hueco en el que quepa
                        print('Se ha encontrado un hueco en el que cabe el bloque')
                        for c_block in range(len(block)): #Se sustituyen los caracteres del hueco por los del bloque
                            disk[iterator - c_block] = block[c_block] 
                            disk[r_iterator + c_block] = '.'
                        print(f'Se ha introducido el bloque {block}:')
                        print(f'{disk}')
                        break
                else:
                    gap = 0
        r_iterator -= 1
        print('Se sigue buscando otro bloque')
        if r_iterator + len(disk) <= 0:
            condicion = False
            
    return disk    
    
    
def checksum(disk):
    checksum = 0
    for i, char in enumerate(disk):
        if char != '.':
            checksum += i * int(char)
        
    return checksum


main()