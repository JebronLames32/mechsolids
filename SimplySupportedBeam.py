from enum import Enum
from math_functions import *
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

class SimplySupportedBeam():

    def __init__(self, id, L):
        self.length = L
        self.name = id
        self.load = [] # list of loads
        self.supports = 0 #A single definition should include both supports. Assuming two supports in a simply supported beam.

    def add_load(self, load):
        self.load.append(load)

    def add_supports(self, supports):
        self.supports = supports

    def remove_load(self, load):
        self.load.remove(load)

    # def remove_supports(self, supports):
    #     self.supports.remove(supports)

    def generate_function_list_of_sfd(self, x):
        sfd = 0
        for load in self.load :
            if(isinstance(load, PointLoad)):
                if(x>=load.dist):
                    sfd -= load.load
                
            elif(isinstance(load, DistributedLoad)):
                if(x >= load.start and x<=load.end):
                    sfd -= load.Area_under_load(x)
                elif(x > load.end):
                    sfd -= load.Area_under_load()

        support = self.supports
        if(isinstance(support, Support)):
            if(x >= support.position1):
                sfd += support.reaction1
            if(x >= support.position2):
                sfd += support.reaction2
        
        return sfd
        

    def find_equation_of_sfd(self):
        # sfd = []
        N = 1001
        x = np.linspace(0,self.length,N)

        self.supports.Reaction_at_support(self.load)

        sf_at_points = np.vectorize(self.generate_function_list_of_sfd)
        V = sf_at_points(x)
        return x, V

    def generate_function_list_of_bmd(self, x):
        pass

    def find_equation_of_bmd(self):
        pass

    def plot_sfd(self):
        rcParams['font.size']=16
        rcParams['mathtext.fontset']='cm'

        x, V = self.find_equation_of_sfd()
        V = np.array(V, dtype=float)

        #fig, axes = plt.subplots(1,2,tight_layout=True)

        fig = plt.figure()
        ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
        ax2 = fig.add_axes([1.2,0.1,0.8,0.8])

        #plt.subplot(1,2,1)
        ax1.plot(x,V,'blue')
        ax1.set_xlabel(r'$x\;\; [{\rm m}]$',fontsize=20)
        ax1.set_ylabel(r'$V\;\; [{\rm N}]$',fontsize=20)
        ax1.axhline(y=0,color='k')
        ax1.axvline(x=0,color='k')
        ax1.fill_between(x,V,color='blue',alpha=0.2)
        ax1.set_yticks([0, -4, -10, 12], minor=False)
        ax1.set_xticks([3,6], minor=False)
        ax1.grid(True)
        plt.show()

        # ax2.plot(x,M)
        # ax2.set_xlabel(r'$x\;\; [{\rm m}]$',fontsize=20)
        # ax2.set_ylabel(r'$M\;\; [{\rm N}\cdot {\rm m}]$',fontsize=20)
        # ax2.axhline(y=0,color='k')
        # ax2.axvline(x=0,color='k')
        # ax2.fill_between(x,M,color='blue',alpha=0.2)
        # ax2.set_yticks([0,-18], minor=False)
        # ax2.set_xticks([3,6], minor=False)
        # ax2.grid(True)

#test the functions
# Beam1 = SimplySupportedBeam("Beam1", 6)
# Beam1.add_load(DistributedLoad(0, 3, 0, 4))
# Beam1.add_load(DistributedLoad(3, 6, 4, 4))
# Beam1.add_supports(Support(0,3))
# Beam1.plot_sfd()
        
        


        
    
        