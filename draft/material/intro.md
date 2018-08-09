---
Introduction
---
Ordered intermetallic compounds are of great interest due to their high melting temperatures,
combined with the inherent advantages of ordered alloys such as low self-diffusion rates, high elastic moduli,
and the retention of these properties at high temperatures [1-6]. In addition, ordered intermetallics with the
L12 structure usually show an anomalous increase in yield stress with temperature over a wide temperature
range [7]. These materials, however, are generally brittle at low temperatures and this limits their use.

```
1. Schwarz RB, Desch PB, Srinivasan S, Nash P. Synthesis and properties of trialuminides with ultra-fine microstructures. Nanostructured Mater. 1992;1(1):37-42. doi:10.1016/0965-9773(92)90049-4
```

Two - phase titanium aluminide alloys exhibit a much better mechanical performance than their monolithic constituents γ(TiAl) and α2(Ti3Al), provided that the
phase distribution and grain size are suitably controlled.

Two-phase titantium aliuminde alloys with proper phase distribution and grain size exhibit better mechanical performance compared with monolithicconstituents gamma and alpha[].
~~~
1. habil. Fritz Appel D, Paul DJDH, Oehring DM. Deformation Behavior of Two-Phase α2(Ti3Al) + γ(TiAl) Alloys. In: Gamma Titanium Aluminide Alloys. Weinheim, Germany: Wiley-VCH Verlag GmbH & Co. KGaA; 2011:125-248. doi:10.1002/9783527636204.ch6
~~~



Brittle fracture in TiAl alloy strongly affects the safety of fracture of structure like turbo of aircraft engine and combustion generator. [**R**]

.Defects such as dislocation, void and segregation plays an significant role in the process of fracture[**R**].

In order to understanding the mechanism of brittle fracture, multiscale methods from micro to marco scale have been applied to investigate the behavior of fracture. It's necessary to carefully examine the revolution of defects and its influence on the fracture process at atomic scale. 

A previous study on void growth in gamma-TiAl single crystal has reveals that  void with high volume fraction detracts incipient yield strength [**R**].
```
[1] F.L. Tang, H.M. Cai, H.W. Bao, H.T. Xue, W.J. Lu, L. Zhu, Z.Y. Rui, Molecular dynamics simulations of void growth in γ-TiAl single crystal, Comput. Mater. Sci. 84 (2014) 232–237. doi:10.1016/j.commatsci.2013.12.014.
```


Molecular dynamics(MD method has been use to investigate the evolution of void in materials in nano-scale[**R**].

```
[1] T. Tang, S. Kim, M.F. Horstemeyer, Molecular dynamics simulations of void growth and coalescence in single crystal magnesium, Acta Mater. 58 (2010) 4742–4759. doi:10.1016/J.ACTAMAT.2010.05.011.
```

The fracture mechanisms in the duplex micro-structure are plasticity-induced grain boundary de- cohesion and cleavage, while those in the lamellar microstructure are interface delamination and crack- ing across the lamellae[**R**].
```
[1] K.S. Chan, Y.W. Kim, Influence of microstructure on crack-tip micromechanics and fracture behaviors of a two-phase TiAl alloy, Metall. Trans. A. 23 (1992) 1663–1677. doi:10.1007/BF02804362.
```


MD Simulation
---




|   a   |

 During the construction process, the grain centers were randomly placed in a simulation cell resulting in the arbitrary shape and orientation of the grains. 
 The construction of a specific grain would stop at a position where atoms from one grain centerwere no longer closer to the centers of other grains. 
 Eventually the construction ceased throughout the entire sample resulting in a three dimensional granular structure, as shown in Fig. 1(a). 
 The initial void diameters (D) ranged from 0.5 nm to 40 nm in models with 16.32 nm grain size, and from 0.5 nm to 7 nmin models with 6.92 nm grain size. 
 The grain sizes of 6.92 and 16.32 nm were chosen according to the computing capability of the computer we used and the number of grains inside the simulation cell. 
 The average grain sizewas calculated by the following method. 
 Given the number of atoms (N) in the simulation cell without a void, assuming all atoms in perfect fcc environment, the volume (Vcell) of the simulation cell then equaled to N ? a3
0/4, where a0 was lattice constant. The volume of the simulation cell was the total volume of all
grains inside the simulation cell because the simulation cellwas filled up with grains. Therefore,N?a3
0/4 equaled to n?4p(d/
2)3/3, assuming spherical grain, where n was the number of grains inside the simulation cell and d was average grain size. There was only one intragranular or intergranular spherical void within each simulation model. The intragranular spherical void was located in grain interior of the largest grain of the simulation model, as shown in Fig. 1(b). The intergranular spherical voidwas at the center of the simulation cell, as shown in Fig. 1(c). Simulation specimens of the 16.32 nm grain size models with initial void diameters at or below 13 nm were mainly considered in the analysis sections owing to the fact that their spherical void surfaces did not intersect with surrounding GBs after the equilibration process. This avoided conflict between competing sources of dislocation emission: GBs or spherical void surfaces. Different diameter intragranular voids were all embedded in the same grain and at the same position in the samples, as shown in Fig. 1(b). The intergranular voids with different initial diameters were identically at the center of the simulation model, as shown in Fig. 1(c). The poly- crystalline cubic samples with a volume of 39.773nm3 containing 27 grains and the same grain size of 16.32 nm, but different
initial void diameters, contained 2,428,690 (D ¼ 40 nm) to 5,201,491 (D ¼ 0.5 nm) atoms; while the 6.92 nm grain size simulation models with a volume of 39.773 nm3 containing 343 grains, and different initial void diameters, contained 5,027,708 to 5,042,878 atoms. The crystallographic orientations of all the grains were retained as initial void diameter changed. Finally, a model with the same structure but without a void was simulated for comparison purposes. Periodic boundary conditions were imposed in all the three directions of the cell. The embedded atom method, with
potential for Cu taken from Mishin et al. (2001),was used to determine interatomic interactions. The timestep for simulation was set to 1 fs. Prior to deformation, a conjugate gradient algorithm was first used to perform the energy minimization procedure. An 80 ps long isothermal annealing processwas performed at 300 K. Meanwhile, the pressure in all directionswas maintained at 0 Pa. Finally under the NPTensemble, the temperaturewas maintained at 0.1 K for 20 ps and the pressure in all directions was still maintained at 0 Pa. During the uniaxial tension, a total strain of 20% was applied to each sample in the x
direction at a constant engineering strain rate of 1 ?108 s?1. All simulations were performed at 0.1 K using a NoseeHoover thermostat

---

---
Results and discussion
---