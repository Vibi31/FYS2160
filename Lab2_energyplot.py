import matplotlib.pyplot as plt
import numpy as np
import lammps_logfile

#henter fram verdier fra log-fil
#fra solid
log_251data = lammps_logfile.File("251K_log.lammps")
Steps251 = log_251data.get("Step")
Energy251 = log_251data.get("TotEng")
Enthalpy251 = log_251data.get("Enthalpy")

#fra 
log_300data = lammps_logfile.File("300K_log.lammps")
Steps300 = log_300data.get("Step")
Energy300 = log_300data.get("TotEng")
Enthalpy300 = log_300data.get("Enthalpy")

#gas fase
log400data = lammps_logfile.File("log400k.lammps")
Steps400 = log400data.get("Step")
Energy400 = log400data.get("TotEng")
Enthalpy400 = log400data.get("Enthalpy")


#plotter
plt.plot(Steps251, Energy251)
plt.title('Total energy mot Tidssteg [fra 251K]')
plt.xlabel('Timestep')
plt.ylabel('Energy av system')
plt.show()

plt.plot(Steps300, Energy300)
plt.title('Total energy mot Tidssteg [fra 300K]')
plt.xlabel('Timestep')
plt.ylabel('Energy av system ')
plt.show()

plt.plot(Steps400, Energy400)
plt.title('Total energy mot Tidssteg [fra 400K]')
plt.xlabel('Timestep')
plt.ylabel('Energy av system')
plt.show()

#plotter enthalpy
plt.plot(Steps251, Enthalpy251)
plt.title('Enthalpy mot Tidssteg [fra 251K]')
plt.xlabel('Timestep')
plt.ylabel('Enthalpy av system')
plt.show()

plt.plot(Steps300, Enthalpy300)
plt.title('Enthalpy mot Tidssteg [fra 300K]')
plt.xlabel('Timestep')
plt.ylabel('Enthalpy av system')
plt.show()

plt.plot(Steps400, Enthalpy400)
plt.title('Enthalpy mot Tidssteg [fra 400K]')
plt.xlabel('Timestep')
plt.ylabel('Enthalpy av system ')
plt.show()
