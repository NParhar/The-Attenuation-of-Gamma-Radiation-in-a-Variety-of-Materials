import matplotlib.pyplot as plt
import math
import copy
import numpy as np 
import os
import glob2
from part6 import get_density
class get_av_density:
    """This class calculates average density of a material."""
    def __init__(self):
        self.file_path_sheet = ''
        self.file_path_block = ''

        self.sheets = 0.
        self.blocks = 0.

        self.p_av = 0. 
        self.p_av_err = 0.

        self.density_sheet = 0.
        self.density_sheet_error = 0.
        self.mass_sheet = 0.
        self.mass_sheet_error = 0.
        self.vol_sheet = 0.
        self.vol_sheet_error = 0.

        self.density_block = 0.
        self.density_block_error = 0.
        self.mass_block = 0.
        self.mass_block_error = 0.
        self.vol_block = 0.
        self.vol_block_error = 0.

        self.a = 0.
        self.a2 =0.
        self.b = 0.
        self.b2 =0.

        self.sheet_thic = 0.
        self.block_thic = 0.
        self.sheet_thic_error = 0.
        self.block_thic_error = 0.
        self.av_thic =0.
        self.av_thic_error =0. 

    def get_p_av(self, file_path_sheet, file_path_block, sheets, blocks):
        self.sheets+= sheets
        self.blocks += blocks
        self.density_sheet += (get_density().get_pmV(file_path_sheet))[0]
        self.density_sheet_error += (get_density().get_pmV(file_path_sheet))[1]
        self.mass_sheet += (get_density().get_pmV(file_path_sheet))[2]
        self.mass_sheet_error += (get_density().get_pmV(file_path_sheet))[3]
        self.vol_sheet += (get_density().get_pmV(file_path_sheet))[4]
        self.vol_sheet_error += (get_density().get_pmV(file_path_sheet))[5]
        self.sheet_thic += (get_density().get_pmV(file_path_sheet))[6]
        self.sheet_thic_error += (get_density().get_pmV(file_path_sheet))[7]

        self.density_block += (get_density().get_pmV(file_path_block))[0]
        self.density_block_error += (get_density().get_pmV(file_path_block))[1]
        self.mass_block += (get_density().get_pmV(file_path_block))[2]
        self.mass_block_error += (get_density().get_pmV(file_path_block))[3]
        self.vol_block += (get_density().get_pmV(file_path_block))[4]
        self.vol_block_error += (get_density().get_pmV(file_path_block))[5]
        self.block_thic += (get_density().get_pmV(file_path_block))[6]
        self.block_thic_error += (get_density().get_pmV(file_path_block))[7]

        self.a+= self.sheets*(self.mass_sheet_error**2) + self.blocks*(self.mass_block_error**2)
        self.a2+= (self.sheets*self.mass_sheet +self.blocks*self.mass_block)**2

        self.b+= self.sheets*(self.vol_sheet_error**2) + self.blocks*(self.vol_block_error**2)
        self.b2+= (self.sheets*self.vol_sheet +self.blocks*self.vol_block)**2


        self.p_av += ((self.sheets*self.mass_sheet)+(self.blocks*self.mass_block))/((self.sheets*self.vol_sheet) + (self.blocks*self.vol_block))
        self.p_av_err+= self.p_av*np.sqrt( self.a/self.a2 +self.b/self.b2 )

        if self.blocks==0. and self.sheets !=0. : 
            self.av_thic += self.sheets*self.sheet_thic
            self.av_thic_error += np.sqrt(self.sheets*(self.sheet_thic_error)**2 )

        if self.sheets==0. and self.blocks!=0. : 
            self.av_thic += self.blocks*self.block_thic
            self.av_thic_error += np.sqrt(self.blocks*(self.block_thic_error)**2 )

        if self.blocks!=0. and self.sheets!=0. : 
            self.av_thic += self.sheets*self.sheet_thic + self.blocks*self.block_thic
            self.av_thic_error += np.sqrt( self.sheets*(self.sheet_thic_error)**2 + self.blocks*(self.block_thic_error)**2 )

        else:
            self.av_thic += 0.
            self.av_thic_error += 0.
        return(self.p_av, self.p_av_err, self.av_thic, self.av_thic_error)

