# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 06:42:48 2024

@author: allam
"""
import re
import math

width = 101
height = 103
seconds = 100

bot_list = []


def main():    
    regex_pos = r'p=(\d+),(\d+)'
    regex_vel = r'v=(-?\d+),(-?\d+)'
    with open('input.txt', 'r', encoding='utf-8') as puzzle_input:
        for line in puzzle_input:
            pos = [int(re.findall(regex_pos, line)[0][0]),
                   int(re.findall(regex_pos, line)[0][1])]
            
            vel = [int(re.findall(regex_vel, line)[0][0]),
                   int(re.findall(regex_vel, line)[0][1])]
            bot_list.append([pos, vel])
            
            
    grid = predict_positions(bot_list)    
    bot_number = count_bots(grid)    
    safety_factor = 1
    for q, number in enumerate(bot_number):
        print(f'Hay {number} bots en el cuadrante Q{q+1}')
        safety_factor *= number
        
    print(f'El factor de seguridad es {safety_factor}')
    
def predict_positions(bot_list):
    global height
    global width
    global seconds
    
    grid = [[ 0 for _ in range(width)] for _ in range(height)]
    
    for bot in bot_list:
        pos_x, pos_y = bot[0][0], bot[0][1]        
        pos_x = (pos_x + bot[1][0]*seconds) % width
        pos_y = (pos_y + bot[1][1]*seconds) % height
        
        grid = write_pos(pos_x, pos_y, grid)
   
    return grid
    
    
def write_pos(pos_x, pos_y, grid):
    grid[pos_y][pos_x] += 1        
    return grid    


def count_bots(grid):
    global height
    global width
    print(grid)
    
    bot_number = [0, 0, 0, 0]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row): #Esto oficialmente cuenta como ñapa
            if x < math.floor(width / 2) and y < math.floor(height / 2): #Q1
                bot_number[0] += cell
            if x > math.floor(width / 2) and y < math.floor(height / 2): #Q2
                bot_number[1] += cell
            if x < math.floor(width / 2) and y > math.floor(height / 2): #Q3
                bot_number[2] += cell
            if x > math.floor(width / 2) and y > math.floor(height / 2): #Q4
                bot_number[3] += cell
                
    return bot_number
    

main()
            
    
    