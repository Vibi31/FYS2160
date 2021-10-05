import matplotlib.pyplot as plt
import numpy as np
from numpy import exp


T = np.linspace(1, 1000, 1000) #10,000 data points
delta_e = 1.602176565e-19 #[1eV]
Kb = 1.38064852e-23 #boltzmann constant
N = 100 
n = N/(exp(delta_e/(T*Kb))+1) #vacancies 

plt.title('vacancies as a function of temperature [K]')
plt.ylabel('Temperature [K]')
plt.xlabel('Vacancies [n]')
plt.plot(n,T)
plt.show()