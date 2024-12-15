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
                
                
                
def win_prizes(button_a, button_b, prize):
    cost_a = 3
    cost_b = 1
    
    A = [[button_a[0],button_b[0]],
         [button_a[1],button_b[1]]]
    
    r = cramer(A, prize)
    
    if not r:
        return 0
    
    coins = r[0]*cost_a + r[1]*cost_b  
    return coins


def cramer(A, res):
    #Determinante de la matriz A
    det_A = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if det_A == 0:
        print("El determinante es 0")
        return []

    #Determinantes de las soluciones
    det_A_x = res[0] * A[1][1] - res[1] * A[0][1]
    det_A_y = A[0][0] * res[1] - A[1][0] * res[0]
    
    #Se comprueba si las soluciones son enteras
    if det_A_x % det_A == 0 and det_A_y % det_A == 0:
        x = det_A_x // det_A
        y = det_A_y // det_A

        #Si ambas soluciones son positivas, se devuelven
        if x > 0 and y > 0:
            return [x, y]
          
    #print("No se han encontrado soluciones enteras positivas.")
    return []



def parse():

    button_a_list = []
    button_b_list = []
    prize_list = []    
    tocate_los_cojones = 10000000000000
    
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
                prize_list.append([int(re.findall(regex, line)[0][0]) + tocate_los_cojones,
                                   int(re.findall(regex, line)[0][1]) + tocate_los_cojones])
                
    return button_a_list, button_b_list, prize_list 

main()