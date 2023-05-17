import os

def get_exafs_data(exafs_dict, rootdir, sig_constraint=0.0001, sort=""):
    """"
    Function for making a dictionary of values from QuantEXAFS analysis.

    Parameters
    ----------
    exafs_dict: Dictionary
        Dictionary where you want data added. Can be blank or already have previous data.

    rootdir: Directory path
        Directory location of QuantEXAFS folders

    sig_constraint: Float
        Minimum value setting for sig2 fitting parameters.
        Currently this code is only constraining the sig2_2 and sig3_3 parameters as these are the Pt-O
        and Pt-Mg shells of my structures of interest.
    sort: string
        Allows dictionary to be sorted in increasing values of the selected key.
            keys:
                'red_chi_square'
                'frechet'
                'r_factor'

    Returns
    ---------
    if sort is set to '':
        exafs_dict: Dictionary
            Dictionary containing fitting parameters and goodness-of-fit data:
                keys:
                    'red_chi_square'
                    'frechet'
                    'r_factor'
                    'sig2_2'
                    'sig2_3'
                    'sig2_4'
                    'sig2_5'
                    'sig2_6'
                values:
                    Pulled from QuantEXAFS analysis report.txt and compare_curves.txt files.
    if sort is set to a value:
        returns a sorted list with the specified value sorted in increasing value.

    """
    # Generating file names in a directory tree and filtering out for desired paths
    for subdir, dirs, files in os.walk(rootdir, followlinks=True):
        if not subdir == rootdir and 'ind' not in subdir:
            if os.path.exists(subdir + '/report.txt'):
                with open(subdir + '/report.txt', 'r') as file:
                    r_factor = [line for line in file if 'r-factor' in line]
                with open(subdir + '/report.txt', 'r') as file:
                    red_chi_sq = [line for line in file if 'reduced chi_square' in line]
                with open(subdir + '/compare_curve.txt', 'r') as file:
                    frechet = [line for line in file if 'frechet' in line]
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
                    if float(sig2_2) < sig_constraint:
                        continue
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_3 = [line.split()[2] for line in file if 'sig2_3    ' in line]
                    sig2_3 = sig2_3[0]
                    if float(sig2_3) < sig_constraint:
                        continue
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_4 = [line.split()[2] for line in file if 'sig2_4    ' in line]
                    sig2_4 = sig2_4[0]
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_5 = [line.split()[2] for line in file if 'sig2_5    ' in line]
                    sig2_5 = sig2_5[0]
                with open(subdir + '/report.txt', 'r') as file:
                    sig2_6 = [line.split()[2] for line in file if 'sig2_6    ' in line]
                    sig2_6 = float(sig2_6[0])
                r = [float(v.split()[-1]) for v in r_factor]
                red = [float(j.split()[-1]) for j in red_chi_sq]
                fre = [float(c.split()[-1]) for c in frechet]
                exafs_dict[str(subdir)] = {}
                exafs_dict[str(subdir)]['r_factor'] = r[0]
                exafs_dict[str(subdir)]['red_chi_square'] = red[0]
                exafs_dict[str(subdir)]['frechet'] = fre[0]
                exafs_dict[str(subdir)]['sig2_2'] = [f"{sig2_2}"]
                exafs_dict[str(subdir)]['sig2_3'] = [f"{sig2_3}"]
                exafs_dict[str(subdir)]['sig2_4'] = [f"{sig2_4}"]
                exafs_dict[str(subdir)]['sig2_5'] = [f"{sig2_5}"]
                exafs_dict[str(subdir)]['sig2_6'] = [f"{sig2_6}"]
    if sort != '':
        exafs_dict = sorted(exafs_dict.items(), key=lambda x: x[1][sort], reverse=False)
    return exafs_dict


'''#testing
os.chdir('/Users/tdprice/Desktop/pt_mgo_ethylene/vacancy_study')

rootdir = os.getcwd()
exafs_dict = {}
exafs_dict = get_exafs_data(exafs_dict, rootdir, sort='red_chi_square')

print(exafs_dict)
print(type(exafs_dict))'''