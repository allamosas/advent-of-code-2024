# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:36:26 2024

@author: allam
"""

import re


def main():  
    button_a_list, button_b_list, prize_list = parse()  
    
    coins = 0
    for button_a, button_b, prize in zip(button_a_list, button_b_list, prize_list):
        coins += win_prizes(button_a, button_b, prize)
        
    print(f'El minimo número de monedas que hay que gastar es: {coins}')



def parse():

    button_a_list = []
    button_b_list = []
    prize_list = []    
    
    regex = r'.*: X[+,=](\d+), Y[+,=](\d+)'
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        for x, line in enumerate(puzzle_input):   
            
            if x%4 == 0:
                button_a_list.append([int(re.findall(regex, line)[0][0]),
                                      int(re.findall(regex, line)[0][1])])
            if x%4 == 1:
                button_b_list.append([int(re.findall(regex, line)[0][0]),
                                      int(re.findall(regex, line)[0][1])])
            if x%4 == 2:
                prize_list.append([int(re.findall(regex, line)[0][0]),
                                      int(re.findall(regex, line)[0][1])])
                
    return button_a_list, button_b_list, prize_list        
                
                
                
def win_prizes(button_a, button_b, prize):
    button_presses = 100
    cost_a = 3
    cost_b = 1
    coins = []
    
    for i in range(button_presses):
        for j in range(button_presses):
            x = i*button_a[0] + j*button_b[0]
            y = i*button_a[1] + j*button_b[1]
            if x == prize[0] and y == prize[1]:
                print(f'{button_a}, {button_b}, {prize}')
                print(f'{i}, {j}')
                coins.append(i*cost_a + j*cost_b)
                
    if coins:
        return min(coins)
    
    return 0



main()

42*10+40*44
18*10+78*44