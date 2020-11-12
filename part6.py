import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2
from part3 import get_file
class get_density:
    """This class calculates density of a material."""
    def __init__(self):
        self.L = 0
        self.L_err = 0.
        self.W = 0
        self.W_err = 0.
        self.T = 0
        self.T_err = 0.
        self.m = 0
        self.m_err = 0.
        self.V = 0.
        self.V_err = 0.
        self.p = 0.
        self.p_err = 0.
        self.file_path = ''
                         
    def get_pmV(self, file_path):
        len1= np.genfromtxt(fname=file_path, dtype= float, usecols=0)
        len_err= np.genfromtxt(fname=file_path, dtype= float, usecols=1)
        wid= np.genfromtxt(fname=file_path, dtype= float, usecols=2)
        wid_err= np.genfromtxt(fname=file_path, dtype= float, usecols=3)
        thic= np.genfromtxt(fname=file_path, dtype= float, usecols=4)
        thic_err= np.genfromtxt(fname=file_path, dtype= float, usecols=5)
        mass= np.genfromtxt(fname=file_path, dtype= float, usecols=6)
        mass_err= np.genfromtxt(fname=file_path, dtype= float, usecols=7)
        self.L+=len1
        self.L_err+=len_err
        self.W+=wid
        self.W_err+=wid_err       
        self.T+=thic
        self.T_err+=thic_err
        self.m+=mass
        self.m_err+=mass_err 
        self.V+= (self.L *self.W * self.T)
        self.V_err+= self.V*np.sqrt((self.L_err/self.L)**2 + (self.W_err/self.W)**2 + (self.T_err/self.T)**2)
        self.p+= float(self.m/self.V)
        self.p_err+= self.p* np.sqrt((self.m_err/self.m)**2 + (self.V_err/self.V)**2)
        return(self.p, self.p_err, self.m, self.m_err, self.V, self.V_err, self.T, self.T_err)

