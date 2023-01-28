from SimplySupportedBeam import *
from math_functions import *

Beam1 = SimplySupportedBeam("Beam1", 6)
Beam1.add_load(DistributedLoad(0, 3, 0, 4))
Beam1.add_load(DistributedLoad(3, 6, 4, 4))
Beam1.add_supports(Support(0,3))
Beam1.plot_sfd()
