import matplotlib.pyplot as plt
from pylab import *

data = dump("dump.lammpstrj")       #timestep data

t = data.time()                     #time steps
nt = size(t)
print('number of timesteps:', nt)   #just wanted to see

n_particles = zeros(n,float)        #number of atoms

