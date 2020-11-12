import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
from combatt  import combo_att
from combatt1 import err_part

#(err_part().calc_err_part(687,1620, 0.0962, 0.09, 1, 1, 1, 1, 0.0009, 0.02))
import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import itertools
from math import log10, floor
import csv


class av:
    """This class calc.s attenuation of materials."""
    def __init__(self):
        self.m_1 = 1.
        self.m_2 = 1.
        self.att_1 = 1.
        self.att_2 = 1.
        self.m_1_err = 1.
        self.m_2_err = 1.
        self.n_1 = []
        self.list_of_att = []
        self.list_of_att_err = []


    def calc_err_av(self, m_1, m_2, att_1, att_2, n_1, n_2, m_1_err, m_2_err, att_1_err, att_2_err):
        """This class calc.s attenuation average for a combination of materials."""
        for x in n_1:
            y=err_part().calc_err_part( m_1, m_2, att_1, att_2, x, n_2, m_1_err, m_2_err, att_1_err, att_2_err)
            self.list_of_att.append(y[0])
            self.list_of_att_err.append(y[1])
        z=0.
        p=0.
        for x in self.list_of_att:
            z+=x
        average = float(z/len(self.list_of_att))
        for x in range(0,len(self.list_of_att_err)):
            p += (self.list_of_att_err[x])**2
        average_err = np.sqrt(p)
        print(average, average_err)

