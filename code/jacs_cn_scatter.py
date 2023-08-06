import numpy as np
from ase.neighborlist import natural_cutoffs, NeighborList
from ase.io import read
from ase.visualize import view
import matplotlib.pyplot as plt
from ase.db import connect

from ase.neighborlist import natural_cutoffs, NeighborList, mic
from ase.io import read
from ase.visualize import view
import numpy as np
from tabulate import tabulate
from matplotlib.ticker import MaxNLocator


def nearest_neighbor(atoms, central_atom, neigh_cutoff, gui=True):
    """
    Parameters
    ----------
    atoms_path : string
        path to cif, traj, xml, CONTCAR ... file
        ase atoms object

    central_atom : string
        central atom atomic symbol

    neigh_cutoff : float
        Cutoff distance for including neighbors of central atom

    gui : boolean
        Opens up ase gui of the nearest neighbor object.
        Default is set to True.

    Returns
    ----------
    """

    atoms = atoms
    pt_index = [a.index for a in atoms if a.symbol == central_atom]
    cutoff = natural_cutoffs(atoms)
    cutoff[-1] = neigh_cutoff

    # Problem: following line  will generate two Pt atoms
    nl = NeighborList(cutoff, bothways=True, self_interaction=True)

    # assign labels to all the neighbors in a list
    nl.update(atoms)
    neigh = nl.get_neighbors(pt_index[0])[0]
    atoms = atoms[neigh]

    mg_cn = []
    o_cn = []

    # Remove duplicate Pt
    for atom in atoms:
        if atom.symbol == central_atom:
            del atoms[[atom.index]]
            break

    for atom in atoms:
        if atom.symbol == central_atom:
            c_index = atom.index

    atomic_symbols = np.unique([a.symbol for a in atoms if a.index != c_index])
    neighbor_dict = {}
    stats = {}

    for atom in atomic_symbols:
        indices = [a.index for a in atoms if (a.index != c_index and a.symbol == atom)]
        distances = atoms.get_distances(c_index, indices, mic=True)
        distances = [round(distance, 3) for distance in distances]
        mean = round(np.mean(distances), 3)
        std = round(np.std(distances), 3)
        max = round(np.max(distances), 3)
        min = round(np.min(distances), 3)
        r = round(max - min, 3)
        neighbor_dict[atom] = distances
        neighbor_dict[f"{atom} stats"] = \
            [f"mean = {mean}", f"std = {std}", f"max = {max}", f"min = {min}", f"range = {r}"]
        stats[atom] = [mean, std, max, min, r]
    num_Mg_neigh = len([a.index for a in atoms if a.symbol == 'Mg'])
    num_O_neigh = len([a.index for a in atoms if a.symbol == 'O'])
    mg_cn.append(num_Mg_neigh)
    o_cn.append(num_O_neigh)
    # Visualization of nearest neighbors
    if gui:
        view(atoms)
    return neighbor_dict, stats, num_Mg_neigh, num_O_neigh

db = connect('/Users/tdprice/Desktop/pt_mgo_ethylene/vacancy_study/s100_sub1_2ox_vac_2mg_vac/updated.db')

mg_cn = []
o_cn = []
for row in db.select(convergence=True):
    if 'Pt' in row.formula and 'C' not in row.formula:
        atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
        if num_Mg == 13:
            continue
        mg_cn.append(num_Mg)
        o_cn.append(num_O)


        #print(row.facet)
        '''if row.facet == 's310':
            atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
            if num_Mg < 6:
                continue
            mg_cn_310.append(num_Mg)
            o_cn_310.append(num_O)
            print(row.facet)
            if num_Mg == 11 and num_O == 6:
                view(row.toatoms())
                atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=True)
        elif row.facet == 's100-Mg-vac':
            atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
            mg_cn_vac.append(num_Mg)
            o_cn_vac.append(num_O)
        else:

            atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
            mg_cn_100.append(num_Mg)
            o_cn_100.append(num_O)'''

'''for row in db.select(convergence=True):
    if 'Pt' in row.formula:
        atoms = row.toatoms()
        pt_index = [a.index for a in atoms if a.symbol == 'Pt']
        cutoff = natural_cutoffs(atoms)
        #print(cutoff)
        #The problem with the following line is that it will generate two Pt atoms in the file traj if self_interaction = True
        nl = NeighborList(cutoff, bothways=True, self_interaction=False)
        # assign labels to all the neighbors in a list
        nl.update(atoms)
        neigh = nl.get_neighbors(pt_index[0])[0]
        atoms = atoms[neigh]
        num_Mg_neigh = len([a.index for a in atoms if a.symbol == 'Mg'])
        num_O_neigh = len([a.index for a in atoms if a.symbol == 'O'])
        if num_O_neigh < 5:
            #view(row.toatoms())
            continue
        mg_cn.append(num_Mg_neigh)
        o_cn.append(num_O_neigh)'''



mg_cn_vac = []
o_cn_vac = []
mg_cn_310 = []
o_cn_310 = []
mg_cn_100 = []
o_cn_100 = []

db = connect('/Users/tdprice/Desktop/pt_mgo_ethylene/pt_mgo.db')
for row in db.select():
    if 'Pt' in row.formula and 'C' not in row.formula:
        if row.facet == 's310':
            atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
            if num_Mg < 6:
                continue
            mg_cn_310.append(num_Mg)
            o_cn_310.append(num_O)
            print(row.facet)
            if num_Mg == 11 and num_O == 6:
                view(row.toatoms())
                atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=True)
        elif row.facet == 's100-Mg-vac':
            atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
            mg_cn_vac.append(num_Mg)
            o_cn_vac.append(num_O)
        else:

            atom_dict, stats, num_Mg, num_O = nearest_neighbor(row.toatoms(), 'Pt', 1.6, gui=False)
            mg_cn_100.append(num_Mg)
            o_cn_100.append(num_O)

k = 4.2
h = 10.6
b = k * 0.2
a = h * 0.2

def ellipse(x, h, k, a, b):
    #top
    print(x)
    y_top = k + b * np.sqrt(1 - np.square(x - h) / np.square(a))
    print(y_top)
    y_bottom = k - b * np.sqrt(1 - np.square(x - h) / np.square(a))
    print(y_bottom)
    return y_top, y_bottom

x_range = np.arange(h-a, h+a, 0.01)
y_top, y_bottom = ellipse(x_range, h, k, a, b)
y_top[0] = k
y_bottom[0] = k

k_pristine = 5.6
h_pristine = 11.1
b = k_pristine * 0.2
a = h_pristine * 0.2

x_range_pristine = np.arange(h_pristine-a, h_pristine+a, 0.01)
y_top_pristine, y_bottom_pristine = ellipse(x_range_pristine, h_pristine, k_pristine, a, b)
y_top_pristine[0] = k_pristine
y_bottom_pristine[0] = k_pristine

#Making a ticked box for the range of CN's from EXAFS data
#plt.style.use('seaborn')
fig, ax = plt.subplots()

pt_O_range_pristine = [5, 6]
pt_Mg_range_pristine = [9, 12]

pt_O_range_reduced = [4, 5]
pt_Mg_range_reduced = [9, 12]

#ax.hlines(pt_O_range_reduced, pt_Mg_range_reduced[0], pt_Mg_range_reduced[-1],
#           linestyles='--', label='Reduced', colors='b')
#ax.vlines(pt_Mg_range_reduced, pt_O_range_reduced[0], pt_O_range_reduced[-1],
#           linestyles='--', colors='b')
#ax.fill_between(pt_Mg_range_reduced, pt_O_range_reduced[0],
#                 pt_O_range_reduced[-1], facecolor='blue', alpha=0.1)

#ax.hlines(pt_O_range_pristine, pt_Mg_range_pristine[0], pt_Mg_range_pristine[-1],
#           linestyles='-.', label='Pristine', colors='r')
#ax.vlines(pt_Mg_range_pristine, pt_O_range_pristine[0], pt_O_range_pristine[-1],
#           linestyles='-.', colors='r')
#ax.fill_between(pt_Mg_range_pristine, pt_O_range_pristine[0],
#                 pt_O_range_pristine[-1], facecolor='red', alpha=0.1)

#ax.plot(x_range, y_top)
#ax.plot(x_range, y_bottom)
ax.fill_between(x_range, y_top, y_bottom,
                facecolor='blue', alpha=0.3)
ax.scatter(h, k, marker='*', color='yellow', s=150)
ax.fill_between(x_range_pristine, y_top_pristine, y_bottom_pristine,
                facecolor='red', alpha=0.3)
ax.scatter(h_pristine, k_pristine, marker='*', color='yellow', s=150)
ax.scatter(mg_cn, o_cn, label='Vacancy study', marker='D', color='red', s=100)
ax.scatter(mg_cn_vac, o_cn_vac, label='[100]-Mg-vac', marker= 's' ,color='black')
ax.scatter(mg_cn_310, o_cn_310, label='[310]',marker='^' , color='green')
ax.scatter(mg_cn_100, o_cn_100, label='[100]', color='purple')
unexplored_points = [[10,6], [10,5], [10,4], [11,4], [12,4]]
unexplored_points = [[10,6], [12,4]]
i=0
for points in unexplored_points:
    if i==0:
        ax.scatter(points[0], points[1], color='black', label='Unexplored',
               marker='x', s=75)
        i+=1
    ax.scatter(points[0], points[1], color='black',
               marker='x', s=75)

ax.set_title('Mg and O Coordination numbers', fontsize='18')
ax.set_xlabel('Mg CN', fontsize='14')
ax.set_ylabel('O CN', fontsize='14')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.tick_params(axis='both', which='major', labelsize=12)
ax.legend(fontsize='10')
plt.show()
#view(atoms)