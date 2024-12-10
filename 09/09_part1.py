# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:39:04 2024

@author: allam
"""

def main():
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        disk_map = puzzle_input.read().strip()

    
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
    
    freed_disk = []
    free_space = disk.count('.')
    iterator = 0
    r_iterator = -1
    occupied_space = len(disk) - free_space
    
    while iterator < len(disk) and iterator < occupied_space:
        if disk[iterator] == '.':
            
            while disk[r_iterator] == '.':
                r_iterator -= 1
            freed_disk.append(disk[r_iterator])
            r_iterator -= 1
            
        else:
            freed_disk.append(disk[iterator])
        iterator += 1
    
    return freed_disk 
    
    
def checksum(disk):
    checksum = 0
    for i, char in enumerate(disk):
        checksum += i * int(char)
        
    return checksum


main()