import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2 
from part7 import get_av_density
from part6 import get_density
class get_thick_activity:
    """This class calculates density of a material multiplied by its thickness."""
    def __init__(self):
        self.file_path_sheet= ''
        self.file_path_block= ''
        self.sheets = 0. 
        self.blocks= 0. 
        self.av_p = 0.
        self.av_p_err = 0.
        self.t_err = 0.
        self.t = 0.
        self.pt = 0.
        self.pt_err =0. 
        self.file_path_thics =''
        self.activity = []
        self.activity_err =[]
        self.N=[]
        self.N_err= []
        self.livetime=[]     
        self.sheet_no =[]
        self.block_no =[]

                         
    def get_pt(self, file_path_sheet, file_path_block, sheets, blocks):
        self.sheets += sheets
        self.blocks += blocks
        self.av_p += get_av_density().get_p_av(self.file_path_sheet,self.file_path_block, self.sheets, self.blocks)[0]
        self.av_p_err += get_av_density().get_p_av(self.file_path_sheet,self.file_path_block, self.sheets, self.blocks)[1]
        self.t += get_av_density().get_p_av(self.file_path_sheet,self.file_path_block, self.sheets, self.blocks)[2]
        self.t_err += get_av_density().get_p_av(self.file_path_sheet,self.file_path_block, self.sheets, self.blocks)[3]
        self.pt += self.av_p*self.t
        self.pt_err +=np.sqrt( (self.av_p_err/self.av_p)**2 + (self.t_err/self.t)**2)
        return(self.pt, self.pt_err)

    def get_activities(self, file_path_thics):
        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=0):
            self.sheet_no.append(x)
        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=1):
            self.block_no.append(x)

        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=2):
            self.N.append(x)
        for x in np.genfromtxt(fname=file_path_thics, dtype= float, usecols=3):
            self.livetime.append(x)      
        for x in self.N:
            if np.sqrt(x)>= 0.01*x:
                self.N_err.append(np.sqrt(x))
            else: 
                self.N_err.append(0.01*x)
        for x in range(0, len(self.N)):
            self.activity.append((self.N[x]/self.livetime[x]))
            self.activity_err.append((self.N_err[x]/self.livetime[x]))

        return(self.sheet_no, self.block_no, self.activity, self.activity_err)


        

       