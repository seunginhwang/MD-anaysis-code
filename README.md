# MD-anaysis-code
- 👋 Hi, I’m @seunginhwang
- 👀 I’m interested in ... python, machine-learning
- 🌱 I’m currently learning ... Oracle
- 📫 How to reach me ... seungin0521@gmail.com


This document describes a code for analyzing the xtc file used in GROMACS, a molecular dynamics simulation program, and the dat file resulting from umbrella sampling.
To use the code, you may need to modify the molecule's code name or adjust minor numerical settings. The code, based on the data file of GROMACS 2021, is described as follows:

[RDF.py]
This code calculates Radial Distribution Functions (RDFs), denoted as g(r), which define the probability of finding a particle at a distance r from a given particle. 
The RDF is highly dependent on the material type, varying greatly for solids, gases, and liquids. 
The reference density ρ (Molar mass of target molecule * Number of target molecules / Box size) remains consistent within a given system.

[overlap_ratio.py]
This code relates to umbrella sampling, a sampling method used in computational chemistry. 
Unlike general MD simulations that sample a system in a low free energy equilibrium state, umbrella sampling uses each frame of a changing system as an initial structure, performing sampling in various states to observe free energy.

As the simulation progresses, several graphs resembling a normal distribution appear. The x-axis represents the distance from the surface, while the y-axis represents probability.
Free energy is calculated based on these graphs, with the accuracy of the calculation depending on whether each graph has a normal shape with one peak and is well arranged according to the frame order. 
Ideally, the overlap region between each graph should be about one-third of one graph's area.
This code helps determine whether umbrella sampling has been performed appropriately by outputting the integral value of the given graphs and the ratio of the overlap region.
