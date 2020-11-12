import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2
from part3 import get_file
class get_varied:
    """This class calculates activity and its error."""
    def __init__(self):
        self.values1 = []
        #counts
        self.values2 = []
        #live time
        self.values3 = []
        #activity
        self.file_path_counts = ''
                   
    def get_activity(self, file_path_counts): 
        self.values1 = []
        self.values2 = []
        self.values3 = []
        a= np.genfromtxt(fname=file_path_counts, dtype= float, usecols=0)
        b=np.genfromtxt(fname=file_path_counts, dtype= float, usecols=1)
        for x in range(0,len(a)):
            self.values1.append(a[x])
            self.values2.append(b[x])
            self.values3.append(float(a[x]/b[x]))        
        return(self.values3)

    def get_activity_err(self, file_path_counts): 
        self.values1 = []
        #Nerr
        self.values2 = []
        #time
        self.values3 = []
        a= np.genfromtxt(fname=file_path_counts, dtype= float, usecols=0)
        b=np.genfromtxt(fname=file_path_counts, dtype= float, usecols=1)
        for x in range(0,len(a)):
            if (np.sqrt(a[x]))>=(0.01*(a[x])):
                self.values1.append(np.sqrt(a[x]))
            else:
                self.values1.append(0.01*(a[x]))     
            self.values2.append(b[x])

        for y in range(0,len(self.values1)):
            self.values3.append(float(self.values1[y]/b[y]))        
        return(self.values3)
   
