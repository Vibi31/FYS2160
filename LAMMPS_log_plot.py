import matplotlib.pyplot as plt
import dump from 
from numpy import *
"""
majority of the code is from statistical physics python-book

"""
data = dmp('dump.lammpstrj')       #timestep data

t = data.time()                     #time steps
nt = size(t)
print('number of timesteps:', nt)   #just wanted to see

n_particles = zeros(n,float)        #number of atoms

tmp_time,box,atoms,bonds,tris,lines = data.viz(0)
halfsize = 0.5*box[3] # Box size in x-di


for i in range(nt):
    xit = array(data.vecs(i,"x"))
    nleft[i] = size(find(xit<halfsize))

plt.plot(t,n_particles)
plt.xlabel('t')
plt.ylabel('N_p')
plt.show() 
