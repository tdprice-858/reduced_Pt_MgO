from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from pmutt.statmech import StatMech, presets
from ase.build import molecule
import seaborn as sns

db = connect('/Users/tdprice/Desktop/02_pt-mgo-ethylene/25_vac_study_best_fit/\
s100_sub1_ox_vac_2mg_vac/best_fit_H_ad_ox_2mg.db')

palette = sns.color_palette('muted')
colors = {'bare': palette[0],
          'H': palette[1]}

# Generating species dictionary using pmutt StatMech class

species = {'H2': StatMech(name='H2', atoms=molecule('H2'),
                   #took this from my calculated H2 molecule
                   potentialenergy=-6.9909168,
                   vib_wavenumbers=[4314.39], symmetrynumber=2,
                   #symmetry number comes from the point group
                   **presets['idealgas']),
                       'bare_88_27_14': StatMech(
                 name='bare_88_27_14', potentialenergy=-943.76857, **presets['electronic']),
}

#The following shifts the energy of the less stable structures
#so that everything is relative to the minimum energy structure

energy_shift = -943.00177682 - (-943.76857)
species['shift'] = StatMech(
                 name='shift', potentialenergy=energy_shift, **presets['electronic'])

h1ad_low_pot_energy_88_27_14 = 10000000
h2ad_low_pot_energy_88_27_14 = 10000000
h3ad_low_pot_energy_88_27_14 = 10000000
h4ad_low_pot_energy_88_27_14 = 10000000



for row in db.select():
    if '88_27_14' in row.path:
        if '01_H_ad' in row.path:
            if row.energy < h1ad_low_pot_energy_88_27_14:
                h1ad_low_pot_energy_88_27_14 = row.energy
                h1ad_path = row.path
        if '2H_ad' in row.path:
            if row.energy < h2ad_low_pot_energy_88_27_14:
                h2ad_low_pot_energy_88_27_14 = row.energy
                h2ad_path = row.path
        if '3H_ad' in row.path:
            if row.energy < h3ad_low_pot_energy_88_27_14:
                h3ad_low_pot_energy_88_27_14 = row.energy
                h3ad_path = row.path
        if '4H_ad' in row.path:
            if row.energy < h4ad_low_pot_energy_88_27_14:
                h4ad_low_pot_energy_88_27_14 = row.energy
                h4ad_path = row.path



for row in db.select():
    #if '02_all_surf_atoms_constrained' in row.path:
    if h1ad_path in row.path:
        species[f"ad_1hy_{row.path.split('/')[-4]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3402.296399, 730.977274, 641.835883],
            **presets['harmonic'])
    #if '03_2_ad_hy' in row.path:
    if h2ad_path in row.path:

        species[f"ad_2hy_{row.path.split('/')[-4]}"] = StatMech(
                name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
                vib_wavenumbers=[3507.459279, 3083.693007, 994.848016,
                                 769.764211, 709.249024, 475.216211],
                **presets['harmonic'])
    #if '04_3_ad_hy' in row.path:
    if h3ad_path in row.path:
        species[f"ad_3hy_{row.path.split('/')[-4]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3534.710211, 3442.478497, 2835.254171,
                             914.995433, 843.014135, 732.632769,
                             671.459514, 477.391946, 339.341457],
            **presets['harmonic'])
    #if '05_4_ad_hy' in row.path and not '03_B2_B3_C2_C3' in row.path:
    if h4ad_path in row.path:
        species[f"ad_4hy_{row.path.split('/')[-4]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3583.132654, 3177.356149, 3142.9158,
                             1647.37151, 1176.598406, 1133.143259,
                             924.772332, 888.696728, 716.616038,
                             651.433586, 570.170672, 370.203939],
            **presets['harmonic'])

h1ad_low_pot_energy_88_27_14 = 10000000
h2ad_low_pot_energy_88_27_14 = 10000000
h3ad_low_pot_energy_88_27_14 = 10000000
h4ad_low_pot_energy_88_27_14 = 10000000



for row in db.select():
    if '84_46_37' in row.path:
        if '01_H_ad' in row.path:
            if row.energy < h1ad_low_pot_energy_88_27_14:
                h1ad_low_pot_energy_88_27_14 = row.energy
                h1ad_path = row.path
        if '2H_ad' in row.path:
            if row.energy < h2ad_low_pot_energy_88_27_14:
                h2ad_low_pot_energy_88_27_14 = row.energy
                h2ad_path = row.path
        if '3H_ad' in row.path:
            if row.energy < h3ad_low_pot_energy_88_27_14:
                h3ad_low_pot_energy_88_27_14 = row.energy
                h3ad_path = row.path
        if '4H_ad' in row.path:
            if row.energy < h4ad_low_pot_energy_88_27_14:
                h4ad_low_pot_energy_88_27_14 = row.energy
                h4ad_path = row.path
        if 'bare' in row.path:
            bare_path = row.path
            print(row.path)
            print(row.energy)



for row in db.select():
    #if '02_all_surf_atoms_constrained' in row.path:
    if h1ad_path in row.path:
        species[f"ad_1hy_{row.path.split('/')[-4]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3402.296399, 730.977274, 641.835883],
            **presets['harmonic'])
    #if '03_2_ad_hy' in row.path:
    if h2ad_path in row.path:

        species[f"ad_2hy_{row.path.split('/')[-4]}"] = StatMech(
                name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
                vib_wavenumbers=[3507.459279, 3083.693007, 994.848016,
                                 769.764211, 709.249024, 475.216211],
                **presets['harmonic'])
    #if '04_3_ad_hy' in row.path:
    if h3ad_path in row.path:
        species[f"ad_3hy_{row.path.split('/')[-4]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3534.710211, 3442.478497, 2835.254171,
                             914.995433, 843.014135, 732.632769,
                             671.459514, 477.391946, 339.341457],
            **presets['harmonic'])
    #if '05_4_ad_hy' in row.path and not '03_B2_B3_C2_C3' in row.path:
    if h4ad_path in row.path:
        species[f"ad_4hy_{row.path.split('/')[-4]}"] = StatMech(
            name=row.path.split('/')[-2].split('_')[0], potentialenergy=row.energy,
            vib_wavenumbers=[3583.132654, 3177.356149, 3142.9158,
                             1647.37151, 1176.598406, 1133.143259,
                             924.772332, 888.696728, 716.616038,
                             651.433586, 570.170672, 370.203939],
            **presets['harmonic'])

    if bare_path in row.path:
        species['bare_84_46_37'] = StatMech(name='bare_84_46_37',
                                            potentialenergy=row.energy,
                                            **presets['electronic'])





# Setting up reactions for phase diagrams
from pmutt.reaction import Reaction

#reactions=[
#    Reaction.from_string('bare_88_27_14 = bare_88_27_14', species),
#Reaction.from_string('bare_84_46_37 = bare_84_46_37', species)]
reactions=[]
for n in species:
    if 'H2' not in n and 'CO' not in n and 'shift' not in n:
        print(n)
        if '88_27_14' in n:
            if n.split('_')[1] == '1hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + 0.5 H2 = {n}", species))
            if n.split('_')[1] == '2hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + H2 = {n}", species))
            if n.split('_')[1] == '3hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + 1.5 H2 = {n}", species))
            if n.split('_')[1] == '4hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + 2 H2 = {n}", species))
            if 'bare' in n:
                reactions.append(Reaction.from_string(f"{n}  = {n}", species))
        if '84_46_37' in n:
            if n.split('_')[1] == '1hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + 0.5 H2 = {n}+ shift", species))
            if n.split('_')[1] == '2hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + H2 = {n}+ shift", species))
            if n.split('_')[1] == '3hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + 1.5 H2 = {n}+ shift", species))
            if n.split('_')[1] == '4hy':
                reactions.append(Reaction.from_string(f"bare_{n.split('hy_')[-1]} + 2 H2 = {n}+ shift", species))
            if 'bare' in n:
                reactions.append(Reaction.from_string(f"{n} = {n} + shift", species))

from pmutt.reaction.phasediagram import PhaseDiagram

phase_diagram = PhaseDiagram(reactions=reactions)


# ## Creating a 1D Phase Diagram

# In[4]:


import numpy as np
from matplotlib import pyplot as plt

T = np.linspace(300, 1000, 10) # K
fig1, ax1 = phase_diagram.plot_1D(x_name='T', x_values=T, P=1, G_units='kJ/mol')


# Set colors to lines
colors = ('#000080', '#0029FF', '#00D5FF', '#7AFF7D',
          '#FFE600', '#FF4A00', '#800000')
# Code from example
'''for color, line in zip(colors, ax1.get_lines()):
    print(line, 'line')
    line.set_color(color)'''
# Setting up colors to have each unique vac structure a different color
for line in ax1.get_lines():
    print(line, 'line')
    if '88_27_14' in str(line):
        line.set_color(palette[0])
        if 'H' in str(line):
            line.set_marker('^')
        else:
            line.set_marker('o')
    if '84_46_37' in str(line):
        line.set_color(palette[1])
        if 'H' in str(line):
            line.set_marker('^')
        else:
            line.set_marker('o')
    #line.set_color(color)

labels = []
for key, value in species.items():
    if str(key) != 'H2' and str(key) != 'shift':
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
plt.show()


# In[ ]: