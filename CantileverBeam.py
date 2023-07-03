from enum import Enum

class CantileverBeam():

    def __init__(self, id, L):
        self.L = L
        self.name = id
        self.load = [] # list of loads
        self.supports = [] # list of supports

    def add_load(self, load):
        self.load.append(load)

    def add_support(self, support):
        self.supports.append(support)

    def remove_load(self, load):
        self.load.remove(load)

    def remove_support(self, support):
        self.supports.remove(support)