import matplotlib.pyplot as plt
import math
import copy
import os
import numpy as np 
class total_zm:
    """This class calc.s z/m and its error for materials."""
    def __init__(self):
        self.z = []
        self.m = []
        self.comp = []
        self.comp_err = []
        self.material = ''
        
    def calc_zm(self,material,z,m,comp, comp_err):
        """This class uses given z,m,composition and comp error in the form of a list to calc z/m and its error."""
        z_total = 0.
        m_total = 0.
        p1 = []
        p2 = []
        for x in range (0,len(z)):
            z_total+= z[x]*comp[x]
            m_total+= m[x]*comp[x]
            p1.append((z[x] * comp_err[x]/comp[x])**2)
            p2.append((m[x] * comp_err[x]/comp[x])**2)
        Z_err_1 = 0.
        M_err_1 = 0.
        for x in range (0,len(z)):
            Z_err_1+= p1[x]
            M_err_1+= p2[x]
        Z_err = np.sqrt(Z_err_1)
        M_err = np.sqrt(M_err_1)
        zm= z_total/ m_total
        zm_err = zm * np.sqrt((Z_err/z_total)**2 + (M_err/m_total)**2 )
        print(material+':')
        print('z:'+ str(z_total)+' +/- '+ str(Z_err))
        print('m:'+ str(m_total)+' +/- ' + str(M_err))
        print('z/m:'+ str( zm)+' +/- '+ str(zm_err))


