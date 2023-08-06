'''
This script is intended to extract information from QuantEXAFS data.

The first part goes through each structure folder and retrieves the goodness of fit parameters.
The second part plots bar charts of the above data
'''

import os, sys, shutil
import numpy as np
from quant_exafs_utils import get_exafs_data

# Where you want to execute code
#os.chdir('/Users/tdprice/Desktop/pt_mgo_ethylene/exafs_fitting_jacs_pap_pristine_data')
os.chdir('/Users/tdprice/Desktop/pt_mgo_ethylene/exafs_fitting_jacs_pap_reduced_data')
rootdir = os.getcwd()

#Sorting dictionary, and confirming
exafs_dict = {}
exafs_dict = get_exafs_data(exafs_dict, rootdir, sig_constraint=10**-30)

#Sorting dictionary in order of best to worst fit wrt. to red chi squre metric
new_dict = sorted(exafs_dict.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)
print(new_dict)


###########%##########
#  PLOTTING RESULTS
###########%########

# Import Library

import numpy as np
import matplotlib.pyplot as plt

# Define Data
s310_frechet = []
s310_red_chi = []
s310_r_factor = []
s100_mg_vac_frechet = []
s100_mg_vac_r_factor = []
s100_mg_vac_red_chi = []
s100_red_chi = []
s100_r_factor = []
s100_frechet = []


#extract data
for data in new_dict:
    structure = data[0].split('/')[-1]
    dict_data = data[1]
    #print(f"{structure} structure, {dict_data}")
    if 's310' in data[0].split('/')[-1] and data[-1]['red_chi_square'] < 100:
        s310_r_factor.append(data[1]['r_factor'])
        s310_frechet.append(data[1]['frechet'])
        s310_red_chi.append(data[1]['red_chi_square'])
        print(f"{structure} structure, {dict_data}")
    elif 's100' in data[0].split('/')[-1] and not 'Mg-vac' in data[0].split('/')[-1] and data[-1]['red_chi_square'] < 100:
        s100_r_factor.append(data[1]['r_factor'])
        s100_frechet.append(data[1]['frechet'])
        s100_red_chi.append(data[1]['red_chi_square'])
        print(f"{structure} structure, {dict_data}")
    elif 's100-Mg-vac' in data[0].split('/')[-1] and data[-1]['red_chi_square'] < 100:
        s100_mg_vac_r_factor.append(data[1]['r_factor'])
        s100_mg_vac_frechet.append(data[1]['frechet'])
        s100_mg_vac_red_chi.append(data[1]['red_chi_square'])
        print(f"{structure} structure \n, {dict_data}")
    else:
        continue


x_s100 = np.arange(len(s100_frechet))
x_s100_Mg_vac = np.arange(len(s100_mg_vac_frechet)) + x_s100[-1] + 1
x_s310 = np.arange(len(s310_frechet)) + x_s100_Mg_vac[-1] + 1

# Create Plot

fig, ax1 = plt.subplots()
#fig , ax1, ax2= plt.figure(figsize = (10, 5))

ax1.set_xlabel('Configuration',fontweight='bold', fontsize=14)
ax1.set_ylabel('Reduced \u03C7 $^{2}$', color='black', fontsize=14)
ax1.bar(x_s100, s100_red_chi, color='red', label='[100]')
ax1.bar(x_s100_Mg_vac, s100_mg_vac_red_chi, color ='purple', label ='[100]-Mg-vac')
ax1.bar(x_s310, s310_red_chi, color ='orange', label ='[310]')

ax1.tick_params(axis='y')
plt.legend(fontsize= 12)

# Adding Twin Axes

ax2 = ax1.twinx()
ax2.set_ylabel('\u03B4 $_{F}$', color='blue', fontsize=14)
ax2.plot(x_s100, s100_frechet, color='blue')
ax2.plot(x_s100_Mg_vac, s100_mg_vac_frechet, color ='blue')
ax2.plot(x_s310, s310_frechet, color ='blue')
ax2.tick_params(axis='y')

plt.title('QuantEXAFS fits of JACs Database', fontweight='bold', fontsize=16)

# Show plot

plt.show()