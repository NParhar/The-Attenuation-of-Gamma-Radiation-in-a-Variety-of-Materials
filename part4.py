import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
from part3 import get_file
import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import itertools
from matplotlib.ticker import FormatStrFormatter
from part5 import get_varied
from part8 import get_thick_activity
from part8b import get_thick_activityb
from part8c import get_pts
from math import log10, floor
import scipy
from scipy import optimize
from scipy.optimize import curve_fit
from function import function1
#from part6 import get_thickness
class plot_data:
    """This class plots the data from the file using the other classes."""
    def __init__(self):
        self.values1 = []
        self.file_path = ''
        self.file_path_thics = ''
        self.file_path_s = ''
        self.file_path_b = ''
        self.title=''
        self.n = 1
        self.b= 1
        self.c =1        
#############################################################################################################################
#E N graph
    def plot_energy_count(self, file_path):
        a=get_file().get_file_data(file_path)
        b=[]
        for x in range(0,len(a)):
            b.append(x)
        y=[]
        for x in a:
            y.append(x)        
        plt.yscale('log')
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.d')) 
        plt.ylim(ymax=sorted(y)[-1]+1)

        axis = plt.subplot()
        axis.errorbar(b, y, fmt ='-' , color ='r')
        axis.set_xlabel('Energy $(keV)$', fontsize=14)
        axis.set_ylabel('Counts', fontsize=14)
        #plt.suptitle(batch)
        plt.show()
##########################################################################################################################
#pT A graph
    def plot_pT_A(self, file_path_thics, file_path_s, file_path_b, title):
        a=get_pts().get_pt(file_path_thics, file_path_s, file_path_b)
        x=a[2]
        x_err=a[3]
        y=a[0]
        y_err=a[1]
   
        axis = plt.subplot()
        axis.errorbar(x, y, xerr=x_err , yerr=y_err, capsize=3, ecolor='r', fmt ='x' , color ='k')
        axis.set_xlabel('Density x Thickness $(g/cm^{2})$', fontsize=14)
        axis.set_ylabel('Activity $(Bq)$', fontsize=14)
        plt.suptitle(title)
        plt.show()
###############################################################################################
