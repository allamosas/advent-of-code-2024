# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 06:00:32 2024

@author: allam
"""
from itertools import product

result_list = []
factor_list = []

#probe a usar diccionarios ayer y ya se van a quedar pal resto
#que maravilla
operation = {
    '+': lambda x, y: x + y, 
    '*': lambda x, y: x * y
    }

def main(): 
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        for line in puzzle_input:
            equation = line.split(':')
            result_list.append(int(equation[0])) #Se pasa a int la parte izquierda
            factor_list.append(list(map(int, equation[1].strip().split(" ")))) #Se pasan a int los factores de la derecha
            
    sum = 0
    progress = 0 #progreso para ver cuanto tiempo tengo para cagar
    for result, factors in zip(result_list, factor_list):  #Por cada resultado se mira si tiene solucion con esos factores
        progress += 1
        print(f'{(progress / len(result_list)) * 100}%')
        if has_solution(result, factors):
            sum += result
            
    print(f'La suma final de los valores de test es {sum}')
    
    
def has_solution(result, factors):
    """
    A ver esto es una paja mental. Lo que he supuesto que se puede hacer es construir una especie de "directrices de operacion"
    Esta movida lo que hace es una lista del tamaño del numero de factores en un numero de combinaciones del numero de operaciones,
    mas que nada porque si luego hay que dividir tambien, por ejemplo, se añade la division a operadores y esto sigue funcionando.
    Lo que hace es devolver una lista de valores en un sistema binario en este caso en el que los 0 son sumas y los 1 multiplicaciones
    De este modo, luego lo unico que hay que hacer es la operacion que diga el numero. A ver que tal rula
    """
    combination_list = list(product(range(len(operation)), repeat = len(factors))) #Se crea la lista con todas las posibles operaciones
    for combination in combination_list: #Por cada combinacion de la lista
    
        solution = factors[0] #Se inicializa con el primer factor para evitar multiplicarlo por 0
        for operator_index, factor in zip(combination, factors[1:]): #Se calculan las operaciones a partir del primer elemento que ya esta inicializado
            operator = list(operation.keys())[operator_index]  #Se convierte el índice a operador ('+', '*')
            solution = operation[operator](solution, factor) #Se realiza la operacion
            if result == solution: #Se comprueba si es valida
                print("Se ha encontrado una solución")
                return True
    #Si llega hasta aqui es que no ha encontrado soluciones
    return False
            

main()