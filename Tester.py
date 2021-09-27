
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

#converting our list to arrays
t = np.array(time)       
t1 = np.array(temp1)
t2 = np.array(temp2)

tau = 5180       #Bodus mug
tau_t = 5598     #Temperfect mug

print(tau)
exp_f = (np.max(t1)-Ta)*(exp(-t/tau)) + Ta

print('max temp of Bodus mug:',np.max(t1))
print('max temp of Temperfect mug:',np.max(t2))


#calculating heat capacity of water:
Tm = 64                 #melting temperature in celsius 
m = 300                 # grams/millilitres
cvw = 4.18              #units= [joules/gram]specific heat capacity
C_vw = m * cvw          #assume constant at all temperatures

#calculating heat capacity of phase change material
C_vc = np.zeros(len(t))     
i = 0
temp_100 = np.linspace(0,100, len(C_vc))
for temp in temp_100:
    if temp > Tm:
        C_vc[i] = 4*C_vw
    else:
        C_vc[i] = 0.1*C_vw
    i += 1 

#calculating temperature change 

temp_100 = np.linspace(0,100, len(C_vc))
dT = np.linspace(len(temp_100))
for i in range(len(temp_100)):
    dT = temp_100[i]

# plotting Latent heat storage
plt.title('Latent heat storage')
plt.xlabel('C_vc')
plt.ylabel('Temperature [C]')
plt.plot(C_vc, temp_100, label="temp1")
plt.show()



