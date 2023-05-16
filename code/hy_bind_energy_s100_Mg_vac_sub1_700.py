from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from ase.visualize import view
from ase.visualize.plot import plot_atoms
import ase
import time

start_time = time.perf_counter()

db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/updated.db')

#Empty list for data
h_1ad_surf = []
h_2ad_surf = []
h_3ad_surf = []
h_4ad_surf = []


h_2ad_surf_subsurf = []

h_1ad_subsurf = []
h_2ad_subsurf = []


for row in db.select(convergence=True):

    if '02_pt-mgo-ethylene/01_bare/opt_PBE_400_221' in row.path:
        bare_energy = row.energy
        print(bare_energy)
        print(row.path)
    elif '19_100_PtMgO_2_sub_hy' in row.path:
        h_2ad_subsurf.append(row.energy)
        atoms = row.toatoms()
        path = row.path
        energy = row.energy
    elif '02_1_ad_hy/01_no_surf_atoms_constrained' in row.path:
        h_1ad_surf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(path)
        #print(row.energy)
        #print(f"{path} \n {energy}")
    elif '02_pt-mgo-ethylene/03_2_ad_hy' in row.path:
        h_2ad_surf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(f"{path} \n {energy}")
    elif '04_3_ad_hy' in row.path:
        h_3ad_surf.append(row.energy)
    elif '05_4_ad_hy' in row.path:
        h_4ad_surf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(f"{path} \n {energy}")
    elif '09_sub_hy' in row.path\
            and not '2_sub_hy' in row.path:
        h_1ad_subsurf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(f"{path} \n {energy}")
    elif '2_sub_hy' in row.path:
        h_2ad_surf_subsurf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(f"{path} \n {energy}")
    elif '01_hydrogen' in row.path:
        H2_energy = row.energy
        print(H2_energy)

h1_binding_energy = np.array(h_1ad_surf)
h2_binding_energy = np.array(h_2ad_surf)
h3_binding_energy = np.array(h_3ad_surf)
h4_binding_energy = np.array(h_4ad_surf)
h1_subsurf_binding_energy = np.array(h_1ad_subsurf)
h2_subsurf_binding_energy = np.array(h_2ad_subsurf)
h2_surf_subsurf_binding_energy = np.array(h_2ad_surf_subsurf)

bare_surf = np.array(bare_energy)

hydrogen_energy = np.array(H2_energy)
print(bare_surf, 'bare surf')
print(hydrogen_energy, 'Hydrogen Energy')

h1_binding_energy_per_h = (sorted(h1_binding_energy) - bare_surf -  0.5*hydrogen_energy)
h2_binding_energy_per_h = (sorted(h2_binding_energy) - bare_surf - hydrogen_energy)/2
h3_binding_energy_per_h = (sorted(h3_binding_energy) - bare_surf -  (3/2)*hydrogen_energy)/3
h4_binding_energy_per_h = (sorted(h4_binding_energy) - bare_surf -  2*hydrogen_energy)/4
h1_subsurf_binding_energy_per_h = (sorted(h1_subsurf_binding_energy) - bare_surf -  0.5*hydrogen_energy)
h2_subsurf_binding_energy_per_h = (sorted(h2_subsurf_binding_energy) - bare_surf - hydrogen_energy)/2
h2_surf_subsurf_binding_energy_per_h = (sorted(h2_surf_subsurf_binding_energy) - bare_surf - hydrogen_energy)/2


print(h1_binding_energy_per_h)
x1 = np.arange(len(h1_binding_energy_per_h))
x2 = np.arange(len(h2_binding_energy_per_h)) + x1[-1] +1
x3 = np.arange(len(h3_binding_energy_per_h)) + x2[-1] +1
x4 = np.arange(len(h4_binding_energy_per_h)) + x3[-1] +1
x5 = np.arange(len(h1_subsurf_binding_energy_per_h)) + x4[-1] +1
x6 = np.arange(len(h2_subsurf_binding_energy_per_h)) + x5[-1] +1
x7 = np.arange(len(h2_surf_subsurf_binding_energy_per_h)) + x6[-1] +1


plt.bar(x1,h1_binding_energy_per_h, color='r',
        edgecolor='grey', label='1H* surf')
plt.bar(x2,h2_binding_energy_per_h, color='b',
        edgecolor='grey', label='2H* surf')
plt.bar(x3 , h3_binding_energy_per_h, color='y',
        edgecolor='grey', label='3H* surf')
plt.bar(x4, h4_binding_energy_per_h, color='c',
        edgecolor='grey', label='4H* surf')
plt.bar(x5 , h1_subsurf_binding_energy_per_h, color='g',
        edgecolor='grey', label='H* sub')
plt.bar(x6 , h2_subsurf_binding_energy_per_h, color='m',
        edgecolor='grey', label='2H* sub')
plt.bar(x7 , h2_surf_subsurf_binding_energy_per_h, color='r',
        edgecolor='grey', label='1H* surf 1H* sub')

plt.xlabel('Configuration', fontweight='bold', fontsize=11)
plt.ylabel('Binding energy per Hydrogen eV', fontweight='bold', fontsize=11)
plt.title('H* adsorption on S100_Mg_vac_sub1_700', fontweight='bold', fontsize=12)
plt.legend()
plt.show()

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"The elapsed time was {elapsed_time} seconds")