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
from part4 import plot_data
from math import log10, floor
import csv

class data_table:
    """This class plots the data in the form of a table."""
    def __init__(self):
        self.col_names = []
        self.file_path_thics = ''
        self.file_path_s = ''
        self.file_path_b = ''

        self.Activity = []
        self.Activity_err =[]
        self.pthic = []
        self.pthic_err = []
        self.sheet_no = []
        self.block_no= []
        self.livetime= []
        self.counts = []
        self.counts_err = []
        self.av_th=[]
        self.av_th_err=[]

        self.list1 =[]

    def plot_table(self, file_path_thics,file_path_s, file_path_b):
        a=get_pts().get_pt(file_path_thics, file_path_s, file_path_b)
        pt=a[2]
        pt_err=a[3]


        activity=a[0]
        activity_err=a[1]
        
        no_sheet = a[4]
        no_block=a[5]
        time = a[6]
        N=a[7]

        N_err=a[8]
        
        t = a[9]

        t_err=a[10]
        col_names_=['Sheets', 'Blocks', 'Thickness(cm)', 'T err(cm)', 'Counts', 'Counts err', 'Livetime(s)', 'Activity(Bq)', 'Activity err(Bq)', 'pT(g/cm^2)', 'pT err(g/cm^2)']

        for x in range(0, len(activity)):
            self.Activity.append(str(activity[x]))
            self.Activity_err.append(str(activity_err[x]))
            self.pthic.append(str(pt[x]))
            self.pthic_err.append(str(pt_err[x]))
            self.sheet_no.append(str(no_sheet[x]))
            self.block_no.append(str(no_block[x]))
            self.livetime.append(str(time[x]))
            self.counts.append(str(N[x]))
            self.counts_err.append(str(N_err[x]))
            self.av_th.append(float(t[x]))
            self.av_th_err.append(float(t_err[x]))

        x=[self.sheet_no, self.block_no, self.av_th, self.av_th_err, self.counts, self.counts_err, self.livetime, self.Activity, self.Activity_err, self.pthic, self.pthic_err]
        z=[]
        no_of_thics= len(self.Activity)
        for i in range(0,len(x)):
            for j in range(0,len(x[i])):
                y=x[i][j]
                z.append(y)
        len_z=len(z)
        lens_of_z= []
        for j in z:
            lens_of_z.append(len(str(j)))
        k_max=max(lens_of_z)
        rows=[]
        for j in range(0,no_of_thics):
            row=[]
            for i in range(0,int(len_z/(no_of_thics))):
                h=j+(i*no_of_thics)     
                row.append((z[h]))
            rows.append(row)

        for i in col_names_:
            self.col_names.append(i+' '*(k_max-len(str(i))))

        ###########################
        self.list1=[self.col_names]
        for i in range(0,len(rows)):
            k=[]
            for j in rows[i]:
                #n= j
                n=str(j)+ ' '*(k_max-len(str(j)))
                #k.append(float(n))
                k.append((n))
                #+ ' '*(k_max-len(str(k)))
            self.list1.append((k))
            ##############################



        return(self.list1)
