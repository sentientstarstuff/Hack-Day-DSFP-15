#!/usr/bin/env python
# coding: utf-8

# # Overview of Discrete 3D Data
# 
# We're going to talk about a couple different ways of getting overviews of 3D data that is stored discretely.
# 
# For this, we'll use some "real" data from a galaxy simulation, accessible on the yt-project [sample data page](https://yt-project.org/data/).  Go ahead and download [Gadget Disk Galaxy](http://yt-project.org/data/GadgetDiskGalaxy.tar.gz) and extract it.

#  * Scatter plots and their problems
#  * Summarization of discrete data
#  * Computing neighbor information
#  * Really large sets of particles
#  * Binning, hexbinning, and smoothing

# In[1]:


import numpy as np
import h5py
import matplotlib.pyplot as plt
import matplotlib.colors as mcm
from SPH_functions import Kernel, gradW
#import ipywidgets
#import pythreejs
plt.rcParams["figure.dpi"] = 200


# In[4]:


class coordinate:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def transform():
        pass
    
    # TODO: act like a tuple


# In[10]:


class particle:
    def __init__(self, mass = 1, position = coordinate, velocity = 0, temperature = 373, k = 1, h = 1, lmda = 1, dt = 0.5, n = 1):
        self.mass = mass # g
        self.position = position # cm
        self.velocity = velocity # cm/s
        self.temperature = temperature # Kelvin
        self.h = h
        self.k = k
        self.dt = dt
        self.n = n
        self.lmda = lmda
        
    def location(self):
        #print(self.position)
        return np.sqrt(self.position[0]**2 + self.position[1]**2)
    
    def __sub__(self, other):
        return np.sqrt((self.position[0] - other.position[0])**2 + (self.position[1] - other.position[1])**2)
    
    def density(self):
        return self.mass*Kernel(self, Vol = 1)
    
    def pressure(self):
        return self.k * self.density()**(1+1/self.n)
    
    def acc(self):
        p = max(self.pressure(), 0.001)
        rho = max(self.density(),0.0001)
        dWx = gradW(self, Vol = 1)

        return self.mass * 2*p/rho**2 * dWx - self.lmda*self.location()
    
    def vel(self):
        return 0.5*self.acc()*self.dt
    
    def new_pos(self):
        return self.vel()*self.dt
    
#     def vel(self, h, k):
#         return 

