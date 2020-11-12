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
#from part6 import get_thickness
class function1:
    def __init__(self):    
        self.x=[]
        self.n=1
        self.b=1
        self.c=1

    def func(self,x,n,b,c):
        return(n*np.exp(x*b) + c)

