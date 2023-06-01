from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from pmutt.statmech import StatMech, presets
from ase.build import molecule
import seaborn as sns
from pprint import pprint
import time
from pmutt.reaction import Reaction
from pmutt.reaction.phasediagram import PhaseDiagram
startTime = time.time()

db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/updated.db')
sub0_Mg_vac_db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
27_s100-Mg-vac_sub1/mg_vac_sub0/updated.db')
sub1_Mg_vac_sub0_pt_db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
23_s100-Mg-vac_sub_bare_0/updated.db')
palette = sns.color_palette('muted')


species = {'H2': StatMech(name='H2', atoms=molecule('H2'),
                   #took this from my calculated H2 molecule
                   potentialenergy=-6.5041754,
                   vib_wavenumbers=[4577.98], symmetrynumber=2,
                   #symmetry number comes from the point group
                   **presets['idealgas'])

}
configs = np.unique(['s100-sub1-Mg-vac_sub1', 's100-sub0-Mg-vac_sub1',
                     's100-sub1-Mg-vac_sub0'])
print(configs)
species_dict = {}
for config in configs:
    species_dict[config]={}
bare_dict = {}
h1ad_low_pot_energy = 10000000
h2ad_low_pot_energy = 10000000
h3ad_low_pot_energy = 10000000
h4ad_low_pot_energy = 10000000
#h1subad_low_pot_energy = 10000000
#h2subad_low_pot_energy = 10000000
#h2subad_low_pot_energy2 = 10000000
for row in db.select():
    if '02_pt-mgo-ethylene/01_bare/opt_PBE_400_221' in row.path:
        print(row.path)
        print(row.energy)
        species_dict['s100-sub1-Mg-vac_sub1']['bare'] = row.path
        bare_dict['s100-sub1-Mg-vac_sub1'] = row.energy
    if '02_all_surf_atoms_constrained' in row.path:
        if row.energy < h1ad_low_pot_energy:
            h1ad_low_pot_energy = row.energy
            species_dict['s100-sub1-Mg-vac_sub1']['surf_1H_ad'] = row.energy
            h1ad_path = row.path
    if '03_2_ad_hy' in row.path:
        if row.energy < h2ad_low_pot_energy:
            h2ad_low_pot_energy = row.energy
            h2ad_path = row.path
            species_dict['s100-sub1-Mg-vac_sub1']['surf_2H_ad'] = row.energy
    if '04_3_ad_hy' in row.path:
        if row.energy < h3ad_low_pot_energy:
            h3ad_low_pot_energy = row.energy
            h3ad_path = row.path
            species_dict['s100-sub1-Mg-vac_sub1']['surf_3H_ad'] = row.energy
    if '05_4_ad_hy' in row.path and not '03_B2_B3_C2_C3' in row.path:
        if row.energy < h4ad_low_pot_energy:
            h4ad_low_pot_energy = row.energy
            h4ad_path = row.path
            species_dict['s100-sub1-Mg-vac_sub1']['surf_4H_ad'] = row.energy
    #if '09_sub_hy' in row.path and not '2_sub_hy' in row.path:
    #    if row.energy < h1subad_low_pot_energy:
    #        h1subad_low_pot_energy = row.energy
    #        h1subad_path = row.path
    #if '09_sub_hy' in row.path and '2_sub_hy' in row.path:
    #    if row.energy < h2subad_low_pot_energy:
    #        h2subad_low_pot_energy = row.energy
    #        h2subad_path = row.path
    #if '19_100_PtMgO_2_sub_hy' in row.path:
    #    if row.energy < h2subad_low_pot_energy2:
    #        h2subad_low_pot_energy2 = row.energy
    #        h2subad_path2 = row.path
            #print(h2subad_path2)
h1ad_surf_low_pot_energy = 10000000
h2ad_surf_pot_energy = 10000000
h3ad_surf_low_pot_energy = 10000000
h4ad_surf_low_pot_energy = 10000000

for row in sub0_Mg_vac_db.select(convergence=True):
    #print('hello')
    print(row.path)
    if 'bare' in row.path:
        print('hello')
        species_dict[configs[0]]['bare'] = row.path
        bare_dict[configs[0]] = row.energy
    if '01_1H_ad' in row.path:
        if row.energy < h1ad_surf_low_pot_energy:
            h1ad_surf_low_pot_energy = row.energy
            species_dict[configs[0]]['surf_H_ad'] = row.energy
    if '2H_ad' in row.path:
        if row.energy < h2ad_surf_pot_energy:
            h2ad_surf_pot_energy = row.energy
            species_dict[configs[0]]['surf_2H_ad'] = row.energy
    if '3H_ad' in row.path:
        if row.energy < h3ad_surf_low_pot_energy:
            h3ad_surf_low_pot_energy = row.energy
            species_dict[configs[0]]['surf_3H_ad'] = row.energy
    if '4H_ad' in row.path:
        if row.energy < h4ad_surf_low_pot_energy:
            h4ad_surf_low_pot_energy = row.energy
            species_dict[configs[0]]['surf_4H_ad'] = row.energy

h1ad_surf_low_pot_energy = 10000000
h2ad_surf_pot_energy = 10000000
h3ad_surf_low_pot_energy = 10000000
h4ad_surf_low_pot_energy = 10000000

for row in sub1_Mg_vac_sub0_pt_db.select(convergence=True):
    if 'bare' in row.path.split('/')[-2]:
        species_dict[configs[1]]['bare'] = row.path
        bare_dict[configs[1]] = row.energy
    if '1H_ad' in row.path:
        if row.energy < h1ad_surf_low_pot_energy:
            h1ad_surf_low_pot_energy = row.energy
            species_dict[configs[1]]['surf_H_ad'] = row.energy
    if '2H_ad' in row.path:
        if row.energy < h2ad_surf_pot_energy:
            h2ad_surf_pot_energy = row.energy
            species_dict[configs[1]]['surf_2H_ad'] = row.energy

bare_min = min(bare_dict.values())
reactions = []
shifts = {}
for config in configs:
    shifts[f"{config}"] = bare_dict[config] - bare_min

print(bare_dict)
for config in configs:
        species[f"bare_{config}"] = StatMech(name=f"bare_{config}",
                                            potentialenergy=bare_dict[f"{config}"],
                                            **presets['electronic'])
        species[f"shift_{config}"] = StatMech(
                 name='shift', potentialenergy=shifts[config],
            **presets['electronic'])
        reactions.append(Reaction.from_string(f"bare_{config} = bare_{config} \
        + shift_{config}", species))

print(species)

for config in configs:
    for item in species_dict[config]:
        print(config)
        print(item)
        print(species_dict[config][item])
        if '_H_ad' in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[3402.296399, 730.977274, 641.835883],
                **presets['harmonic'])
            reactions.append(Reaction.from_string(f"bare_{config} \
            + 0.5 H2 = {item +'_'+ config} + shift_{config}", species))
        if '2H_ad' in item:
            species[item +'_'+ config] = StatMech(
                name=item +'_'+ config, potentialenergy=species_dict[config][item],
                vib_wavenumbers=[3507.459279, 3083.693007, 994.848016,
                                 769.764211, 709.249024, 475.216211],
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

print(reactions)
#print(species_dict)
#print(bare_dict)

phase_diagram = PhaseDiagram(reactions=reactions)



T = np.linspace(300, 1000, 10) # K
fig1, ax1 = phase_diagram.plot_1D(x_name='T', x_values=T, P=1, G_units='eV')


# Set colors to lines
colors = ('#000080', '#0029FF', '#00D5FF', '#7AFF7D',
          '#FFE600', '#FF4A00', '#800000')
# Code from example
for color, line in zip(colors, ax1.get_lines()):
    print(line, 'line')
    line.set_color(color)

num_configs = len(configs)

for line in ax1.get_lines():
    print(line, 'line')
    for count, config in enumerate(configs):
        if config in str(line):
            line.set_color(palette[count])
            if 'H' in str(line):
                line.set_marker('^')
            else:
                line.set_marker('o')

labels = []
for key, value in species.items():
    if str(key) != 'H2' and 'shift' not in str(key) and 'H_ad' not in str(key):
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
labels = []
for key, value in species.items():
    if str(key) != 'H2' and 'shift' not in str(key):
        labels.append(str(key))
cbar2.ax.set_yticklabels(labels)
print(labels)
fig2.set_dpi(150.)
fig2.set_size_inches((14,8))
plt.show()



executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

'''
for row in db.select():
    if h1ad_path in row.path:
        species[f"ad_1hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=row.data['vib_wavenumbers'],
            **presets['harmonic'])
    if h2ad_path in row.path:
        if row.vib == True:
            species[f"ad_2hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
                name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
                vib_wavenumbers=row.data['vib_wavenumbers'],
                **presets['harmonic'])
    if h3ad_path in row.path:
        species[f"ad_3hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=row.data['vib_wavenumbers'],
            **presets['harmonic'])
    if h4ad_path in row.path:
        species[f"ad_4hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=row.data['vib_wavenumbers'],
            **presets['harmonic'])
    #if h1subad_path in row.path:
    #    species[f"sub_1ad_hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
    #        name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
    #        vib_wavenumbers=row.data['vib_wavenumbers'],
    #        **presets['harmonic'])
    #if h2subad_path in row.path:
    #    species[f"sub_surf_2ad_hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
    #        name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
    #        vib_wavenumbers=row.data['vib_wavenumbers'],
    #        **presets['harmonic'])
    #if h2subad_path2 in row.path:
    #    species[f"sub_2ad_hy_conf_{row.path.split('/')[-2].split('_')[0]}"] = StatMech(
    #        name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
    #        vib_wavenumbers=row.data['vib_wavenumbers'],
    #        **presets['harmonic'])
#print(species, 'species')

from pmutt.reaction import Reaction

reactions=[
    Reaction.from_string('bare = bare', species)]

for n in species:
    if 'H2' not in n and 'bare' not in n:
        if n.split('_')[1] == '1hy' or n.split('_')[1] == '1ad':
            reactions.append(Reaction.from_string(f"bare + 0.5 H2 = {n}", species))
        if n.split('_')[1] == '2hy' or n.split('_')[1] == '2ad' or '2ad' in n:
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
fig1, ax1 = phase_diagram.plot_1D(x_name='T', x_values=T, P=1, G_units='eV')


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
fig2.set_size_inches((11,8))
plt.show()


# In[ ]:

'''