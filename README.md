# Turing_pattern_analysis

======================================================================================================================================================================================
Context: Wertheim, Kenneth Yann (2017). Mathematical Modelling of Lymphangiogenesis. University of Southampton, Doctoral Thesis, 234pp.
About: This repository contains the python programs used for Turing pattern analysis in chapter 6 of the above thesis, their outputs, as well as the plot data in chapter 6 and the COMSOL files used to generate them.

Python programs: They are all carefully documented.

Plot data: The csv file names match their labels in the thesis.

COMSOL version: All the COMSOL files were built in COMSOL Multiphysics version 5.2.
Hardware: The simulations were run on a desktop computer with an Intel(R) Core(TM) i5-3570 CPU at 3.40 GHz and 16 GB of RAM.
Units: All the simulation results are dimensionless.

Nomenclature for the COMSOL implementations:
-c1 is the concentration of MMP2.
-c2 is the concentration of VEGFC.
-c3 is the concentration of collagen I.
-c4 is the concentration of VEGFC-collagen I.

======================================================================================================================================================================================
Python programs

1. BU1.Turing_space.py explores the parametric space of the secondary system, leading to a sample of Turing points.
-The output is turing1_band.txt.
-In turing1_band.txt, there is a collection of lists. Each list has the format [b1, b2, b3, b4, b5, a1m2, a1vc, a2m2, a2vc, a3, a4, [dispersion relation]].
-[dispersion relation] is a sublist with 88 entries. They are the maximum eigenvalues' real parts at the first 88 wavenumbers, including 0.

2. BU2.Parametric_distributions.py takes turing1_band.txt as its input and generates figure 6.1.

3. BU3.Ranking.py takes turing1_band.txt as its input and finds the 10 Turing points closest to the reference point in the parametric space.
-The output is band10.txt.
-In band10.txt, there are 10 lists. Each has the format [b1, b2, b3, b4, b5, a1m2, a1vc, a2m2, a2vc, a3, a4, [dispersion relation]].
-[dispersion relation] is a sublist with 88 entries. They are the maximum eigenvalues' real parts at the first 88 wavenumbers, including 0.

4. BU4.Dispersion_relations.py takes band10.txt as its input and generates figures 6.2, 6.3, and 6.6.

5. BU5.Bifurcation_M2_b3.py generates figure 6.4.

6. BU6.Bifurcation_VC_b4.py generates figure 6.5.

======================================================================================================================================================================================
COMSOL files

1. BU7.Secondary_NF_1D.mph is the COMSOL implementation of the secondary system in one dimension and with no-flux boundary conditions.
-The 1D concentration profiles of VEGFC at different time points are plotted in figures 6.7, 6.8, and 6.9.

2. BU8.Secondary_NF_2D.mph is the COMSOL implementation of the secondary system in two dimensions and with no-flux boundary conditions.
-The 2D concentration profiles of VEGFC at different time points are plotted in figure 6.11.

3. BU9.Secondary_P_2D.mph is the COMSOL implementation of the secondary system in two dimensions and with periodic boundary conditions.
-The 2D concentration profiles of VEGFC at different time points are plotted in figure 6.12.
======================================================================================================================================================================================
