#from operator import truediv
"""graph analysis code used from statphys_python.pdf, histogram/frequency chart written by me"""

import matplotlib.pyplot as plt
import numpy as np
from ase.io import read


fil = 'dump.uke35'          #write file name inside paranthesis
traj = read(fil, format="lammps-dump-text", index=":")
n = len(traj)                   # Number of timesteps
print('number of timesteps = ', n)
nleft = np.zeros(n, dtype=np.int)

#choose what graphs i need:
graph = True #False
freq_histogram = True #False

# Find size of simulation box
firstframe = traj[0]
cellshape = firstframe.get_cell()
halfsize = cellshape[0][0]*0.5

# Count number of particles on left side for each timest
it = 0
for frame in traj:
    x = frame.get_positions()   # positions of atoms
    xi = x[:,0]                 # x-coordinates of atoms
    nleft[it] = np.sum(xi<halfsize)
    it = it + 1

if graph == True:

    #plotting graph
    plt.plot(nleft)
    plt.title('Atoms present on the left side of the box')
    plt.ylabel('Number of atoms/particles')
    plt.xlabel('Timestep')
    plt.show()

if freq_histogram == True:
    #determine number of bins needed for frequency-histogram plot
    rest = []
    for i in nleft:
        if i not in rest:
            rest.append(i)
    tot_bins = len(rest)

    #print number of times Nl has different values
    print('number of times Nl has different values: ', tot_bins)
    print('')
    #plotting the histogram
    plt.hist(nleft, bins = tot_bins)
    plt.style.use('ggplot')
    plt.xlabel('number of atom/particle on the left side')
    plt.ylabel('frequency')
    plt.title('histogram of atom/particle number frequency')
    plt.show()

    #normalising the curve, area = 1, trying to get a bell curve
    normalised = rest/(np.sum(rest))
    print(normalised)
    x_normal = np.linspace(0,np.max(rest), len(rest))
    plt.plot(x_normal, normalised)
    plt.show()

    
#np.savetxt('tmp.d', (t,Npart[0,:]))