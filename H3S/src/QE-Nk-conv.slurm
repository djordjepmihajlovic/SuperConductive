#!/bin/bash
#
# Parallel script produced by bolt
#        Resource: ARCHER2 (HPE Cray EX (128-core per node))
#    Batch system: Slurm
#
# bolt is written by EPCC (http://www.epcc.ed.ac.uk)
#
#SBATCH --job-name=QE_k_conv
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

# k-point grid size convergence calculation
for k in 3 6 9 12 15 18 21 24 27 30 33
do
  	sed "s/3 3 3 0 0 0/$k $k $k 0 0 0/" h3s.scf-dos.in > h3s.scf-dos-temp.in
	srun -n 6 pw.x -npool 6 -pd .true. -in h3s.scf-dos-temp.in > h3s.scf-dos.out
	# Post-processing
	sed "s/  fildos  = 'h3s_dos_tetra.dat'/  fildos  = 'h3s_dos_tetra_$k.dat'/" h3s.pp_dos.in > h3s.pp_dos_temp.in
	srun dos.x -pd .true. -in h3s.pp_dos_temp.in > h3s.pp_dos.out
done

