'''This script pulls data from ase db
and plots H2 binding energy for various adsorption
sites on 700 site'''


from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
from ase.visualize import view
from ase.visualize.plot import plot_atoms
import time

start_time = time.perf_counter()

# Location of desired database
db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/updated.db')

# Empty list for data
'''H2_ad = [[row.energy, row.path.split('/')[-2]]
         for row in db.select(convergence=True)
         if '17_100_PtMgO_H2' in row.path]'''

H2_ad = []

# Loop to extract data from
for row in db.select(convergence=True):

    if '02_pt-mgo-ethylene/01_bare/opt_PBE_400_221' in row.path:
        bare_energy = row.energy
    elif '01_hydrogen' in row.path:
        H2_energy = row.energy
    elif '17_100_PtMgO_H2' in row.path:
        H2_ad.append([row.energy, row.path.split('/')[-2]])
        #H2_ad.append(row.energy)
    #    print(row.path.split('/')[-2])

H2_ad = sorted(H2_ad, key=itemgetter(0))
print(H2_ad)
H2_energies = [item[0] for item in H2_ad]
H2_labels = [item[1] for item in H2_ad]
H2_binding_energy = np.array(H2_energies)

#print(H2_binding_energy[:,0])

bare_surf = np.array(bare_energy)

hydrogen_energy = np.array(H2_energy)
print(bare_surf, 'bare surf')
print(hydrogen_energy, 'Hydrogen Energy')

H2_binding_energy_per_molecule = (H2_binding_energy - bare_surf - hydrogen_energy)

x = np.arange(len(H2_binding_energy_per_molecule))


plt.bar(x , H2_binding_energy_per_molecule, color='b',
        edgecolor='grey', label='H2* surf')

plt.xlabel('Configuration', fontweight='bold', fontsize=11)
plt.ylabel('Binding energy eV', fontweight='bold', fontsize=11)
plt.title('H\u2082* adsorption on Pt/MgO', fontweight='bold', fontsize=12)
plt.legend()
plt.show()

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"The elapsed time was {elapsed_time} seconds")