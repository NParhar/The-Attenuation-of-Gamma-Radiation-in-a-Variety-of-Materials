import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2
class get_file:
    """This class creates one list containing all of the data using a file_path."""
    def __init__(self):
        self.values1 = []
        self.file_path = ''
                   
    def get_file_data(self, file_path): 
        self.values1 = []
        a= np.genfromtxt(fname=file_path, dtype= float, usecols=0, skip_header=11, skip_footer=14)
        for x in range(0,len(a)):
            self.values1.append(a[x])
        return(self.values1)

