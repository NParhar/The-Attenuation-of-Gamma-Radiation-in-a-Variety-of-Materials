import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
import itertools
from math import log10, floor
import csv

class combo_att:
    """This class calc.s attenuation of 2 materials."""
    def __init__(self):
        self.m_1 = 1.
        self.m_2 = 1.
        self.att_1 = 1.
        self.att_2 = 1.

    def calc(self, m_1, m_2, att_1, att_2, n_1, n_2):
        m_total = (m_1*n_1) + (m_2*n_2)
        ratio_1 = n_1*m_1/m_total
        ratio_2 = n_2*m_2/m_total
        part_1 = ratio_1 * att_1
        part_2 = ratio_2 * att_2
        x = part_1 + part_2
        return(x)
              