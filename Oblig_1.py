import matplotlib.pyplot as plt
import numpy as np

"""
file = open('termokopper.txt', 'r')
Lines = file.readlines()
"""

time = []
temp1 = []      #Tw temperature of water inside 
temp2 = []      #Tw temperature of water inside Temperfect mug

Ta = 22         # ambient temperature

with open('termokopper.txt', 'r') as lines:
    for line in lines:
        row = line.split()              #split the line when it finds space
        time.append(float(row[0]))
        temp1.append(float(row[1]))
        temp2.append(float(row[2]))
#lines.close()

#print(len(time), len(temp1), len(temp2))
#t = np.linspace(0,len(time), len(time))

t = np.array(time)       
t1 = np.array(temp1)
t2 = np.array(temp2)


plt.title('Temperature change of water over time')
plt.xlabel('time (seconds)')
plt.ylabel('temperature (celsius)')
plt.plot(np.array(time), np.array(temp1), label="temp1")
plt.plot(time, np.array(temp2), label="temperfect mug")
plt.legend()
plt.show()
