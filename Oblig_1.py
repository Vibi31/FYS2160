import matplotlib.pyplot as plt
import numpy as np

"""
file = open('termokopper.txt', 'r')
Lines = file.readlines()
"""

time = []
temp1 = []
temp2 = []

with open('termokopper.txt', 'r') as lines:
    for line in lines:
        row = line.split()              #split the line when it finds space
        time.append(row[0])
        temp1.append(row[1])
        temp2.append(row[2])

print(time)