#!/bin/bash
#
# Parallel script produced by bolt
#        Resource: ARCHER2 (HPE Cray EX (128-core per node))
#    Batch system: Slurm
#
# bolt is written by EPCC (http://www.epcc.ed.ac.uk)
#
#SBATCH --job-name=QE_SCF_conv
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --exclusive
#SBATCH --time=10:00:00

#SBATCH --account=dc158
#SBATCH --partition=standard
#SBATCH --qos=standard

#module load epcc-job-env
#export OMP_NUM_THREADS=1

module load mpt
module load quantum-espresso

# SCF convergence calculation
for ecut in 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 
do
  	sed "s/    ecutwfc = 80.0,/    ecutwfc = $ecut,/" h3s.scf-dos.in > h3s.scf-dos-temp.in
	srun -n 6 pw.x -npool 6 -pd .true. -in h3s.scf-dos-temp.in > h3s.scf-dos.out
	e=$(grep "!    total energy" h3s.scf-dos.out | sed 's/[^0-9.-]*//g')
	echo "$ecut" "$e" 
done

