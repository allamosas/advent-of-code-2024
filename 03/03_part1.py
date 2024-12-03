# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:00:47 2024

@author: allam
"""

import re

#Se recogen los valores del input en una lista y se introduce cada lista en una lista anidada
with open('input', 'r', encoding='utf-8') as puzzle_input:
    memory_readings = puzzle_input.read()
    
#Regex para detectar 'mul(' + numero de 1 a 3 cifras + ',' + numero de 1 a 3 cifras + ')'
regex_sanitize = r'mul\(\d{1,3},\d{1,3}\)'

#Se buscan todas las coincidencias y se almacenan en muls
muls = re.findall(regex_sanitize, memory_readings)

#Ya que estamos, regex para limpiar la parte izquierda y derecha del input y 
#dejarlas separadas por una coma para realizar el split
regex_split = r'\d{1,3},\d{1,3}'

#Se recorren todas las coincidencias y se pasan a una lista de enteros
numbers = []
for mul in muls:
    new_row = []    #Se crea una nueva fila y se añaden los dos numeros parseados a int
    pair = re.findall(regex_split, mul)                        # "abc,xyz"       
    numbers.append([int(num) for num in pair[0].split(",")])   # [abc][xyz] #Se añade a numbers

#Se multiplican los valores y se suman
sum = 0
for number in numbers:
    sum = sum + (number[0] * number[1])
    
print(sum)