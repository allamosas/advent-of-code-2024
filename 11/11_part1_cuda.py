# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 06:09:00 2024

@author: allam
   ___  _____  _____  ____   __  ____    ___  ____     __  __ __ 
  /  _]|     ||     ||    | /  ]|    |  /  _]|    \   /  ]|  |  |
 /  [_ |   __||   __| |  | /  /  |  |  /  [_ |  _  | /  / |  |  |
|    _]|  |_  |  |_   |  |/  /   |  | |    _]|  |  |/  /  |  ~  |
|   [_ |   _] |   _]  |  /   \_  |  | |   [_ |  |  /   \_ |___, |
|     ||  |   |  |    |  \     | |  | |     ||  |  \     ||     |
|_____||__|   |__|   |____\____||____||_____||__|__|\____||____/ 
                                                                
  ____   ___     ___  _____     ____   ____   ____   ____   ____   ____   ____   ____   ____  
 /    | /   \   /  _]/ ___/    |    \ |    \ |    \ |    \ |    \ |    \ |    \ |    \ |    \ 
|   __||     | /  [_(   \_     |  o  )|  D  )|  D  )|  D  )|  D  )|  D  )|  D  )|  D  )|  D  )
|  |  ||  O  ||    _]\__  |    |     ||    / |    / |    / |    / |    / |    / |    / |    / 
|  |_ ||     ||   [_ /  \ |    |  O  ||    \ |    \ |    \ |    \ |    \ |    \ |    \ |    \ 
|     ||     ||     |\    |    |     ||  .  \|  .  \|  .  \|  .  \|  .  \|  .  \|  .  \|  .  \
|___,_| \___/ |_____| \___|    |_____||__|\_||__|\_||__|\_||__|\_||__|\_||__|\_||__|\_||__|\_|
"""

import time
import math
import cupy as cp

blinks = 75
cp.set_printoptions(linewidth=200)

def main():
    
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        stone_list = cp.array(puzzle_input.read().split(" "), dtype=cp.int64)
        print(stone_list)
        
        inicio_bucle = time.time()
        last = 0
        for i in range(blinks):
            inicio = time.time()
            stone_list = blink(stone_list)
            fin = time.time()
            print(f'He pestañeado {i+1} veces y hay {len(stone_list)} piedras ({len(stone_list) - last} más)')
            last = len(stone_list)
            print(f'Se ha tardado {round(fin - inicio, 3)}s ')
            #print(stone_list)
        fin_bucle = time.time()
        print(f'Han aparecido {len(stone_list)} piedras en un total de {round(fin_bucle - inicio_bucle, 3)}s!')
        
        
def blink(stone_list):
    i = 0
    while i < len(stone_list): #Se utiliza un while porque se va a avanzar el iterador a mano
        stone = stone_list[i]
        
        if stone == 0:
            stone_list[i] = 1
        else:
            digits = count_digits(stone)
            if digits % 2 == 0:
                #Reemplazar por dos piedras
                left, right = split_in_two(stone, digits)
                stone_list[i] = left #Se actualiza la piedra izquierda
                i += 1 #Se avanza manualmente el puntero a la derecha para no sobreescribir el nuevo item
                stone_list = cp.concatenate( #Se añade el termino derecho al lado sin variar el resto de la lista
                    [stone_list[:i], 
                     cp.array([right]), 
                     stone_list[i:]]) 
                
            else:
                stone_list[i] = multiplicar_por_2024(stone)
        i += 1
    return stone_list

'''
Segunda amortización de estructura de datos
En lugar de separar los numeros como si fuesen strings, se va a realizar una 
división modular, el cociente es la parte izquierda y el resto la derecha
Para calcular el numero de digitos, se hace algo parecido al calculo de digitos pares
Igual hay que remodelar esa operacion para que se realice una única vez
'''    
def split_in_two(stone, digits):
    power = 10 ** (digits // 2)
    leftie, rightie = divmod(stone, power)
    return int(leftie), int(rightie)


'''
En el reddit del dia 7 publicaron una función para contar digitos con logaritmos
que me pareció interesante
'''
def count_digits(number):
    return math.floor(math.log(number, 10)) + 1 if number > 0 else 1


'''
Hoy vamos a amortizar la matricula de estructura de datos
Para hacer que la multiplicacion por 2024 sea mas rapida se va a realizar un desplazamiento de bits
Se desplaza a la izquierda 11 veces (* 2048)
Se resta un desplazamiento a la izquierda de 4 bits (* 16)
y se resta otro de 3 bits (* 8)
'''
def multiplicar_por_2024(number):
        return (number << 11) - (number << 4) - (number << 3)

    
    
main()
    
    