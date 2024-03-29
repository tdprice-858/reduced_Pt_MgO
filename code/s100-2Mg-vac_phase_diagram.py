from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from pmutt.statmech import StatMech, presets
from ase.build import molecule
from pprint import pprint

db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/20_100_PtMgO_mg_vac/2_surf_mg_vac/updated.db')

#for row in db.select(convergence=True):
#    print(row.path)


h1ad_low_pot_energy = 10000000
h2ad_low_pot_energy = 10000000
h3ad_low_pot_energy = 10000000
h4ad_low_pot_energy = 10000000
h1subad_low_pot_energy = 10000000
h2subad_low_pot_energy = 10000000
h2subad_low_pot_energy2 =10000000
for row in db.select():
    #print(row.path)
    if 'bare' in row.path:
        bare_energy = row.energy
    if '01_1H_ad' in row.path:
        if row.energy < h1ad_low_pot_energy:
            h1ad_low_pot_energy = row.energy
            h1ad_path = row.path
    if '02_2H_ad' in row.path:
        if row.energy < h2ad_low_pot_energy:
            h2ad_low_pot_energy = row.energy
            h2ad_path = row.path
    if '03_3H_ad' in row.path:
        if row.energy < h3ad_low_pot_energy:
            h3ad_low_pot_energy = row.energy
            h3ad_path = row.path
    if '04_4H_ad' in row.path:
        if row.energy < h4ad_low_pot_energy:
            h4ad_low_pot_energy = row.energy
            h4ad_path = row.path

print(h4ad_path)
species = {'H2': StatMech(name='H2', atoms=molecule('H2'),
                   #took this from my calculated H2 molecule
                   potentialenergy=-6.5041754,
                   vib_wavenumbers=[4577.98], symmetrynumber=2,
                   #symmetry number comes from the point group
                   **presets['idealgas']),
        #'O2': StatMech(name='O2', atoms=molecule('O2'),
         #                  #took this from my calculated O2 molecule
          #                 potentialenergy=-10.277953,
           #                vib_wavenumbers=[1603], symmetrynumber=1,
            #               #symmetry number comes from the point group
             #              **presets['idealgas']),
                       'bare': StatMech(
                 name='bare', potentialenergy=bare_energy, **presets['electronic']),
        #'CO': StatMech(name='CO', atoms=molecule('CO'),
         #                  #took this from my calculated CO molecule
          #                 potentialenergy=-15.185734,
           #            #need to confirm that CO symmetrymnumber is 1
            #               vib_wavenumbers=[2141], symmetrynumber=1,
             #              #symmetry number comes from the point group
              #             **presets['idealgas']),

}

for row in db.select():
    if h1ad_path in row.path:
        species[f"ad_1hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3402.296399, 730.977274, 641.835883],
            **presets['harmonic'])
    if h2ad_path in row.path:
        species[f"ad_2hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3507.459279, 3083.693007, 994.848016,
                             769.764211, 709.249024, 475.216211],
            **presets['harmonic'])
    if h3ad_path in row.path:
        species[f"ad_3hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3534.710211, 3442.478497, 2835.254171,
                             914.995433, 843.014135, 732.632769,
                             671.459514, 477.391946, 339.341457],
            **presets['harmonic'])
    if h4ad_path in row.path:
        species[f"ad_4hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3583.132654, 3177.356149, 3142.9158,
                             1647.37151, 1176.598406, 1133.143259,
                             924.772332, 888.696728, 716.616038,
                             651.433586, 570.170672, 370.203939],
            **presets['harmonic'])

print(species, 'species')

from pmutt.reaction import Reaction

reactions=[
    Reaction.from_string('bare = bare', species)]
for n in species:
    if 'H2' not in n and 'bare' not in n:
        if n.split('_')[1] == '1hy' or n.split('_')[1] == '1ad':
            reactions.append(Reaction.from_string(f"bare + 0.5 H2 = {n}", species))
        if n.split('_')[1] == '2hy' or n.split('_')[1] == '2ad':
            reactions.append(Reaction.from_string(f"bare + H2 = {n}", species))
        if n.split('_')[1] == '3hy':
            reactions.append(Reaction.from_string(f"bare + 1.5 H2 = {n}", species))
        if n.split('_')[1] == '4hy':
            reactions.append(Reaction.from_string(f"bare + 2 H2 = {n}", species))

print(reactions)
for reaction in reactions:
    print(f"the reaction is {reaction}, \n the reactants are {reaction.reactants} \n products are {reaction.products}")


from pmutt.reaction.phasediagram import PhaseDiagram

phase_diagram = PhaseDiagram(reactions=reactions)


# ## Creating a 1D Phase Diagram

# In[4]:


import numpy as np
from matplotlib import pyplot as plt

T = np.linspace(300, 1000, 200) # K
fig1, ax1 = phase_diagram.plot_1D(x_name='T', x_values=T, P=1, G_units='kJ/mol')


# Set colors to lines
colors = ('#000080', '#0029FF', '#00D5FF', '#7AFF7D',
          '#FFE600', '#FF4A00', '#800000')
for color, line in zip(colors, ax1.get_lines()):
    line.set_color(color)

labels = []
for key, value in species.items():
    if str(key) != 'H2':
        labels.append(str(key))
# Set labels to lines

print(labels, 'labels for plot')
handles, _ = ax1.get_legend_handles_labels()
print(handles, 'handles')
print(_)
for handle in handles:
    print(f"the is the handle xday {handle.get_data()}")
    print(f"this is the path {handle.get_path()}")


ax1.get_legend().remove()
ax1.legend(handles, labels, loc=0,
           title='Various configurations', fontsize= 8)
ax1.set_xlabel('Temperature (K)')

fig1.set_dpi(150.)
fig1.show()




# ## Creating a 2D Phase Diagram

# In[5]:


# Generate Pressure range
T = np.linspace(300, 1000) # K
P = np.logspace(-3, 3) # bar

fig2, ax2, c2, cbar2 = phase_diagram.plot_2D(x1_name='T', x1_values=T,
                                             x2_name='P', x2_values=P)


# Change y axis to use log scale
ax2.set_yscale('log')
# Add axis labels
ax2.set_xlabel('Temperature (K)')
ax2.set_ylabel('H Pressure (bar)')
# Change color scheme
plt.set_cmap('jet')
# Add labels
cbar2.ax.set_yticklabels(labels)
print(labels)

fig2.set_dpi(150.)
plt.show()


# In[ ]:


