import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2 
from part7 import get_av_density
from part6 import get_density
class get_thick_activityb:
    """This class ccreates a list using the average density of a material."""
    def __init__(self):
        self.av_p = []
        self.av_p_err = []
        self.t_err = []
        self.t = []
        self.pt = []
        self.pt_err =[] 
        self.file_path_thics =''
        self.activity = []
        self.activity_err =[]
        self.N=[]
        self.N_err= []
        self.livetime=[]     
        self.sheet_no =[]
        self.block_no =[]


    def get_activities(self, file_path_thics):
        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=0):
            self.sheet_no.append(x)
        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=1):
            self.block_no.append(x)

        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=2):
            self.N.append(x)
        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=3):
            self.livetime.append(x)      
        for x in self.N:
            if np.sqrt(x)>= 0.01*x:
                self.N_err.append(np.sqrt(x))
            else: 
                self.N_err.append(0.01*x)
        for x in range(0, len(self.N)):
            self.activity.append((self.N[x]/self.livetime[x]))
            self.activity_err.append((self.N_err[x]/self.livetime[x]))


        return(self.activity, self.activity_err, self.sheet_no, self.block_no, self.livetime, self.N, self.N_err)