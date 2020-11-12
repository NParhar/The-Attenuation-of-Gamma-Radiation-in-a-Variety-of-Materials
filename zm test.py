import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
from zm1  import total_zm
#INPUT:
#material,z,m,compp,comp_err
#OUTPUT:
#material, z, z_err,  m, m_err,   z/m, z/m_err
total_zm().calc_zm('WOOD',[6,8,1,7], [12,16,1,14], [0.5, 0.42, 0.06, 0.01], [0.05,0.05,0.02,0.005])
total_zm().calc_zm('STEEL',[28,26,24,6], [58.7,55.8,52,12], [0.08, 0.7392, 0.18, 0.0008], [0.04,0.05,0.05,0.01])
total_zm().calc_zm('BRICK',[30,50,28,76], [60,102,56,159.6], [0.55, 0.25, 0.035, 0.07], [0.05,0.05,0.02,0.04])

