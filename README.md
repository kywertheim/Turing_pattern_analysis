# Turing_pattern_analysis
Context: Wertheim, Kenneth Yann (2017). Mathematical Modelling of Lymphangiogenesis. University of Southampton, Doctoral Thesis, 234pp.

About: This repository contains the python programs used for Turing pattern analysis in chapter 6 of the above thesis, as well as their outputs.

Hardware: The programs were run on a desktop computer with an Intel(R) Core(TM) i5-3570 CPU at 3.40 GHz and 16 GB of RAM.

BU1.Turing_space.py explores the parametric space of the secondary system, leading to a sample of Turing points.
1. The output is turing1_band.txt.
2. In turing1_band.txt, there is a collection of lists. Each list has the format [b1, b2, b3, b4, b5, a1m2, a1vc, a2m2, a2vc, a3, a4, [dispersion relation]].
3. [dispersion relation] is a sublist with 88 entries. They are the maximum eigenvalues' real parts at the first 88 wavenumbers, including 0.

BU2.Parametric_distributions.py takes turing1_band.txt as its input and generates figure 6.1.

BU3.Ranking.py takes turing1_band.txt as its input and finds the 10 Turing points closest to the reference point in the parametric space.
1. The output is band10.txt.
2. In band10.txt, there are 10 lists. Each has the format [b1, b2, b3, b4, b5, a1m2, a1vc, a2m2, a2vc, a3, a4, [dispersion relation]].
3. [dispersion relation] is a sublist with 88 entries. They are the maximum eigenvalues' real parts at the first 88 wavenumbers, including 0.

BU4.Dispersion_relations.py takes band10.txt as its input and generates figures 6.2, 6.3, and 6.6.

BU5.Bifurcation_M2_b3.py generates figure 6.4.

BU6.Bifurcation_VC_b4.py generates figure 6.5.
