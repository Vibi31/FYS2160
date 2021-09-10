import lammps_logfile 
import matplotlib.pyplot as plt

log = lammps_logfile.File('log.lammps')


x = log.get("Time")
y = log.get("Temp")

plt.plot(x, y)
plt.show()


