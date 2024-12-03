# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:00:47 2024

@author: allam
"""

import re

#Se recogen los valores del input en una lista y se introduce cada lista en una lista anidada
with open('input', 'r', encoding='utf-8') as puzzle_input:
    memory_readings = puzzle_input.read()

#Regex para detectar 'mul()', 'do()' y "don't'"
regex_sanitize = r"(do\(\)|mul\(\d+,\d+\)|don't\(\))"

#Se buscan todas las coincidencias y se almacenan en match en lugar de findall
#para poder procesarlo mejor
matches = [match.group() for match in re.finditer(regex_sanitize, memory_readings)]

valid = []
do_flag = True #Se crea un flag para ver si se multiplica el elemento encontrado
#Por defecto es True ya que se especifica que se realiza la primera multiplicacion
#aunque no tenga un do

#Se procesan las combinaciones válidas que no tengan un don't entremedias
for i, current in enumerate(matches):
    print(current)
    if current == 'do()': #Se encuentra un do()
        do_flag = True
        
    elif current == "don't()": #Se encuentra un dont()
        do_flag = False
        print('False')
        
    else: #Se ha encontrado un mul
        if do_flag: #Si hay luz verde, se marca como valido
            valid.append(current)            
            
#Ya que estamos, regex para limpiar la parte izquierda y derecha del input y 
#dejarlas separadas por una coma para realizar el split
regex_split = r'\d{1,3},\d{1,3}'

numbers = []
for mul in valid:
    new_row = []    #Se crea una nueva fila y se añaden los dos numeros parseados a int
    pair = re.findall(regex_split, mul)                        # "abc,xyz"       
    numbers.append([int(num) for num in pair[0].split(",")])   # [abc][xyz] #Se añade a numbers

#Se multiplican los valores y se suman
sum = 0
for number in numbers:
    sum = sum + (number[0] * number[1])
    
print(sum)