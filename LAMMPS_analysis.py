
import lammps_logfile
log = lammps_logfile.File(\"./log.lammps\")
t = log.get(\"Time\")
