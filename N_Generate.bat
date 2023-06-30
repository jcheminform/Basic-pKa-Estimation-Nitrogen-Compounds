@echo off
orca_2mkl Base -molden
Multiwfn Base.molden.input < scratch/comand_N.txt
setlocal enabledelayedexpansion

set N=N.inp
set N+1=N+1.inp
set N-1=N-1.inp

set /p num=Enter the number of processors: 

set count=0
for /f "tokens=* delims=" %%a in (%N%) do (
    set /a count+=1
    if !count! == 2 (
        echo %%pal nprocs !num! end%>>temp.txt
    )
    echo %%a>>temp.txt
)

del %N%
ren temp.txt %N%

set count=0
for /f "tokens=* delims=" %%a in (%N+1%) do (
    set /a count+=1
    if !count! == 2 (
        echo %%pal nprocs !num! end%>>temp.txt
    )
    echo %%a>>temp.txt
)

del %N+1%
ren temp.txt %N+1%

set count=0
for /f "tokens=* delims=" %%a in (%N-1%) do (
    set /a count+=1
    if !count! == 2 (
        echo %%pal nprocs !num! end%>>temp.txt
    )
    echo %%a>>temp.txt
)

del %N-1%
ren temp.txt %N-1%
