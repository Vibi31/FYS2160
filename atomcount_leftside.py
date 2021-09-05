import matplotlib.pyplot as plt
import numpy as np
from ase.io import read

traj = read("twosec02.lammpstrj", format="lammps-dump-text", index=":")
n = len(traj) # Number of timesteps
nleft = np.zeros(n)

# Find size of simulation box
firstframe = traj[0]
cellshape = firstframe.get_cell()
halfsize = cellshape[0][0]*0.5

# Count number of particles on left side for each timest
it = 0
for frame in traj:
x = frame.get_positions() # positions of atoms
xi = x[:,0] # x-coordinates of atoms
nleft[it] = np.sum(xi<halfsize)
it = it + 1
plt.plot(nleft)
#end1
np.savetxt(’tmp.d’, (t,Npart[0,:]