import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
from part3 import get_file
from part4 import plot_data
from part5 import get_varied
from part6 import get_density
from part7 import get_av_density
from part8 import get_thick_activity
from part8b import get_thick_activityb
from part8c import get_pts
from part4b import data_table
class table_a:
    """This class writes a table containing vital data- both measured and calculated."""
    def __init__(self):
        self.file_path_thics = ''
        self.file_path_s = ''
        self.file_path_b = ''
        self.file_path_table = ''

    def write_table(self, file_path_thics,file_path_s, file_path_b, file_path_table):
        x=(data_table().plot_table(file_path_thics, file_path_s, file_path_b))
        f=open(file_path_table,'w')
        for a in x:
            f.write(str(a).replace('[','').replace(']','').replace(',','').replace("'",'')+'\n' )
        f.close() 