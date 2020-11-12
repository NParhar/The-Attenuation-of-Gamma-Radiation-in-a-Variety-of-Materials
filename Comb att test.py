import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
from combatt  import combo_att
from combatt1 import err_part
from combatt2 import av
#Attenuations and errors:
#lead: 0.0962, 0.0009
#brick: 0.09, 0.02
#Al: 0.0699, 0.0005
#Wood: 0.0781, 0.0006
#Steel: 0.069, 0.001
#conc: 0.06369, 0.00001
#polystyrene: 0.03, 0.02
print('Lead and Brick:'), av().calc_err_av(687,1620, 0.0962, 0.09, [1,2,3], 1, 1, 1, 0.0009, 0.02)
print('Steel and Brick:'), av().calc_err_av(1600,1620, 0.069, 0.09, [2,4,6,8], 1, 1, 1, 0.001, 0.02)
print('Lead and Concrete:'), av().calc_err_av(687,4474, 0.0962, 0.06369, [1,2,3], 1, 1, 1, 0.0009, 0.00001)
print('Aluminium and Brick:'), av().calc_err_av(1131,1620, 0.0699, 0.09, [2,4,6,8,10], 1, 1, 1, 0.0005, 0.02)














#combo_att.calc(m_1, m_2, att_1, att_2, n_1, n_2)
#print(combo_att().calc(687,1620, 0.0962, 0.09, 3, 1))
#print(err_part().calc_err_part(687,1620, 0.0962, 0.09, 1, 1, 1, 1, 0.0009, 0.02))