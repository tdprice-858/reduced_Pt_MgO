'''
This class generates a phase diagram for stability comparison of various
adsorbate structures.

Author: Trevor Price
2023
'''

#!/usr/bin/env python
from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from pmutt.statmech import StatMech, presets
from ase.build import molecule
import seaborn as sns
import time
from pmutt.reaction import Reaction
from pmutt.reaction.phasediagram import PhaseDiagram
startTime = time.time()

#db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
#26_vac_study_most_stable/s100_sub1_ox_vac_2mg_vac/updated.db')
#db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
#26_vac_study_most_stable/s100_sub1_ox_vac_2mg_vac/88_39_46/updated.db')
#db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
#26_vac_study_most_stable/s100_sub1_2ox_vac_2mg_vac/84_88_16_26/updated.db')

db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
26_vac_study_most_stable/s100_sub1_ox_vac_2mg_vac/88_39_46/updated.db')
iso_molecule_db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
08_isolated_molecules/RPBE_iso/updated.db')
palette = sns.color_palette('muted')


configs = np.unique([row.path.split('s100_sub1_ox_vac_2mg_vac/')[-1].split('/')[0]
           for row in db.select(convergence=True)])
#configs = np.unique([row.path.split('s100_sub1_2ox_vac_2mg_vac/')[-1].split('/')[0]
#           for row in db.select(convergence=True)])
species_dict = {}
bare_dict = {}



bare_min = 100
for config in configs:
    species_dict[config] = {}
    h1ad_surf_low_pot_energy = 10000000
    h2ad_surf_pot_energy = 10000000
    h3ad_surf_low_pot_energy = 10000000
    h4ad_surf_low_pot_energy = 10000000
    h1ad_sub_low_pot_energy = 10000000
    h2ad_sub_pot_energy = 10000000
    h3ad_sub_low_pot_energy = 10000000
    h4ad_sub_low_pot_energy = 10000000
    h1ad_surf_sub_low_pot_energy = 10000000
    h2ad_surf_sub_pot_energy = 10000000
    h3ad_surf_sub_low_pot_energy = 10000000
    h4ad_surf_sub_low_pot_energy = 10000000
    H2_mol_low_pot_energy = 100000
    CO_low_pot_energy = 100000
    O_low_pot_energy = 100000
    O2_low_pot_energy = 10000
    CO_2H_low_pot_energy = 10000
    for row in db.select(convergence=True):
        if config in row.path:
            if 'bare' in row.path:
                species_dict[config]['bare'] = row.path
                bare_dict[config] = row.energy
                if row.energy < bare_min:
                    bare_min = row.energy
            elif 'subsurf' in row.path:
                if '_H_ad' in row.path:
                    if row.energy < h1ad_sub_low_pot_energy:
                        h1ad_sub_low_pot_energy = row.energy
                        species_dict[config]['sub_H_ad'] = row.energy
                if '2H_ad' in row.path:
                    if row.energy < h2ad_sub_pot_energy:
                        h2ad_sub_pot_energy = row.energy
                        species_dict[config]['sub_2H_ad'] = row.energy
                if '3H_ad' in row.path:
                    if row.energy < h3ad_sub_low_pot_energy:
                        h3ad_sub_low_pot_energy = row.energy
                        species_dict[config]['sub_3H_ad'] = row.energy
                if '4H_ad' in row.path:
                    if row.energy < h4ad_sub_low_pot_energy:
                        h4ad_sub_low_pot_energy = row.energy
                        species_dict[config]['sub_4H_ad'] = row.energy
            elif 'surf_sub' in row.path:
                if '01_H_ad' in row.path:
                    if row.energy < h1ad_surf_sub_low_pot_energy:
                        h1ad_surf_sub_low_pot_energy = row.energy
                        species_dict[config]['surf_sub_H_ad'] = row.energy
                if '2H_ad' in row.path:
                    if row.energy < h2ad_surf_sub_pot_energy:
                        h2ad_surf_sub_pot_energy = row.energy
                        species_dict[config]['surf_sub_2H_ad'] = row.energy
                if '3H_ad' in row.path:
                    if row.energy < h3ad_surf_sub_low_pot_energy:
                        h3ad_surf_sub_low_pot_energy = row.energy
                        species_dict[config]['surf_sub_3H_ad'] = row.energy
                if '4H_ad' in row.path:
                    if row.energy < h4ad_surf_sub_low_pot_energy:
                        h4ad_surf_sub_low_pot_energy = row.energy
                        species_dict[config]['surf_sub_4H_ad'] = row.energy
            elif 'surf' in row.path:
                if '01_H_ad' in row.path:
                    if row.energy < h1ad_surf_low_pot_energy:
                        h1ad_surf_low_pot_energy = row.energy
                        species_dict[config]['surf_H_ad'] = row.energy
                if '2H_ad' in row.path:
                    print(row.path)
                    print(row.energy)


                    if row.energy < h2ad_surf_pot_energy:


                        h2ad_surf_pot_energy = row.energy
                        species_dict[config]['surf_2H_ad'] = row.energy

                if '3H_ad' in row.path:
                    if row.energy < h3ad_surf_low_pot_energy:
                        h3ad_surf_low_pot_energy = row.energy
                        species_dict[config]['surf_3H_ad'] = row.energy
                if '4H_ad' in row.path:
                    if row.energy < h4ad_surf_low_pot_energy:
                        h4ad_surf_low_pot_energy = row.energy
                        species_dict[config]['surf_4H_ad'] = row.energy
                if 'H2_ad' in row.path:
                    if row.energy < H2_mol_low_pot_energy:
                        H2_mol_low_pot_energy = row.energy
                        species_dict[config]['surf_H2_ad'] = row.energy
            elif 'CO' in row.path and 'H' not in row.formula:
                if row.energy < CO_low_pot_energy:
                    CO_low_pot_energy = row.energy
                    species_dict[config]['CO_ad'] = row.energy

            elif 'O2_ad' in row.path:
                if row.energy < O2_low_pot_energy:
                    O2_low_pot_energy = row.energy
                    species_dict[config]['O2_ad'] = row.energy

            elif 'O' in row.path and 'CO' not in row.path and 'O2' not in row.path:
                if row.energy < O_low_pot_energy:
                    O_low_pot_energy = row.energy
                    species_dict[config]['O_ad'] = row.energy

            elif 'H' in row.formula and 'C' in row.formula:
                if row.energy < CO_2H_low_pot_energy:
                    CO_2H_low_pot_energy = row.energy
                    species_dict[config]['CO_2H_ad'] = row.energy




for config in configs:
    bare_dict[config] -= bare_min


#Here we will start to add our species to the StatMech class in pmutt
species = {}
for row in iso_molecule_db.select(convergence=True):
    if 'O2' in row.formula or 'H2' in row.formula:
        species[f"{row.formula}"] = StatMech(name=f"{row.formula}",
                                             atoms=row.toatoms(),
                       potentialenergy=row.energy,
                       vib_wavenumbers=[row.data['vib_wavenumbers'][0]], symmetrynumber=2,
                       **presets['idealgas'])
    if 'CO' in row.formula:
        species[f"{row.formula}"] = StatMech(name=f"{row.formula}", atoms=row.toatoms(),
                           potentialenergy=row.energy,
                           vib_wavenumbers=[row.data['vib_wavenumbers'][0]], symmetrynumber=1,
                           **presets['idealgas'])

reactions = []

for config in configs:
    for row in db.select(path=species_dict[config]['bare']):

        species[f"bare_{config}"] = StatMech(name=f"bare_{config}",
                                            potentialenergy=row.energy,
                                            **presets['electronic'])
        species[f"shift_{config}"] = StatMech(
                 name='shift', potentialenergy=bare_dict[config],
            **presets['electronic'])
        reactions.append(Reaction.from_string(f"bare_{config} = bare_{config} \
        + shift_{config}", species))

print(species_dict)

for config in configs:
    for item in species_dict[config]:

        if '_H_ad' in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[3402.296399, 730.977274, 641.835883],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
            + 0.5 H2 = {item +'_'+ config} + shift_{config}", species))
        if '_2H_ad' in item and 'CO' not in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[3507.459279, 3083.693007, 994.848016,
                                 769.764211, 709.249024, 475.216211],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                        + H2 = {item +'_'+ config} + shift_{config}", species))
        if 'H2_ad' in item and 'CO' not in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[4128.99, 707.19, 467.21,
                                 310.50, 165.09, 100.22],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                        + H2 = {item +'_'+ config} + shift_{config}", species))
        if '3H_ad' in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[3534.710211, 3442.478497, 2835.254171,
                             914.995433, 843.014135, 732.632769,
                             671.459514, 477.391946, 339.341457],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                        + 1.5 H2 = {item +'_'+ config} + shift_{config}", species))
        if '4H_ad' in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[3583.132654, 3177.356149, 3142.9158,
                             1647.37151, 1176.598406, 1133.143259,
                             924.772332, 888.696728, 716.616038,
                             651.433586, 570.170672, 370.203939],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                                    + 2 H2 = {item +'_'+ config} + shift_{config}", species))
        if 'O_ad' in item and not 'CO' in item:
            species[item + '_' + config] = StatMech(
                name=item + '_' + config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[583.925039, 460.242488, 296.488304],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                                                + 0.5 O2 = {item + '_' + config} + shift_{config}", species))
        if 'O2_ad' in item:
            species[item + '_' + config] = StatMech(
                name=item + '_' + config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[1141.442323, 584.621919, 382.38351, 269.965748, 145.648531, 109.555067],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                                                + O2 = {item + '_' + config} + shift_{config}", species))
        if 'CO_2H' in item:
            species[item + '_' + config] = StatMech(
                name=item + '_' + config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[1141.442323, 584.621919, 382.38351, 269.965748, 145.648531, 109.555067],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                                                + CO + H2 = {item + '_' + config} + shift_{config}", species))
        if 'CO_ad' in item:
            species[item + '_' + config] = StatMech(
                name=item + '_' + config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[1579.490562, 1072.366846, 711.887527, 628.454417, 396.794991, 159.020783],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
                                                + CO = {item + '_' + config} + shift_{config}", species))







phase_diagram = PhaseDiagram(reactions=reactions)

print(species)

T = np.linspace(300, 1000, 10) # K
fig1, ax1 = phase_diagram.plot_1D(x_name='T', x_values=T, P=1, G_units='eV')


# Set colors to lines
colors = ('#000080', '#0029FF', '#00D5FF', '#7AFF7D',
          '#FFE600', '#FF4A00', '#800000')
# Code from example
'''for color, line in zip(colors, ax1.get_lines()):
    print(line)
    print(color)
    line.set_color(color)'''

num_configs = len(configs)
i=0
for counts, line in enumerate(ax1.get_lines()):
    print(line)
    for count, config in enumerate(configs):
        if config in str(line):
            if i>9:
                i = 0
            line.set_color(palette[i])
            i += 1
            if 'CO_ad' in str(line):
                line.set_marker('*')
            elif 'O2_ad' in str(line):
                line.set_marker('d')
            elif 'O_ad' in str(line):
                line.set_marker('D')
            elif 'CO_2H' in str(line):
                line.set_marker('x')
            elif 'H' in str(line):
                line.set_marker('^')
            else:
                line.set_marker('o')

labels = []
for key, value in species.items():
    if str(key) not in ['H2', 'CO', 'O2'] and 'shift' not in str(key):
        labels.append(str(key))
# Set labels to lines

handles, _ = ax1.get_legend_handles_labels()
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
P = np.logspace(-3, 1) # bar

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

fig2.set_dpi(150.)
fig2.set_size_inches((11,8))
plt.show()



executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
print(labels)