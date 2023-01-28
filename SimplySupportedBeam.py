from enum import Enum

class SimplySupportedBeam():

    def __init__(self, id, L):
        self.L = L
        self.name = id
        self.load = [] # list of loads
        self.supports = [] # list of supports

    def add_load(self, load):
        self.load.append(load)

    def add_supports(self, supports):
        self.supports.append(supports)

    def remove_load(self, load):
        self.load.remove(load)

    def remove_supports(self, supports):
        self.supports.remove(supports)

    
        