# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 06:37:20 2024

@author: allam
"""

def is_safe(report):
    ordered = False
    safe_leaps = False    
    
    increasing = all(report[level] < report[level+1] for level in range(len(report) -1)) #Se comprueba que todos los elementos son mayores que el anterior
    decreasing = all(report[level] > report[level+1] for level in range(len(report) -1)) #Se comprueba que todos los elementos son menores que el anterior
    
    if increasing or decreasing: #Se anota si esta ordenado
        ordered = True
        
    highest_leap = max(abs(report[level] - report[level+1]) for level in range(len(report) -1)) #Se calcula la mayor distancia entre elementos contiguos del informe
    
    if highest_leap <=3: #Se anota si esta distancia máxima es igual o menor que 3
        safe_leaps = True
    
    if ordered and safe_leaps: #Si todo es correcto, se da el visto bueno al reporte
        return True
    else:
        return False
    
reports = []


#Se recogen los valores del input en una lista y se introduce cada lista en una lista anidada
with open('input', 'r', encoding='utf-8') as puzzle_input:
    for line in puzzle_input:
        report = [int(level) for level in line.split(' ')] # Se formatea cada string de la linea en un int
        reports.append(report)
        
#Se analizan las líneas del informe y se cuentan los favorables
report_count = 0
for report in reports:
    if is_safe(report):
        report_count += 1
        
print(report_count)
        
        