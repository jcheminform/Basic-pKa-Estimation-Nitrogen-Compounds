move Base.out scratch\
move Conjugate_acid.out scratch\
move N.out scratch/
move N+1.out scratch/
move N-1.out scratch/
orca_2mkl Base -molden
Multiwfn Base.molden.input < scratch/A.txt > scratch/ALIE1.out
Multiwfn Base.molden.input < scratch/S.txt > scratch/S.out
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
