from ase.db import connect
import numpy as np
import matplotlib.pyplot as plt
from ase.visualize import view

#db = connect('/Users/tdprice/Desktop/pt_mgo_ethylene/pt_mgo.db')
db = connect('/Users/tdprice/Desktop/pt_mgo_ethylene/vacancy_study/s100_sub1_2ox_vac_2mg_vac/updated.db')

#Empty list for data
ad_1H_energy = []
ad_2H_energy = []
ad_3H_energy = []
ad_4H_energy = []
ad_6H_energy = []
vac_energy = []
H2_energy = []
is_there_a_copy = []
i = 1
s100_sub1_ox_vac_2mg_vac_dict = {}
s100_sub1_ox_vac_mg_vac = {}
s100_sub1_ox_vac = {}
s100_sub1_mg_vac = {}
s100_sub1_2ox_vac_2mg_vac_dict = {}
s100_sub1_2ox_vac_mg_vac_dict = {}

for row in db.select():
    if "H_ad" in row.path:
        continue
    print(i)
    #if 's100_sub1_ox_vac_2mg_vac_88_16_39' in row.path:
        #view(row.toatoms())
    if row.path.split('/')[10] == 's100_sub1_ox_vac_2mg_vac':
        #print(row.path.split('/')[11])
        s100_sub1_ox_vac_2mg_vac_dict[row.path.split('/')[11]] = {}
        s100_sub1_ox_vac_2mg_vac_dict[row.path.split('/')[11]]['energy'] = row.energy
        s100_sub1_ox_vac_2mg_vac_dict[row.path.split('/')[11]]['frechet'] = row.frechet
        s100_sub1_ox_vac_2mg_vac_dict[row.path.split('/')[11]]['r_factor'] = row.r_factor
        s100_sub1_ox_vac_2mg_vac_dict[row.path.split('/')[11]]['red_chi_square'] = row.red_chi_sq
    if row.path.split('/')[10] == 's100_sub1_ox_vac_mg_vac':
        s100_sub1_ox_vac_mg_vac[row.path.split('/')[11]] = {}
        s100_sub1_ox_vac_mg_vac[row.path.split('/')[11]]['energy'] = row.energy
        s100_sub1_ox_vac_mg_vac[row.path.split('/')[11]]['frechet'] = row.frechet
        s100_sub1_ox_vac_mg_vac[row.path.split('/')[11]]['r_factor'] = row.r_factor
        s100_sub1_ox_vac_mg_vac[row.path.split('/')[11]]['red_chi_square'] = row.red_chi_sq
    if row.path.split('/')[10] == 's100_sub1_ox_vac':
        s100_sub1_ox_vac[row.path.split('/')[11]] = {}
        s100_sub1_ox_vac[row.path.split('/')[11]]['energy'] = row.energy
        s100_sub1_ox_vac[row.path.split('/')[11]]['frechet'] = row.frechet
        s100_sub1_ox_vac[row.path.split('/')[11]]['r_factor'] = row.r_factor
        s100_sub1_ox_vac[row.path.split('/')[11]]['red_chi_square'] = row.red_chi_sq
    if row.path.split('/')[10] == 's100_sub1_mg_vac':
        s100_sub1_mg_vac[row.path.split('/')[11]] = {}
        s100_sub1_mg_vac[row.path.split('/')[11]]['energy'] = row.energy
        s100_sub1_mg_vac[row.path.split('/')[11]]['frechet'] = row.frechet
        s100_sub1_mg_vac[row.path.split('/')[11]]['r_factor'] = row.r_factor
        s100_sub1_mg_vac[row.path.split('/')[11]]['red_chi_square'] = row.red_chi_sq
    if row.path.split('/')[10] == 's100_sub1_2ox_vac_2mg_vac':
        try:
            print(row.frechet)
            s100_sub1_2ox_vac_2mg_vac_dict[row.path.split('/')[11]] = {}
            s100_sub1_2ox_vac_2mg_vac_dict[row.path.split('/')[11]]['energy'] = row.energy
            s100_sub1_2ox_vac_2mg_vac_dict[row.path.split('/')[11]]['frechet'] = row.frechet
            s100_sub1_2ox_vac_2mg_vac_dict[row.path.split('/')[11]]['r_factor'] = row.r_factor
            s100_sub1_2ox_vac_2mg_vac_dict[row.path.split('/')[11]]['red_chi_square'] = row.red_chi_sq
        except:
            print(f"{row.path} has no data")
            continue
    if row.path.split('/')[10] == 's100_sub1_2ox_vac_mg_vac':
        try:
            print(row.frechet)
            s100_sub1_2ox_vac_mg_vac_dict[row.path.split('/')[11]] = {}
            s100_sub1_2ox_vac_mg_vac_dict[row.path.split('/')[11]]['energy'] = row.energy
            s100_sub1_2ox_vac_mg_vac_dict[row.path.split('/')[11]]['frechet'] = row.frechet
            s100_sub1_2ox_vac_mg_vac_dict[row.path.split('/')[11]]['r_factor'] = row.r_factor
            s100_sub1_2ox_vac_mg_vac_dict[row.path.split('/')[11]]['red_chi_square'] = row.red_chi_sq
        except:
            print(f"{row.path} has no data")
            continue
    i += 1



sorted_s100_sub1_ox_vac_2mg_vac_dict = sorted(s100_sub1_ox_vac_2mg_vac_dict.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)
sorted_s100_sub1_mg_vac_dict = sorted(s100_sub1_mg_vac.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)
sorted_s100_sub1_ox_vac_dict = sorted(s100_sub1_ox_vac.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)
sorted_s100_sub1_ox_vac_mg_vac_dict = sorted(s100_sub1_ox_vac_mg_vac.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)
sorted_s100_sub1_2ox_vac_2mg_vac_dict = sorted(s100_sub1_2ox_vac_2mg_vac_dict.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)
sorted_s100_sub1_2ox_vac_mg_vac_dict = sorted(s100_sub1_2ox_vac_mg_vac_dict.items(), key=lambda x: x[1]['red_chi_square'], reverse=False)

print(sorted_s100_sub1_2ox_vac_2mg_vac_dict)
s100_sub1_ox_vac_mag_vac_minE = sorted_s100_sub1_ox_vac_mg_vac_dict[0][1]['energy']
s100_sub1_mg_vac_minE = sorted_s100_sub1_mg_vac_dict[0][1]['energy']
s100_sub1_ox_vac_2mg_vac_minE = sorted_s100_sub1_ox_vac_2mg_vac_dict[0][1]['energy']
s100_sub1_ox_vac_minE = sorted_s100_sub1_ox_vac_dict[0][1]['energy']
s100_sub1_2ox_vac_2mg_vac_minE = sorted_s100_sub1_2ox_vac_2mg_vac_dict[0][1]['energy']
s100_sub1_2ox_vac_mg_vac_minE = sorted_s100_sub1_2ox_vac_mg_vac_dict[0][1]['energy']



for data in sorted_s100_sub1_ox_vac_2mg_vac_dict:
    data[-1]['energy'] -= s100_sub1_ox_vac_2mg_vac_minE
for data in sorted_s100_sub1_ox_vac_mg_vac_dict:
    data[-1]['energy'] -= s100_sub1_ox_vac_mag_vac_minE
for data in sorted_s100_sub1_ox_vac_dict:
    data[-1]['energy'] -= s100_sub1_ox_vac_minE
for data in sorted_s100_sub1_mg_vac_dict:
    data[-1]['energy'] -= s100_sub1_mg_vac_minE
for data in sorted_s100_sub1_2ox_vac_2mg_vac_dict:
    data[-1]['energy'] -= s100_sub1_2ox_vac_2mg_vac_minE
for data in sorted_s100_sub1_2ox_vac_mg_vac_dict:
    data[-1]['energy'] -= s100_sub1_2ox_vac_mg_vac_minE

###########%##########
#  PLOTTING RESULTS
###########%########

# Import Library

import numpy as np
import matplotlib.pyplot as plt

# Define Data
s100_sub1_ox_vac_2mg_vac_frechet = []
s100_sub1_ox_vac_2mg_vac_red_chi_square = []
s100_sub1_ox_vac_2mg_vac_r_factor = []
s100_sub1_ox_vac_2mg_vac_energy = []
s100_sub1_ox_vac_2mg_vac_red_chi_square_surf = []
s100_sub1_ox_vac_2mg_vac_energy_surf =[]

s100_sub1_ox_vac_frechet = []
s100_sub1_ox_vac_red_chi_square = []
s100_sub1_ox_vac_r_factor = []
s100_sub1_ox_vac_energy = []

s100_sub1_mg_vac_frechet = []
s100_sub1_mg_vac_red_chi_square = []
s100_sub1_mg_vac_r_factor = []
s100_sub1_mg_vac_energy = []

s100_sub1_ox_vac_mg_vac_frechet = []
s100_sub1_ox_vac_mg_vac_red_chi_square = []
s100_sub1_ox_vac_mg_vac_r_factor = []
s100_sub1_ox_vac_mg_vac_energy = []

s100_sub1_2ox_vac_mg_vac_frechet = []
s100_sub1_2ox_vac_mg_vac_red_chi_square = []
s100_sub1_2ox_vac_mg_vac_r_factor = []
s100_sub1_2ox_vac_mg_vac_energy = []

s100_sub1_2ox_vac_2mg_vac_frechet = []
s100_sub1_2ox_vac_2mg_vac_red_chi_square = []
s100_sub1_2ox_vac_2mg_vac_r_factor = []
s100_sub1_2ox_vac_2mg_vac_energy = []

i = 0
#Location of nearest neighbors and respective indices
surf_O_indices = ['88']
surf_Mg_indices = ['39', '16', '38', '28']
sub1_O_indices = ['75', '61', '85', '86']
sub1_Mg_indices = ['46', '27', '37', '14']
sub2_O_indices = ['84']
sub2_Mg_indices = ['26', '36', '12', '35']

for data in sorted_s100_sub1_ox_vac_2mg_vac_dict:
    if i % 2 != 0:
        print(i)
        i += 1
        continue
    i += 1
    print(data[0])
    '''if data[0].split('_')[-3] in surf_O_indices \
            and data[0].split('_')[-2] in surf_Mg_indices \
            and data[0].split('_')[-1] in surf_Mg_indices:
        s100_sub1_ox_vac_2mg_vac_red_chi_square_surf.append(data[-1]['red_chi_square'])
        s100_sub1_ox_vac_2mg_vac_energy_surf.append(data[-1]['energy'])
        print(f"all surf {data[0]}")
        continue'''
    s100_sub1_ox_vac_2mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_ox_vac_2mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_ox_vac_2mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_ox_vac_2mg_vac_energy.append(data[-1]['energy'])


for data in sorted_s100_sub1_ox_vac_mg_vac_dict:
    s100_sub1_ox_vac_mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_ox_vac_mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_ox_vac_mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_ox_vac_mg_vac_energy.append(data[-1]['energy'])
for data in sorted_s100_sub1_ox_vac_dict:
    s100_sub1_ox_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_ox_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_ox_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_ox_vac_energy.append(data[-1]['energy'])
for data in sorted_s100_sub1_mg_vac_dict:
    s100_sub1_mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_mg_vac_energy.append(data[-1]['energy'])
for data in sorted_s100_sub1_2ox_vac_mg_vac_dict:
    print(data)
    s100_sub1_2ox_vac_mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_2ox_vac_mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_2ox_vac_mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_2ox_vac_mg_vac_energy.append(data[-1]['energy'])
for data in sorted_s100_sub1_2ox_vac_2mg_vac_dict:
    s100_sub1_2ox_vac_2mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_2ox_vac_2mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_2ox_vac_2mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_2ox_vac_2mg_vac_energy.append(data[-1]['energy'])

#x_s100_sub1_ox_vac_2mg_vac_surf = np.arange(len(s100_sub1_ox_vac_2mg_vac_energy_surf)) + 1
#print(x_s100_sub1_ox_vac_2mg_vac_surf)
x_s100_sub1_ox_vac_2mg_vac = np.arange(len(s100_sub1_ox_vac_2mg_vac_energy))
x_s100_sub1_ox_vac_mg_vac = np.arange(len(s100_sub1_ox_vac_mg_vac_energy))
x_s100_sub1_ox_vac = np.arange(len(s100_sub1_ox_vac_energy))
x_s100_sub1_mg_vac = np.arange(len(s100_sub1_mg_vac_energy))
x_s100_sub1_2ox_vac_mg_vac = np.arange(len(s100_sub1_2ox_vac_mg_vac_energy))
x_s100_sub1_2ox_vac_2mg_vac = np.arange(len(s100_sub1_2ox_vac_2mg_vac_energy))
# Create Plot

fig, ax1 = plt.subplots(3, 2)
plt.figure(figsize=(14,10))
plt.tight_layout(pad=5)
y_lim_red_chi_sq = 50
#ax1.figure(figsize = (10, 5))
#print(s100_sub1_ox_vac_2mg_vac_energy_surf)
#ax1[:,:].set_xlabel('Configuration',fontweight='bold', fontsize=11)
#ax1[:,:].set_ylabel('red_chi_square', color='black')
ax1[1, 1].bar(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_red_chi_square,
              color='red')
#ax1[1, 1].bar(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_energy,
#              color='yellow')
ax1[1, 1].set_title('s100_sub1_ox_vac_2mg_vac')
ax1[1, 1].set_ylim([0, y_lim_red_chi_sq])
#ax1[1, 1].set_xlim([0, 10])

ax1[1, 0].bar(x_s100_sub1_ox_vac_mg_vac, s100_sub1_ox_vac_mg_vac_red_chi_square, color = 'purple')
ax1[1, 0].set_title('s100_sub1_ox_vac_mg_vac')
ax1[1, 0].set_ylim([0, y_lim_red_chi_sq])
#ax1[1, 0].set_xlim([0, 10])

ax1[0, 0].bar(x_s100_sub1_ox_vac, s100_sub1_ox_vac_red_chi_square, color = 'orange')
ax1[0, 0].set_title('s100_sub1_ox_vac')
ax1[0, 0].set_ylim([0, y_lim_red_chi_sq])

ax1[0, 1].bar(x_s100_sub1_mg_vac, s100_sub1_mg_vac_red_chi_square, color= 'green')
ax1[0, 1].set_title('s100_sub1_mg_vac')
ax1[0, 1].set_ylim([0, y_lim_red_chi_sq])

ax1[2, 0].bar(x_s100_sub1_2ox_vac_mg_vac, s100_sub1_2ox_vac_mg_vac_red_chi_square, color = 'green')
ax1[2, 0].set_title('s100_sub1_2ox_vac_mg_vac')
ax1[2, 0].set_ylim([0, y_lim_red_chi_sq])
#ax1[2, 0].set_xlim([0, 8])

ax1[2, 1].bar(x_s100_sub1_2ox_vac_2mg_vac, s100_sub1_2ox_vac_2mg_vac_red_chi_square, color = 'orange')
ax1[2, 1].set_title('s100_sub1_2ox_vac_2mg_vac')
ax1[2, 1].set_ylim([0, y_lim_red_chi_sq])
#ax1[2, 1].set_xlim([0, 50])


print(ax1)
#ax1.tick_params(axis='y')
#plt.legend(fontsize= 6)

# Adding Twin Axes
ax2 = ax1.copy()
print(ax2)
ax2[1, 1] = ax1[1, 1].twinx()
#ax2[1, 1].plot(x_s100_sub1_ox_vac_2mg_vac,
#               s100_sub1_ox_vac_2mg_vac_red_chi_square_surf, color='blue')
ax2[1, 1].plot(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_frechet, color='blue')
ax2[1 ,0] = ax1[1, 0].twinx()
ax2[1, 0].plot(x_s100_sub1_ox_vac_mg_vac, s100_sub1_ox_vac_mg_vac_frechet, color = 'blue')
ax2[0, 0] = ax1[0, 0].twinx()
ax2[0, 0].plot(x_s100_sub1_ox_vac, s100_sub1_ox_vac_frechet, color = 'blue')
ax2[0, 1] = ax1[0, 1].twinx()
ax2[0, 1].plot(x_s100_sub1_mg_vac, s100_sub1_mg_vac_frechet, color='blue')
ax2[2, 0] = ax1[2, 0].twinx()
ax2[2, 0].plot(x_s100_sub1_2ox_vac_mg_vac, s100_sub1_2ox_vac_mg_vac_frechet, color='blue')
ax2[2, 1] = ax1[2, 1].twinx()
ax2[2, 1].plot(x_s100_sub1_2ox_vac_2mg_vac, s100_sub1_2ox_vac_2mg_vac_frechet, color='blue')
#ax2[2, 1].set_ylim([0, 70])
#ax2[:,:].tick_params(axis='y')

for ax in ax1[:, 0].flat:
    ax.set(ylabel='Red Chi Squared')
for ax in ax1[2, :].flat:
    ax.set(xlabel='Config')
for ax in ax1[0:2,:].flat:
    #ax.get_xaxis().set_visible(False)
    ax.get_xaxis().set_ticklabels([])
for ax in ax2[:,1].flat:
    ax.set(ylabel='Frechet')
for ax in ax1[:, 1].flat:
    ax.get_yaxis().set_ticklabels([])
#plt.title('exafs_fitting_vacancy_study_reduced_data', fontweight='bold', fontsize=12)

# Show plot

#ax1[1, 1].legend()
plt.show()