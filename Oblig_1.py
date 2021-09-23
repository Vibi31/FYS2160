import matplotlib.pyplot as plt
import numpy as np
from numpy import exp 

"""
file = open('termokopper.txt', 'r')
Lines = file.readlines()
"""

time = []
temp1 = []      #Tw temperature of water inside Bodum thermos mug
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

#converting our list to arrays
t = np.array(time)       
t1 = np.array(temp1)
t2 = np.array(temp2)

tau =  3773
#tau = 6700 #guess
exp_f =   np.max(t1)*exp(-t/tau)

print('max temp of Bodus mug:',np.max(t1))
print('max temp of Temperfect mug:',np.max(t2))

# plotting the two mugs against eachother 
plt.title('Temperature change of water over time')
plt.xlabel('time (seconds)')
plt.ylabel('temperature (celsius)')
plt.plot(t, t1, label="temp1")
plt.plot(t, t2, label="temperfect mug")
plt.plot(t, exp_f, label="exponential approx.")

plt.legend()
plt.show()
