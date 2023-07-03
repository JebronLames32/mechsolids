from SimplySupportedBeam import *
from math_functions import *

Name = "Q12"
L = 4
Beam1 = SimplySupportedBeam(Name, L)
equation = "w0+k*x**2"
load_list = [EquationLoad(equation,0,L,2.4,4.8)]
support = Support(0,4)


for load in load_list :
    Beam1.add_load(load)
    print(load.equation)
Beam1.add_supports(support)
Beam1.generate_sf_at_all_points()
# print(Beam1.supports[0].reaction1)

# Beam1.plot_sfd()
Beam1.plot_bmd()



# take the description of the beam

# print("Enter the equation of the load intensity w(x) in terms of x")
# equation = input(("w(x) = "))
# print("Equation of the load intensity w(x) is: ", equation)