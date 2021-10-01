
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, log

K = 1.38064852e-23 #Boltzmann constant
N = 500
q = np.linspace(1,250,251)
Kelvin = np.linspace(25, 500, 251)

Multiplicity = (((q+N)/q)**q) * (((q+N)/N)**N) 
entropy = K*(q+N)*log(q+N) - K*q*log(q) - K*N*log(N) 

def Temp(q, K):
    T = np.gradient(entropy,q)**(-1) #dU/dS
    return T


plt.title('Multiplicity as a function of q')
plt.xlabel('q')
plt.ylabel('Multiplicity')
plt.plot(q, Multiplicity)
plt.show()

plt.title('Entropy as a function of q')
plt.ylabel('Entropy [J/K]')
plt.xlabel('q')
plt.plot(q, entropy)
plt.show()

"""
T = temp(200,)
plt.title('Temperature curve')
plt.ylabel('Temperature [K]')
plt.xlabel('q')
plt.plot(q, T)
plt.show()
"""

def Cv(T, N):
    K = 1.38064852e-23
    epsilon = 1         #to keep things simple
    return (N*epsilon**2*exp(-epsilon/(K*T)))/((K*T**2)*(1-exp(-epsilon/(K*T))))

T = np.linspace(0,300, 301)
heat_cap = Cv(T, 250)

plt.title('Heat capacity curve')
plt.xlabel('Temperature [K]')
plt.ylabel('Heat capacity Cv')
plt.plot(T, heat_cap)
plt.show()

