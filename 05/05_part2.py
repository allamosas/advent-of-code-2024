# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 06:54:30 2024

@author: allam
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 05:53:28 2024

@author: allam
"""

is_ordering_rule=True
ordering_rules = []
update_numbers = []
incorrect_updates = []



def check_updates(update_numbers):
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
                #print("existe una mejor manera de hacer esto pero fijo")
                print(end="")
        
        if is_valid_update:
            valid_updates.append(update)
        else:
            incorrect_updates.append(update)
            
    return valid_updates, incorrect_updates


def correct_updates(incorrect_updates):
    updated_updates = []
    
    for update in incorrect_updates:  #Por cada update
        print(update)
        repeat = True
        
        while repeat:   #Se repite la comprobación hasta que sea correcto para todas las reglas            
            for rule in ordering_rules: #Por cada regla
                try:
                    left = update.index(rule[0]) #Se busca la parte izquierda
                    right = update.index(rule[1]) #Se busca la parte derecha
                    if left > right:
                        update[left],update[right] = update[right],update[left]
                        repeat = True
                        break
                except:
                    print(end="")
                repeat = False
            
        updated_updates.append(update)    
        
    return updated_updates
            

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


valid_updates, incorrect_updates = check_updates(update_numbers)
correct_incorrect_updates_xd = correct_updates(incorrect_updates)
middle_values = get_middle_value(correct_incorrect_updates_xd)
print(sum(middle_values))