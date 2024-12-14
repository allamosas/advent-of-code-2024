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
brute_force = 2

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
            
            
    grid, seconds = find_the_fucking_tree(bot_list)    
    print(f'Posiblemente hay un arbol de navidad. Han pasado {seconds-1} segundos')
    
def find_the_fucking_tree(bot_list):
    global height
    global width
        
    grid = [[ 0 for _ in range(width)] for _ in range(height)]
    
    seconds = 0
    while not has_tree(grid, ):
        grid = [[ 0 for _ in range(width)] for _ in range(height)]
        for bot in bot_list:
            pos_x, pos_y = bot[0][0], bot[0][1]        
            pos_x = (pos_x + bot[1][0]*seconds) % width
            pos_y = (pos_y + bot[1][1]*seconds) % height
            grid = write_pos(pos_x, pos_y, grid)
        print(f"\rSe han comprobado los primeros {seconds}s{' ' * 20}", end='', flush=True)
        seconds += 1

    
    return grid, seconds
    
    
def write_pos(pos_x, pos_y, grid):
    grid[pos_y][pos_x] += 1        
    return grid    


def has_tree(grid):
    printed_pos = print_grid(grid)
    if any('##############################' in line for line in printed_pos):
        print('\n Encontrado!!!')
        return True
    return False
    

def count_bots(grid):
    global height
    global width
    
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

def print_grid(grid):
    file_grid = []
    for row in grid:
        line = ''
        for cell in row:
            if cell == 0:
                line += ' '
            else:
                line += '#'
        line += '\n'
        file_grid.append(line)
    return file_grid

main()
            
    
    