#!/usr/bin/env python

import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.colors as mcm
#import ipywidgets
#import pythreejs

class coordinate:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def transform():
        pass
    
    # TODO: act like a tuple

class particle:
    def __init__(self, mass = 1, position = coordinate, velocity = 0, temperature = 373, smoothing_length = 1):
        self.mass = mass # g
        self.position = position # cm
        self.velocity = velocity # cm/s
        self.temperature = temperature # Kelvin
        self.smoothing_length = smoothing_length # unitless

