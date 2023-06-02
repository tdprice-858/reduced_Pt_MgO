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
                    print(r_eff)
                with open(subdir + '/report.txt', 'r') as file:
                    degeneracy = [float(line.split()[-1]) for line in file if 'degen' in line]
                    print(degeneracy)
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
                print(overall_tag_list)
                for count, value in enumerate(r_eff):
                    # Change value < 3.2 if looking at Jacs paper
                    if value < 3.2 and nlegs_list[count]==2:
                        re = value
                        r = r_opt[count]
                        alpha_1.append(r / re)
                        num_1_paths += 1*degeneracy[count]
                        print('degeneracy',degeneracy[count])
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
                exafs_dict[str(subdir)]['avg\nalpha_1'] = [f"{round(avg_alpha_1, 2)}\n{num_1_paths} paths"]
                exafs_dict[str(subdir)]['avg\nalpha_2'] = [f"{round(avg_alpha_2, 2)}\n{num_2_paths} paths"]
                exafs_dict[str(subdir)]['avg\nalpha_3'] = [f"{round(avg_alpha_3, 2)}\n{num_3_paths} paths"]
                #exafs_dict[str(subdir)]['del_r1'] = [del_r1]
                #exafs_dict[str(subdir)]['del_r2'] = [del_r2]
                #exafs_dict[str(subdir)]['del_r3'] = [del_r3]
                exafs_dict[str(subdir)]['sig2_2'] = [f"{'%.2E' % Decimal(float((sig2_2)))}\n{num_sig2_paths} paths"]
                exafs_dict[str(subdir)]['sig2_3'] = [f"{'%.2E' % Decimal(float((sig2_3)))}\n{num_sig3_paths} paths"]
                exafs_dict[str(subdir)]['sig2_4'] = [f"{'%.2E' % Decimal(float((sig2_4)))}\n{num_sig4_paths} paths"]
                exafs_dict[str(subdir)]['sig2_5'] = [f"{'%.2E' % Decimal(float((sig2_5)))}\n{num_sig5_paths} paths"]
                exafs_dict[str(subdir)]['sig2_6'] = [f"{'%.2E' % Decimal(float((sig2_6)))}\n{num_sig6_paths} paths"]
#############%%%% add variable

    return exafs_dict

os.chdir('/Users/tdprice/Desktop/pt_mgo_ethylene/\
s100_sub0-Mg-vac_sub1/')
root_dir = os.getcwd()
exafs_dict = {}
exafs_dict = get_exafs_data(exafs_dict, root_dir)

new_dict = sorted(exafs_dict.items(), key=lambda x: x[1]['red \u03C72'], reverse=False)

#Because new_dict is actually a list, we need to make a new list
#sorted_dict = {}
#for count, item in enumerate(new_dict):
#    sorted_dict[f"{new_dict[count][0]}"] = new_dict[count][1]
#print(sorted_dict)
sorted_dict = dict(new_dict)
with open('s100_sub0-Mg-vac_sub1.txt', 'w') as f:
    for title, keys in sorted_dict.items():
            print(title)
            #print(keys)
            #if float(sorted_dict[f"{title}"]['sig2_2'][0].split()[0]) > 0.0001 and float(sorted_dict[f"{title}"]['sig2_3'][0].split()[0]) > 0.0001:
            #if 'H_ad' in title:
            #print(title.split('/')[-1])
            #print(tabulate(keys, headers='keys', tablefmt='fancy_grid'))
            #title = color.BOLD + f"{title.split('/')[-1]}" + color.END + "\n"
            #print(title)
            f.write(f"{title.split('/')[-1]} \n")
            f.write(f"{tabulate(keys, headers='keys', tablefmt='fancy_grid')} \n")


#os.chdir('/Users/tdprice/Desktop/pt_mgo_ethylene/stable_hydrogen_structures_3_categories/3_cats_fix_params/03_2_ad_hy01_ot_pt_ot_vac/')
#paths = read_paths()