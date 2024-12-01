# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:35:14 2024

@author: allam
"""
left_list = []
right_list = []

#Se recogen los valores del input en dos listas
with open('input', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        left_list.append(int(line.split('   ')[0]))  #Item de la izquierda en la lista izquierda
        right_list.append(int(line.split('   ')[1])) #Item de la derecha en la lista derecha
        
#Se ordenan las listas
left_list.sort()
right_list.sort()

#Se genera una tercera lista con las distancias entre cada punto de la lista
distances = []

for left, right in zip(left_list, right_list):
    distances.append(abs(left - right))
    
#Se suman las distancias recogidas en la lista
print(sum(distances))

        