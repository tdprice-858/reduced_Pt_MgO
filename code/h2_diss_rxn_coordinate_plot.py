import os,sys
import seaborn as sns
import matplotlib.pyplot as plt
from os import environ,sys
from ase import io
import ase.db
from ase.vibrations import Vibrations
import numpy as np
import pickle
import math
from ase.thermochemistry import HarmonicThermo
from scipy.optimize import fsolve
import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (6, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

#What is the following?
cm_inv2ev = 0.0001239842573

#* data means in can be in a tuple form
def fit_cubic(coeff,*data):
    data = data[0]
    #sys.exit()
    x = data[0]
    y = data[1]
    err = []
    a,b,c,d = coeff
    for val_x, val_y in zip(x,y):
        err.append(a*val_x**3 + b*val_x**2 + c*val_x + d - val_y)
    val_x = x[1] # mid value
    val_y = y[1]
    err.append(3*a*val_x**2 + 2*b*val_x + c ) # Derivative must be zero at the mid
    return (err)

#rxn_e = [0.26, 0.50, 0, 0.54, -0.49, -0.70]
    #0.29, -1.49 -1.68]
rxn_e = [0, 0.49, 0, 0.7, -0.34, -0.39]
index_ts = [1, 3, 6]#[3,5,7]



# plt.figure()
spacing = 0.5
width = 0.5
old_end = 0.0 - spacing
old_val = 0


my_color = 'k'


for i,val in enumerate(rxn_e):
    hori_line_left = old_end + spacing
    hori_line_right = hori_line_left + width
    if i > 0 and i not in index_ts and i not in [val+1 for val in index_ts]:
        # don't plot the first one. Also don't plot the ones corresponding to index_ts
        plt.plot([old_end, hori_line_left], [old_val, rxn_e[i]], '--', color=my_color, lw=0.5)

    if i in index_ts:
        h, = plt.plot((hori_line_left + hori_line_right) / 2, rxn_e[i], '*-', ms=8, color=my_color)
        # fit a ax3+bx2+cx+d = y to the three points
        x_left = hori_line_left - spacing
        x_right = hori_line_right + spacing
        x_mid = (hori_line_left + hori_line_right) / 2
        y_left = rxn_e[i - 1]
        y_right = rxn_e[i + 1]
        y_mid = rxn_e[i]
        assert val == rxn_e[i]
        x = [x_left, x_mid, x_right]
        y = [y_left, y_mid, y_right]
        # plt.plot(x,y,'ro-') # For testing

        coeff0 = np.array([1., 1., 1., 1.])
        data = [x, y]
        out = fsolve(fit_cubic, coeff0, args=data)
        a, b, c, d = out
        coeff = out
        assert np.linalg.norm(fit_cubic(coeff, data)) <= 1E-5
        curve_x = np.linspace(x_left, x_right, 100)
        curve_y = a * curve_x ** 3 + b * curve_x ** 2 + c * curve_x + d
        plt.plot(curve_x, curve_y, '-', color=my_color, lw=1)

    else:
        if len(index_ts) == 0:
            sys.exit()
            h, = plt.plot([hori_line_left, hori_line_right], [val, val], '-', color=my_color)
        else:
            plt.plot([hori_line_left, hori_line_right], [val, val], '-', color=my_color)

    old_val = val
    old_end = hori_line_right

    # For legenda
#    if i == 2:
#        list_h.append(h, )
#        if T == 0:
#            list_l.append('0 K')
#        else:
#            list_l.append('%s$^\circ$C' % T_deg_C)

    # For special
    # Basically, if the index exists in special_index, we need to get the
    # value of that special index using rel_special


    plt.xlabel('Reaction coordinate', fontsize=14)
    plt.ylabel('Gibbs free energy, eV', fontsize=14)
    #plt.legend(list_h, list_l)
    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.xaxis.set_ticks([])



print('DONE')
plt.tight_layout()
# plt.savefig('fig_80C.pdf',dpi=300)
plt.xlabel('Reaction coordinate', fontsize=14)
plt.ylabel('Gibbs free energy, eV', fontsize=14)
#plt.legend(list_h, list_l)
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.xaxis.set_ticks([])
# plt.savefig('fig_iso.pdf',dpi = 300 )


'''
print(list_volcano)
plt.figure()
plt.plot(T_range,np.array(list_volcano)[:,0],'ro--',label='bind_2no')
plt.plot(T_range,np.array(list_volcano)[:,1],'bo--',label='remove_o2')  
plt.legend() 
'''
'''#rxn_e = [0.26, 0.50, 0, 0.29, -1.49, -1.68]
rxn_e = [0, 0.49, 0, 0.47, -1.55, -1.58]
index_ts = [1, 3, 6]#[3,5,7]

# plt.figure()
spacing = 0.5
width = 0.5
old_end = 0.0 - spacing
old_val = 0


my_color = 'k'


for i,val in enumerate(rxn_e):
    hori_line_left = old_end + spacing
    hori_line_right = hori_line_left + width
    if i > 0 and i not in index_ts and i not in [val+1 for val in index_ts]:
        # don't plot the first one. Also don't plot the ones corresponding to index_ts
        plt.plot([old_end, hori_line_left], [old_val, rxn_e[i]], '--', color=my_color, lw=0.5)

    if i in index_ts:
        h, = plt.plot((hori_line_left + hori_line_right) / 2, rxn_e[i], '*-', ms=8, color=my_color)
        # fit a ax3+bx2+cx+d = y to the three points
        x_left = hori_line_left - spacing
        x_right = hori_line_right + spacing
        x_mid = (hori_line_left + hori_line_right) / 2
        y_left = rxn_e[i - 1]
        y_right = rxn_e[i + 1]
        y_mid = rxn_e[i]
        assert val == rxn_e[i]
        x = [x_left, x_mid, x_right]
        y = [y_left, y_mid, y_right]
        # plt.plot(x,y,'ro-') # For testing

        coeff0 = np.array([1., 1., 1., 1.])
        data = [x, y]
        out = fsolve(fit_cubic, coeff0, args=data)
        a, b, c, d = out
        coeff = out
        assert np.linalg.norm(fit_cubic(coeff, data)) <= 1E-5
        curve_x = np.linspace(x_left, x_right, 100)
        curve_y = a * curve_x ** 3 + b * curve_x ** 2 + c * curve_x + d
        plt.plot(curve_x, curve_y, '-', color=my_color, lw=1)

    else:
        if len(index_ts) == 0:
            sys.exit()
            h, = plt.plot([hori_line_left, hori_line_right], [val, val], '-', color=my_color)
        else:
            plt.plot([hori_line_left, hori_line_right], [val, val], '-', color=my_color)

    old_val = val
    old_end = hori_line_right

    # For legenda
#    if i == 2:
#        list_h.append(h, )
#        if T == 0:
#            list_l.append('0 K')
#        else:
#            list_l.append('%s$^\circ$C' % T_deg_C)

    # For special
    # Basically, if the index exists in special_index, we need to get the
    # value of that special index using rel_special


    plt.xlabel('Reaction coordinate', fontsize=14)
    plt.ylabel('Gibbs free energy, eV', fontsize=14)
    #plt.legend(list_h, list_l)
    ax = plt.gca()
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.xaxis.set_ticks([])

'''

print('DONE')
plt.tight_layout()
#plt.savefig('fig_80C.pdf',dpi=300)
plt.xlabel('Reaction coordinate: 120 \N{DEGREE SIGN}C', fontsize=14)
plt.ylabel('Gibbs free energy, eV', fontsize=14)
#plt.legend(list_h, list_l)
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
ax.axes.xaxis.set_ticks([])
#plt.savefig('fig_iso.pdf',dpi = 300 )
plt.show()
