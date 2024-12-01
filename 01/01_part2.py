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

#Se buscan las veces que se repiten los números de la izquierda en la lista de la derecha y se multiplican los valores de la lista de la izquierda por el número de iteraciones
similarities = []       
for item in left_list:
    similarities.append(item*right_list.count(item))
    
#Se suman los valores de las iteraciones
print(sum(similarities))
        