<h1 align="center"> Mechanics of Solids</h1>
<h2 align="center">Mechanical Engineering Department, Indian Institute of Technology Kharagpur</h2>



This is a repository of some useful files for the subject __"Mechanics of
Solids"__ in the Mechanical Engineering Department of IIT Kharagpur. This
subject is a mandatory one for the second year undergraduate students of
Mechanical Engineering. 

The latest version of the course home page is maintained at: [http://www.facweb.iitkgp.ac.in/~jeevanjyoti/teaching/mechsolids/2021/](http://www.facweb.iitkgp.ac.in/~jeevanjyoti/teaching/mechsolids/2021/)


* [Tutorial Sheet 2A: Q3](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/TS2A-Q3.ipynb)

* [Tutorial Sheet 2A: Q7](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/TS2A-Q7.ipynb)

* [Tutorial Sheet 2A: Q8](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/TS2A-Q8.ipynb)

* [Tutorial Sheet 2A: Q9](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/TS2A-Q9.ipynb)

* [Mohr Circle](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/Mohr_Circle.ipynb)

* [Tutorial Sheet 5: Q13: Polar Strain-Displacement](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/TS5-Q13_polar_strain-displ.ipynb)

* [Stress equilibrium equations in cylindrical coordinates](https://nbviewer.jupyter.org/github/jeevanjyoti4/mechsolids/blob/master/stress_eqb_cyl.ipynb)

<h2>  Manual to use the Beam class </h2>
We need to have Sympy installed before using the beam class. To install Sympy, use the following command:

```bash
pip install sympy
```

* Tested with Sympy version 1.11.1
* Tested with Python version 3.9.13
<ol>
<li> Create a new Python file to solve a problem. Import the Beam and math modules as follows:
  
```python
from Beam import *
from math_functions import *
```
</li>

<li> Create either a *Simply Supported Beam* or a *Cantilever Beam* object as follows:
  
```python
beam = SimplySupportedBeam(NameOfBeam, LengthOfBeam)
beam = CantileverBeam(NameOfBeam, LengthOfBeam)
```
</li>

<li> If the beam is a *Simply Supported Beam*, then add the supports as follows:
  
```python
beam.add_supports(Support(PositionOfSupport1, PositionOfSupport2))
```
where *position* is the distance of the support from the left end of the beam.
</li>

<li> Create loads using the load class as follows:
  
```python
load1 = PointLoad(ValueOfLoad, PositionOfLoad)
load2 = DistributedLoad(StartPosition, EndPosition, LoadAtStart, LoadAtEnd)
load3 = EquationLoad(EquationString, StartPosition, EndPosition, startLoad(=0), endLoad(optional))

# add these loads on the beam
beam.add_load(load1)
beam.add_load(load2)
beam.add_load(load3)
```
where *position* is the distance of the load from the left end of the beam.
</li>

<li> To generate the shear force and bending moment diagrams, use the following functions:
  
```python
beam.plot_sfd_and_bmd()
# if you want to plot just the shear force diagram or bending moment diagram, use the following functions:
beam.plot_sfd()
beam.plot_bmd()
```
</li>
</ol>