# Prediction-of-basic-pKa-values-in-nitrogen-compounds
These instructions are intended for Windows users who are unfamiliar with computational calculations and data processing. Linux-only users and experts in the field of computational chemistry will have no difficulty performing pKa calculations using ORCA and Multiwfn to obtain the necessary properties and solve the equation pKa = 0.1074ΔE – 0.1422ΔHLGap – 0.9132χM + 0.0151%NPSA – 1.4887ΔALIEN + 3.0608BaseT – 30.7139, as described in the article (#).

To begin, download and decompress all the required files to a preferred location, which will be referred to as the "main folder." Instructions on how to install the necessary programs, such as ORCA, Multiwfn, and Python, are included in the files. You will also need a molecular structure creator and editor, as outlined in the "Molecular visualization software" document.

Once you have installed the programs, follow the steps below:

1) Draw the structure of the base and conjugate acid of interest and save it in xyz format. Ensure that the saved structure meets two conditions: a) the base must have a net charge of zero, and the conjugate acid must have a net charge of +1. If necessary, add Cl- or Na+ ions to meet this condition, and b) the target nitrogen atom (protonated and non-protonated) must be the first atom enumerated, so it should be located at the beginning of the coordinate matrix of the xyz file. You can use any text reader to edit the xyz file.

2) Name the xyz files as follows: "Base.xyz" for the non-protonated compound and "Conjugate_acid.xyz" for the protonated compound, including capital letters.

3) Replace the old inputs with the new files in the "main folder".

4) Double-click on the RUN.bat file, and the associated pKa value will be displayed once the calculations are complete.

Note that if the structures are too large, the calculation may take longer than desired on a regular computer. In this case, it is recommended to obtain optimized structures using the ORCA program on Linux on a high-performance computer. The inputs in .inp format are provided in the "main folder." Once you obtain the optimized structures, copy the out and gbw files to the "main folder" and run the RUN2.bat file (not RUN.bat) to get the pKa value.

If the pKa calculation still takes longer than desired, the required single points can be calculated using the ORCA program on Linux on a high-performance computer. To do this, run the N_generate.bat file to generate the inputs N.inp, N+1.inp, and N-1.inp. The corresponding outputs should eventually be copied to the "main folder" to obtain the pKa value by running the RUN3.bat file.
