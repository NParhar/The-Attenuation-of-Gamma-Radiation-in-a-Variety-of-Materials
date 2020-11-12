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
from part_table import table_a

#print(get_file().get_file_data('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\Aluminium3sheet_text.txt'))
#plot_data().plot_energy_count('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\Aluminium3sheet_text.txt')
#print(get_varied().get_activity_err('C:\\Users\\nikit\\+]t5]Documents\\Particle phys project\\IV_new\\lead.txt'))
#plot_data().plot_thick_activity('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\lead2.txt')
#print(get_density().get_pmV('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadblock.txt'))
#print(get_av_density().get_p_av('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadsheet.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadblock.txt', 0, 1))
#print(get_thick_activityb().get_activities('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\lead.txt'))
#print(get_pts().get_pt('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\lead.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadsheet.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadblock.txt'))
#print(plot_data().plot_pT_A('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\Al.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\Al_sheet.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadblock.txt','Pb'))
#x=(data_table().plot_table('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\lead.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadsheet.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadblock.txt'))
(table_a().write_table('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\brick_als.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\bricks.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\Al_sheet.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\brick_al_table.txt'))
#(table_a().write_table('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\brick_steels.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\bricks.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\steel.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\brick_steels_table.txt'))


#(plot_data().plot_pT_A('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\woods.txt','C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\wood.txt', 'C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\leadblock.txt', 'Steel'))











#f=open('C:\\Users\\nikit\\Documents\\Particle phys project\\IV_new\\pb_lead.txt','w')
#for a in x:
 #   f.write(str(a).replace('[','').replace(']','').replace(',','').replace("'",'')+'\n' )
#f.close() 

#from math import log10, floor
#def round_to_1(x):
 #   return round(x, -int(floor(log10(abs(x)))))

#print(round_to_1(132))
#x=0.00132
#y=round(x, 2-int(floor(log10(abs(x))))-1)
#print(y)

