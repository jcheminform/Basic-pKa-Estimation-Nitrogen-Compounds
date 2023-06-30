@echo off
echo Starting pKa value calculation...
orca Base.inp > scratch/Base.out
orca Conjugate_acid.inp > scratch/Conjugate_acid.out
del /s /q *.densities
del /s /q *.engrad
del /s /q *.opt
del /s /q Base_trj.xyz
del /s /q Conjugate_acid_trj.xyz
del /s /q Base_property.txt
del /s /q Conjugate_acid_property.txt
orca_2mkl Base -molden
Multiwfn Base.molden.input < scratch/A.txt > scratch/ALIE1.out
Multiwfn Base.molden.input < scratch/S.txt > scratch/S.out
Multiwfn Base.molden.input < scratch/comand_N.txt
orca N.inp > scratch/N.out
orca N+1.inp > scratch/N+1.out
orca N-1.inp > scratch/N-1.out
del /s /q N.inp
del /s /q N+1.inp
del /s /q N-1.inp
del /s /q N.wfn
del /s /q N+1.wfn
del /s /q N-1.wfn
del /s /q N.densities
del /s /q N+1.densities
del /s /q N-1.densities
del /s /q N.wfx
del /s /q N+1.wfx
del /s /q N-1.wfx
del /s /q N.gbw
del /s /q N+1.gbw
del /s /q N-1.gbw
del /s /q N.ges
del /s /q N+1.ges
del /s /q N-1.ges
del /s /q N_property.*
del /s /q N+1_property.*
del /s /q N-1_property.*
orca_2mkl Conjugate_acid -molden
Multiwfn Conjugate_acid.molden.input < scratch/A.txt > scratch/ALIE2.out
del /s /q *.molden.input
cd scratch/
pKa.py
pause
del /s /q ALIE1.out
del /s /q ALIE2.out
del /s /q N.out
del /s /q N+1.out
del /s /q N-1.out
del /s /q S.out