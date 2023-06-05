from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from ase.visualize import view
from ase.visualize.plot import plot_atoms
import ase
import time

start_time = time.perf_counter()

db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
27_s100-Mg-vac_sub1/mg_vac_sub0/updated.db')

#Empty list for data
h_1ad_surf = []
h_2ad_surf = []
h_3ad_surf = []
h_4ad_surf = []


h_2ad_surf_subsurf = []

h_1ad_subsurf = []
h_2ad_subsurf = []

H2_ad = []


for row in db.select(convergence=True):

    if 'bare' in row.path:
        bare_energy = row.energy
        print(bare_energy)
        print(row.path)
    elif '19_100_PtMgO_2_sub_hy' in row.path:
        h_2ad_subsurf.append(row.energy)
        atoms = row.toatoms()
        path = row.path
        energy = row.energy
    elif '01_1H_ad' in row.path:
        h_1ad_surf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(path)
        #print(row.energy)
        #print(f"{path} \n {energy}")
    elif '02_2H_ad' in row.path:
        h_2ad_surf.append(row.energy)
        path = row.path
        energy = row.energy

        print(f"{path} \n {energy}")
    elif '03_3H_ad' in row.path:
        h_3ad_surf.append(row.energy)
    elif '04_4H_ad' in row.path:
        h_4ad_surf.append(row.energy)
        path = row.path
        energy = row.energy
        #print(f"{path} \n {energy}")```

h1_binding_energy = np.array(h_1ad_surf)
h2_binding_energy = np.array(h_2ad_surf)
h3_binding_energy = np.array(h_3ad_surf)
h4_binding_energy = np.array(h_4ad_surf)
#h1_subsurf_binding_energy = np.array(h_1ad_subsurf)
#h2_subsurf_binding_energy = np.array(h_2ad_subsurf)
#h2_surf_subsurf_binding_energy = np.array(h_2ad_surf_subsurf)
#H2_binding_energy = np.array(H2_ad)

bare_surf = np.array(bare_energy)

hydrogen_energy = np.array(-6.5041754)
print(bare_surf, 'bare surf')
print(hydrogen_energy, 'Hydrogen Energy')

h1_binding_energy_per_h = (sorted(h1_binding_energy) - bare_surf -  0.5*hydrogen_energy)
h2_binding_energy_per_h = (sorted(h2_binding_energy) - bare_surf - hydrogen_energy)#/2
h3_binding_energy_per_h = (sorted(h3_binding_energy) - bare_surf -  (3/2)*hydrogen_energy)#/3
h4_binding_energy_per_h = (sorted(h4_binding_energy) - bare_surf -  2*hydrogen_energy)#/4
#h1_subsurf_binding_energy_per_h = (sorted(h1_subsurf_binding_energy) - bare_surf -  0.5*hydrogen_energy)
#h2_subsurf_binding_energy_per_h = (sorted(h2_subsurf_binding_energy) - bare_surf - hydrogen_energy)#/2
#h2_surf_subsurf_binding_energy_per_h = (sorted(h2_surf_subsurf_binding_energy) - bare_surf - hydrogen_energy)#/2
#H2_binding_energy_per_molecule = (sorted(H2_binding_energy) - bare_surf - hydrogen_energy)

x1 = np.arange(len(h1_binding_energy_per_h))
x2 = np.arange(len(h2_binding_energy_per_h)) + x1[-1] +1
x3 = np.arange(len(h3_binding_energy_per_h)) + x2[-1] +1
x4 = np.arange(len(h4_binding_energy_per_h)) + x3[-1] +1
#x5 = np.arange(len(h1_subsurf_binding_energy_per_h)) + x4[-1] +1
#x6 = np.arange(len(h2_subsurf_binding_energy_per_h)) + x5[-1] +1
#x7 = np.arange(len(h2_surf_subsurf_binding_energy_per_h)) + x6[-1] +1
#x8 = np.arange(len(H2_binding_energy_per_molecule)) + x7[-1] +1


plt.bar(x1,h1_binding_energy_per_h, color='r',
        edgecolor='grey', label='1H* surf')
plt.bar(x2,h2_binding_energy_per_h, color='b',
        edgecolor='grey', label='2H* surf')
plt.bar(x3 , h3_binding_energy_per_h, color='y',
        edgecolor='grey', label='3H* surf')
plt.bar(x4, h4_binding_energy_per_h, color='c',
        edgecolor='grey', label='4H* surf')
#plt.bar(x5 , h1_subsurf_binding_energy_per_h, color='g',
#        edgecolor='grey', label='H* sub')
#plt.bar(x6 , h2_subsurf_binding_energy_per_h, color='m',
#        edgecolor='grey', label='2H* sub')
#plt.bar(x7 , h2_surf_subsurf_binding_energy_per_h, color='r',
#        edgecolor='grey', label='1H* surf 1H* sub')
#plt.bar(x8 , H2_binding_energy_per_molecule, color='b',
#        edgecolor='grey', label='H2* surf')

plt.xlabel('Configuration', fontweight='bold', fontsize=11)
plt.ylabel('Binding energy eV', fontweight='bold', fontsize=11)
plt.title('H* adsorption on Pt/MgO-sub0-Mg-Vac', fontweight='bold', fontsize=12)
plt.legend()
plt.show()

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"The elapsed time was {elapsed_time} seconds")