import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2 
from part7 import get_av_density
from part6 import get_density
from part8b import get_thick_activityb
class get_pts:
    """This class calculates density of a material."""
    def __init__(self):
        self.file_path_sheet= ''
        self.file_path_block= ''
        self.av_p = []
        self.av_p_err = []
        self.t_err = []
        self.t = []
        self.pt = []
        self.pt_err =[] 
        self.file_path_thics =''
        self.activity = []
        self.activity_err =[]
        self.N=[]
        self.N_err= []
        self.livetime=[]     
        self.sheet_no =[]
        self.block_no =[]
        self.livetime = []
    
 
    def get_pt(self, file_path_thics, file_path_sheet, file_path_block):
        b=get_thick_activityb().get_activities(file_path_thics)
        for x in b[2]:
            self.sheet_no.append(x)
        for x in b[3]:
            self.block_no.append(x)
        for x in b[0]:
            self.activity.append(x)
        for x in b[1]:
            self.activity_err.append(x)
        for x in b[4]:
            self.livetime.append(x)
        for x in b[5]:
            self.N.append(x)
        for x in b[6]:
            self.N_err.append(x)



        for c in range(0,len(self.sheet_no)):            
            a=get_av_density().get_p_av(file_path_sheet, file_path_block, self.sheet_no[c], self.block_no[c])
            self.av_p.append(a[0])
            self.av_p_err.append(a[1])
            self.t.append(a[2])
            self.t_err.append(a[3])

        for x in range(0, len(self.av_p)):
            if self.t[x]==0. and self.av_p[x]==0.:
                self.pt.append(0.)
                self.pt_err.append (0.)
            if self.t[x]==0. or self.av_p[x]==0.:
                self.pt.append(0.)
                self.pt_err.append (0.)
            if self.t[x]!=0 and self.av_p[x]!=0.:
                self.pt.append(self.av_p[x]*self.t[x])            
                y=(self.av_p[x]*self.t[x])*np.sqrt( (self.av_p_err[x]/self.av_p[x])**2 + (self.t_err[x]/self.t[x])**2 )
                self.pt_err.append (y)


        return(self.activity, self.activity_err, self.pt, self.pt_err, self.sheet_no, self.block_no, self.livetime, self.N, self.N_err, self.t, self.t_err)

