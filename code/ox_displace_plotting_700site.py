from tabulate import tabulate
import numpy as np
import sys, os
from itertools import islice
from decimal import Decimal


def get_exafs_data(exafs_dict, rootdir):
    # Generating file names in a directory tree and filtering out for desired paths
    for subdir, dirs, files in os.walk(rootdir, followlinks=True):
        # we don't want to include root dir and get_filter ensures that we have the desired opt directory
            if os.path.exists(subdir + '/report.txt'):
                with open(subdir + '/report.txt', 'r') as file:
                    del_e0 = [line for line in file if 'del_e0' in line]
                    del_e0 = del_e0[0].split()[2]
                with open(subdir + '/report.txt', 'r') as file:
                    del_r1 = [line for line in file if 'del_r1' in line]
                    del_r1 = del_r1[0].split()[2]
                with open(subdir + '/report.txt', 'r') as file:
                    del_r2 = [line for line in file if 'del_r2' in line]
                    del_r2 = del_r2[0].split()[2]
                with open(subdir + '/report.txt', 'r') as file:
                    del_r3 = [line for line in file if 'del_r3' in line]
                    del_r3 = del_r3[0].split()[2]
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_1 = [line.split()[2] for line in file if 'sig2_1    ' in line]
                    sig2_1 = sig2_1[0]
                    #if float(sig2_2) < 0.001:
                    #    continue
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_2 = [line.split()[2] for line in file if 'sig2_2    ' in line]
                    sig2_2 = sig2_2[0]
                    #if float(sig2_2) < 0.001:
                    #    continue
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_3 = [line.split()[2] for line in file if 'sig2_3    ' in line]
                    sig2_3 = sig2_3[0]
                    #if float(sig2_3) < 0.001:
                    #    continue
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_4 = [line.split()[2] for line in file if 'sig2_4    ' in line]
                    sig2_4 = sig2_4[0]
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_5 = [line.split()[2] for line in file if 'sig2_5    ' in line]
                    sig2_5 = sig2_5[0]
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_6 = [line.split()[2] for line in file if 'sig2_6    ' in line]
                    sig2_6 = float(sig2_6[0])
                with open(subdir + '/report.txt', 'r') as file:
                    r_factor = [line for line in file if 'r-factor' in line]
                with open(subdir + '/report.txt', 'r') as file:
                    red_chi_sq = [line for line in file if 'reduced chi_square' in line]
                with open(subdir + '/compare_curve.txt', 'r') as file:
                    frechet = [line for line in file if 'frechet' in line]
                with open(subdir + '/report.txt', 'r') as file:
                    r_opt = [float(line.split()[2]) for line in file if 'r     ' in line and ':=' in line]
                with open(subdir + '/report.txt', 'r') as file:
                    r_eff = [float(line.split()[-1]) for line in file if 'reff   ' in line]
                with open(subdir + '/report.txt', 'r') as file:
                    degeneracy = [float(line.split()[-1]) for line in file if 'degen' in line]
                overall_tag_list = []
                nlegs_list = []
                with open(subdir + '/paths.dat', 'r') as g:
                    for i, line in enumerate(g):
                        if 'index, nleg, degeneracy, r' in line:
                            nlegs_val = int(line.split()[1])
                            nlegs_list.append(nlegs_val)

                            tag_list = []
                            for lines in islice(g, 1, nlegs_val + 1):
                                tag_list.append(lines.split()[4].replace("'", ''))

                            overall_tag_list.append(tag_list)

                alpha_1 = []
                alpha_2 = []
                alpha_3 = []
                num_1_paths = 0
                num_2_paths = 0
                num_3_paths = 0
                num_sig1_paths = 0
                num_sig2_paths = 0
                num_sig3_paths = 0
                num_sig4_paths = 0
                num_sig5_paths = 0
                num_sig6_paths = 0
                with open(subdir + '/report.txt', 'r') as file:
                    i=0
                    for line in file:
                        if 'degen' in line:
                            deg = float(line.split()[-1])
                        if "'sig2_1'" in line:
                            num_sig1_paths += 1*deg
                        if "'sig2_2'" in line:
                            num_sig2_paths += 1*deg
                        if "'sig2_3'" in line:
                            num_sig3_paths += 1*deg
                        if "'sig2_4'" in line:
                            num_sig4_paths += 1*deg
                        if "'sig2_5'" in line:
                            num_sig5_paths += 1*deg
                        if "'sig2_6'" in line:
                            num_sig6_paths += 1*deg
                for count, value in enumerate(r_eff):
                    # Change value < 3.2 if looking at Jacs paper
                    if value < 3.2 and nlegs_list[count]==2:
                        re = value
                        r = r_opt[count]
                        alpha_1.append(r / re)
                        num_1_paths += 1*degeneracy[count]
                    elif value > 3.2 and value < 4.0:
                        re = value
                        r = r_opt[count]
                        alpha_2.append(r / re)
                        num_2_paths += 1*degeneracy[count]
                    else:
                        re = value
                        r = r_opt[count]
                        alpha_3.append(r / re)
                        num_3_paths += 1*degeneracy[count]

                total_paths = count + 1
                avg_alpha_1 = np.average(alpha_1)
                avg_alpha_2 = np.average(alpha_2)
                avg_alpha_3 = np.average(alpha_3)
                std_alpha_1 = np.std(alpha_1)
                std_alpha_2 = np.std(alpha_2)
                std_alpha_3 = np.std(alpha_3)



                r = [float(v.split()[-1]) for v in r_factor]
                red = [float(j.split()[-1]) for j in red_chi_sq]
                fre = [float(c.split()[-1]) for c in frechet]

                exafs_dict[str(subdir)] = {}
                exafs_dict[str(subdir)]['r_factor'] = [round(r[0],2)]
                exafs_dict[str(subdir)]['red \u03C72'] = [round(red[0], 2)]
                exafs_dict[str(subdir)]['frechet'] = [round(fre[0], 2)]
                exafs_dict[str(subdir)]['del_e0'] = [round(float(del_e0), 2)]
                exafs_dict[str(subdir)]['avg\nalpha_1'] = [round(avg_alpha_1, 2)]
                exafs_dict[str(subdir)]['avg\nalpha_2'] = [round(avg_alpha_2, 2)]
                exafs_dict[str(subdir)]['avg\nalpha_3'] = [round(avg_alpha_3, 2)]
                #exafs_dict[str(subdir)]['del_r1'] = [del_r1]
                #exafs_dict[str(subdir)]['del_r2'] = [del_r2]
                #exafs_dict[str(subdir)]['del_r3'] = [del_r3]
                exafs_dict[str(subdir)]['sig2_1'] = [float((sig2_1))]
                exafs_dict[str(subdir)]['sig2_2'] = [float((sig2_2))]
                exafs_dict[str(subdir)]['sig2_3'] = [float((sig2_3))]
                exafs_dict[str(subdir)]['sig2_4'] = [float((sig2_4))]
                exafs_dict[str(subdir)]['sig2_5'] = [float((sig2_5))]
                exafs_dict[str(subdir)]['sig2_6'] = [float((sig2_6))]
#############%%%% add variable

    return exafs_dict

os.chdir('/Users/tdprice/Desktop/pt_mgo_ethylene/oxygen_distance_study/700_site')
root_dir = os.getcwd()
exafs_dict = {}
exafs_dict = get_exafs_data(exafs_dict, root_dir)

new_dict = sorted(exafs_dict.items(), key=lambda x: x[0], reverse=False)

#Because new_dict is actually a list, we need to make a new list
#sorted_dict = {}
#for count, item in enumerate(new_dict):
#    sorted_dict[f"{new_dict[count][0]}"] = new_dict[count][1]
#print(sorted_dict)
sorted_dict = dict(new_dict)
#print(sorted_dict)
o_dist = [round(float(path[0].split('/')[-1].split('_')[-1]),2) for path
    in sorted_dict.items()]
r_factor = [path[1]['r_factor'] for path
    in sorted_dict.items()]
red_chi = [path[1]['red \u03C72'] for path
    in sorted_dict.items()]
frechet = [path[1]['frechet'] for path
    in sorted_dict.items()]
alpha_1 = [path[1]['avg\nalpha_1'] for path
    in sorted_dict.items()]
alpha_2 = [path[1]['avg\nalpha_2'] for path
    in sorted_dict.items()]
alpha_3 = [path[1]['avg\nalpha_3'] for path
    in sorted_dict.items()]
sig2_1 = [path[1]['sig2_1'] for path
    in sorted_dict.items()]
sig2_2 = [path[1]['sig2_2'] for path
    in sorted_dict.items()]
sig2_3 = [path[1]['sig2_3'] for path
    in sorted_dict.items()]
sig2_4 = [path[1]['sig2_4'] for path
    in sorted_dict.items()]
sig2_5 = [path[1]['sig2_5'] for path
    in sorted_dict.items()]
sig2_6 = [path[1]['sig2_6'] for path
    in sorted_dict.items()]

import matplotlib.pyplot as plt
import numpy as np


print(sig2_1)

# plot
fig, ax = plt.subplots()

# Optimized Pt-O distance without hydrogen
Pt_O_opt_dist =2.041
# Optimized Pt-O distance with 2 hydrogen (OH group) most stable structure
Pt_O_H_opt_dist = 2.965
ax.axvline(x=Pt_O_opt_dist, label= 'Opt. Pt-O Dist.', color='r' )
ax.axvline(x=Pt_O_H_opt_dist, label= 'Opt. Pt-O-H Dist.', color='c')
ax.scatter(o_dist, sig2_1, label='sig2_1 (Pt-'r'$\delta$ O)')
ax.scatter(o_dist, sig2_2, label='sig2_2 (Pt-O)')
ax.scatter(o_dist, sig2_3, label='sig2_3 (Pt-Mg)')
ax.set_title('700 site: sig2_* vs. O_dist')
plt.xlabel('O_dist (Angstrom)')
plt.ylabel('sig2_1')
plt.legend()


plt.show()



fig, ax = plt.subplots()
ax.axvline(x=Pt_O_opt_dist, label= 'Opt. Pt-O Dist.', color='r' )
ax.axvline(x=Pt_O_H_opt_dist, label= 'Opt. Pt-O-H Dist.', color='c')
ax.scatter(o_dist, r_factor)
ax.set_title('r_factor vs. O_dist')
plt.xlabel('O_dist (Angstrom)')
plt.ylabel('r_factor')
plt.legend()

plt.show()

fig, ax = plt.subplots()
ax.axvline(x=Pt_O_opt_dist, label= 'Opt. Pt-O Dist.', color='r' )
ax.axvline(x=Pt_O_H_opt_dist, label= 'Opt. Pt-O-H Dist.', color='c')
ax.scatter(o_dist, red_chi)
ax.set_title('red \u03C72 vs. O_dist')
plt.xlabel('O_dist (Angstrom)')
plt.ylabel('red \u03C72')
plt.legend()

plt.show()

fig, ax = plt.subplots()
ax.axvline(x=Pt_O_opt_dist, label= 'Opt. Pt-O Dist.', color='r' )
ax.axvline(x=Pt_O_H_opt_dist, label= 'Opt. Pt-O-H Dist.', color='c')
ax.scatter(o_dist, frechet)
ax.set_title('Frechet vs. O_dist')
plt.xlabel('O_dist (Angstrom)')
plt.ylabel('frechet')
plt.legend()

plt.show()