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

import math
from functools import cache #SACAMOS LA PUTA DEAGLE

blinks = 75

def main():
    
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        stone_list = list(map(int, puzzle_input.read().split(" ")))
        print(stone_list)
        
        stone_number = sum(blink(stone, blinks) for stone in stone_list)
        
        print(f'Se han contado {stone_number} piedras')
        
        
'''
Dos cositas
Lo que te piden no es la lista de piedras, sino el número de piedras que va a haber. Asi que lo que he hecho es una funcion 
recursiva que cuenta las piedras que van apareciendo y le suda la polla guardarlo en ningun sitio.
Muchas piedras siguen los mismos patrones, como los 0. Siempre se convierten en 1, el 1 se multiplica por 2024 y el 2024 se divide en 20 y 24
Con @cache, se guarda ese resultado en la RAM. Si se vuelve a encontrar una función que tenga que calcular 1 * 2024, en lugar de calcularlo, lo
recoge de la ram, reduciendo DRASTICAMENTE DE COJONES el consumo de recursos. Probablemente se podría haber hecho sin las funciones turboeficientes de abajo
'''
@cache
def blink(stone, blinks):
    if blinks == 0: #Se termina el bucle
        return 1 
    if stone == 0: #Se continua contando 
        return blink(1, blinks -1)
    digits = count_digits(stone)
    if digits % 2 == 0:
        #Reemplazar por dos piedras
        left, right = split_in_two(stone, digits)
        return blink(left, blinks - 1) + blink(right, blinks - 1)
    else:
        return blink(multiplicar_por_2024(stone), blinks - 1)



'''
Hoy vamos a amortizar la matricula de estructura de datos
Para hacer que la multiplicacion por 2024 sea mas rapida se va a realizar un desplazamiento de bits
Se desplaza a la izquierda 11 veces (* 2048)
Se resta un desplazamiento a la izquierda de 4 bits (* 16)
y se resta otro de 3 bits (* 8)
'''
def multiplicar_por_2024(number):
        return (number << 11) - (number << 4) - (number << 3)
    
    
'''
Segunda amortización de estructura de datos
En lugar de separar los numeros como si fuesen strings, se va a realizar una 
división modular, el cociente es la parte izquierda y el resto la derecha
Para calcular el numero de digitos, se hace algo parecido al calculo de digitos pares
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

    
    
main()
    
    