import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import itertools
from math import log10, floor
import csv
from combatt  import combo_att

class err_part:
    """This class calc.s attenuation of materials."""
    def __init__(self):
        self.m_1 = 1.
        self.m_2 = 1.
        self.att_1 = 1.
        self.att_2 = 1.
        self.m_1_err = 1.
        self.m_2_err = 1.

    def calc_err_part(self, m_1, m_2, att_1, att_2, n_1, n_2, m_1_err, m_2_err, att_1_err, att_2_err):
        mu_over_p = combo_att().calc(m_1, m_2, att_1, att_2, n_1, n_2)
        w_1 = (n_1*m_1/(n_1*m_1+n_2*m_2))
        w_2 = (n_2*m_2/(n_1*m_1+n_2*m_2))

        w_err_1 = w_1 *np.sqrt( (m_1_err*np.sqrt(n_1)/(m_1*n_1))**2 + (n_1*m_1_err**2 + n_2*m_2_err**2)/( (n_1*m_1) + (n_2*m_2) )**2  )
        w_err_2 = w_2 *np.sqrt( (m_2_err*np.sqrt(n_2)/(m_2*n_2))**2 + (n_1*m_1_err**2 + n_2*m_2_err**2)/( (n_1*m_1) + (n_2*m_2) )**2  )
        #add sqrt outside

        att_err_1 = np.sqrt( (w_err_1/w_1)**2 +  (att_1_err/att_1)**2 ) * att_1
        att_err_2 = np.sqrt( (w_err_2/w_2)**2 +  (att_2_err/att_2)**2 ) * att_2

        att_total_err = np.sqrt(att_err_1**2 + att_err_2**2)
        return(mu_over_p, att_total_err)