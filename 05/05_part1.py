# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:53:28 2024

@author: allam
"""

is_ordering_rule=True
ordering_rules = []
update_numbers = []


def check_valid_updates(update_numbers):
    valid_updates = []
    for update in update_numbers: #Se comprueba por cada update si cumple todas las reglas    
        is_valid_update = True
        
        for rule in ordering_rules:
            try:
                left = update.index(rule[0]) #Se busca la parte izquierda
                right = update.index(rule[1]) #Se busca la parte derecha
                if left > right:
                    is_valid_update = False
                    break
            except:
                print("existe una mejor manera de hacer esto pero fijo")
        
        if is_valid_update:
            valid_updates.append(update)
            
    return valid_updates
            

def get_middle_value(valid_updates):
    middle_values = []
    for update in valid_updates:
        middle_index = len(update) // 2
        middle_values.append(update[middle_index])
        
    return middle_values


with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        
        if line == '':
            is_ordering_rule = False
        else:   
            if is_ordering_rule:
                ordering_rules.append(list(map(int, line.split("|"))))  
            else:
                update_numbers.append(list(map(int, line.split(","))))  

valid_updates = check_valid_updates(update_numbers)
middle_values = get_middle_value(valid_updates)
print(sum(middle_values))