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
        print(row.path)
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
print(sorted_s100_sub1_ox_vac_2mg_vac_dict)

sorted_s100_sub1_ox_vac_2mg_vac_dict = sorted(s100_sub1_ox_vac_2mg_vac_dict.items(), key=lambda x: x[1]['energy'], reverse=False)
sorted_s100_sub1_mg_vac_dict = sorted(s100_sub1_mg_vac.items(), key=lambda x: x[1]['energy'], reverse=False)
sorted_s100_sub1_ox_vac_dict = sorted(s100_sub1_ox_vac.items(), key=lambda x: x[1]['energy'], reverse=False)
sorted_s100_sub1_ox_vac_mg_vac_dict = sorted(s100_sub1_ox_vac_mg_vac.items(), key=lambda x: x[1]['energy'], reverse=False)
sorted_s100_sub1_2ox_vac_2mg_vac_dict = sorted(s100_sub1_2ox_vac_2mg_vac_dict.items(), key=lambda x: x[1]['energy'], reverse=False)
sorted_s100_sub1_2ox_vac_mg_vac_dict = sorted(s100_sub1_2ox_vac_mg_vac_dict.items(), key=lambda x: x[1]['energy'], reverse=False)

#print(sorted_s100_sub1_2ox_vac_2mg_vac_dict)
print(sorted_s100_sub1_ox_vac_2mg_vac_dict)

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

def boltzmann_factor(E, T):
    '''
    Function for calculating Boltzmann factors.

    Parameters:
        E: Energy; eV
        Scalar or vector

        T: Temperature; Kelvin
        Scalar

    Output:
        Boltzmann Factor
    '''

    #Boltzmann Constant
    k = 1.3806526 * 10**(-23) # [J/K]
    joule = 6.242 * 10**(18) # eV
    k *= joule


    b_f = np.exp((-E) / (k * T))
    return b_f

T = 170 + 273.15



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
        i += 1
        continue
    i += 1
    #if data[0].split('_')[-3] in surf_O_indices \
    #        and data[0].split('_')[-2] in surf_Mg_indices \
    #         and data[0].split('_')[-1] in surf_Mg_indices:
    #    s100_sub1_ox_vac_2mg_vac_red_chi_square_surf.append(data[-1]['red_chi_square'])
    #    s100_sub1_ox_vac_2mg_vac_energy_surf.append(data[-1]['energy'])
    #    continue

    s100_sub1_ox_vac_2mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_ox_vac_2mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_ox_vac_2mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_ox_vac_2mg_vac_energy.append(data[-1]['energy'])
    #print(data[0], 'structure')
    #print(data[-1]['energy'])
    #print(data[-1]['red_chi_square'])
    print(data[0], 'structure')
    print(data[-1]['energy'])
    print(data[-1]['red_chi_square'])
    print(boltzmann_factor(np.array(data[-1]['energy']), T))


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
    s100_sub1_2ox_vac_mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_2ox_vac_mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_2ox_vac_mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_2ox_vac_mg_vac_energy.append(data[-1]['energy'])

for data in sorted_s100_sub1_2ox_vac_2mg_vac_dict:
    s100_sub1_2ox_vac_2mg_vac_r_factor.append(data[-1]['r_factor'])
    s100_sub1_2ox_vac_2mg_vac_frechet.append(data[-1]['frechet'])
    s100_sub1_2ox_vac_2mg_vac_red_chi_square.append(data[-1]['red_chi_square'])
    s100_sub1_2ox_vac_2mg_vac_energy.append(data[-1]['energy'])
    #print(data[0], 'structure')
    #print(data[-1]['energy'])
    #print(data[0], 'structure')
    #print(data[-1]['energy'])

x_s100_sub1_ox_vac_2mg_vac_surf = np.arange(len(s100_sub1_ox_vac_2mg_vac_energy_surf))

#x_s100_sub1_ox_vac_2mg_vac = np.arange(len(s100_sub1_ox_vac_2mg_vac_energy)) \
#                             + x_s100_sub1_ox_vac_2mg_vac_surf[-1] + 1
x_s100_sub1_ox_vac_mg_vac = np.arange(len(s100_sub1_ox_vac_mg_vac_energy))
x_s100_sub1_ox_vac = np.arange(len(s100_sub1_ox_vac_energy))
x_s100_sub1_mg_vac = np.arange(len(s100_sub1_mg_vac_energy))
x_s100_sub1_2ox_vac_mg_vac = np.arange(len(s100_sub1_2ox_vac_mg_vac_energy))
x_s100_sub1_2ox_vac_2mg_vac = np.arange(len(s100_sub1_2ox_vac_2mg_vac_energy))

s100_sub1_mg_vac_BF = boltzmann_factor(np.array(s100_sub1_mg_vac_energy),  T)
s100_sub1_ox_vac_BF = boltzmann_factor(np.array(s100_sub1_ox_vac_energy), T)
s100_sub1_ox_vac_mg_vac_BF = boltzmann_factor(np.array(s100_sub1_ox_vac_mg_vac_energy), T)
s100_sub1_2ox_vac_mg_vac_BF = boltzmann_factor(np.array(s100_sub1_2ox_vac_mg_vac_energy), T)
s100_sub1_ox_vac_2mg_vac_BF = boltzmann_factor(np.array(s100_sub1_ox_vac_2mg_vac_energy), T)
s100_sub1_2ox_vac_2mg_vac_BF = boltzmann_factor(np.array(s100_sub1_2ox_vac_2mg_vac_energy), T)
#print(s100_sub1_ox_vac_2mg_vac_BF, 'Boltzmann Factor')

#print(s100_sub1_2ox_vac_2mg_vac_BF, 'Boltzmann factor')
# Create Plot

fig, ax1 = plt.subplots(3, 2)
plt.figure(figsize=(14,10))
plt.tight_layout(pad=2)

x = [10**-6 * 100**x for x in range(0,4, 1)]

#ax1.figure(figsize = (10, 5))
#ax1[:,:].set_xlabel('Configuration',fontweight='bold', fontsize=11)
#ax1[:,:].set_ylabel('red_chi_square', color='black')
ax1[1, 1].scatter(s100_sub1_ox_vac_2mg_vac_BF, s100_sub1_ox_vac_2mg_vac_red_chi_square,
              color='red')#, label='Surf vacancies')
#ax1[1, 1].bar(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_energy,
#              color='yellow')
ax1[1, 1].set_title('s100_sub1_ox_vac_2mg_vac')
ax1[1, 1].set_ylim([0.0, 50])



ax1[1, 0].scatter(s100_sub1_ox_vac_mg_vac_BF, s100_sub1_ox_vac_mg_vac_red_chi_square, color = 'purple')
ax1[1, 0].set_title('s100_sub1_ox_vac_mg_vac')

#ax1[1, 0].set_ylim([0, 1.0])
#ax1[1, 0].set_xlim([0, 10])

ax1[0, 0].scatter(s100_sub1_ox_vac_BF, s100_sub1_ox_vac_red_chi_square, color = 'orange')
ax1[0, 0].set_title('s100_sub1_ox_vac')
ax1[0, 0].set_xscale('symlog')
#ax1[0, 0].set_ylim([0, 1.0])

ax1[0, 1].scatter(s100_sub1_mg_vac_BF, s100_sub1_mg_vac_red_chi_square, color= 'green')
ax1[0, 1].set_title('s100_sub1_mg_vac')

#ax1[0, 1].set_ylim([0, 1.0])

ax1[2, 0].scatter(s100_sub1_2ox_vac_mg_vac_BF, s100_sub1_2ox_vac_mg_vac_red_chi_square, color = 'green')
ax1[2, 0].set_title('s100_sub1_2ox_vac_mg_vac')

#ax1[2, 0].set_ylim([0, 1.0])
#ax1[2, 0].set_xlim([0, 8])

ax1[2, 1].scatter(s100_sub1_2ox_vac_2mg_vac_BF, s100_sub1_2ox_vac_2mg_vac_red_chi_square, color = 'orange')
ax1[2, 1].set_title('s100_sub1_2ox_vac_2mg_vac')
ax1[2, 1].set_ylim([0, 50])

#ax1[2, 1].set_xlim([0, 50])


#ax1.tick_params(axis='y')
#plt.legend(fontsize= 6)
'''
# Adding Twin Axes
ax2 = ax1.copy()
print(ax2)
ax2[1, 1] = ax1[1, 1].twinx()
ax2[1, 1].plot(x_s100_sub1_ox_vac_2mg_vac_surf,
               s100_sub1_ox_vac_2mg_vac_red_chi_square_surf, color='blue')
ax2[1, 1].plot(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_red_chi_square, color='blue')
ax2[1 ,0] = ax1[1, 0].twinx()
ax2[1, 0].plot(x_s100_sub1_ox_vac_mg_vac, s100_sub1_ox_vac_mg_vac_red_chi_square, color = 'blue')
ax2[0, 0] = ax1[0, 0].twinx()
ax2[0, 0].plot(x_s100_sub1_ox_vac, s100_sub1_ox_vac_red_chi_square, color = 'blue')
ax2[0, 1] = ax1[0, 1].twinx()
ax2[0, 1].plot(x_s100_sub1_mg_vac, s100_sub1_mg_vac_red_chi_square, color='blue')
ax2[2, 0] = ax1[2, 0].twinx()
ax2[2, 0].plot(x_s100_sub1_2ox_vac_mg_vac, s100_sub1_2ox_vac_mg_vac_red_chi_square, color='blue')
ax2[2, 1] = ax1[2, 1].twinx()
ax2[2, 1].plot(x_s100_sub1_2ox_vac_2mg_vac, s100_sub1_2ox_vac_2mg_vac_red_chi_square, color='blue')
ax2[2, 1].set_ylim([0, 70])
#ax2[:,:].tick_params(axis='y')'''

for ax in ax1[:, 0].flat:
    ax.set(ylabel='Red Chi Squared')
    #ax.label_outer()
for ax in ax1[2, :].flat:
    ax.set(xlabel='Boltzmann Factor')
    #ax.set_xticks(x)
for ax in ax1[:, :].flat:
    ax.set_xscale('log')
    ax.set_xlim([10**-6, 2])
    ax.set_xticks(x)
for ax in ax1[0:2,:].flat:
    #ax.get_xaxis().set_visible(False)
    ax.get_xaxis().set_ticklabels([])
    ax.set_xticks([])

    #ax.label_outer()
#for ax in ax2[:, 1].flat:
#    ax.set(xlabel='Config', ylabel='Red Chi Sq')
#    #ax.label_outer()
#for ax in ax1.flat:
#    ax.label_outer()


#plt.title('exafs_fitting_vacancy_study_reduced_data', fontweight='bold', fontsize=12)

# Show plot

#ax1[1, 1].legend()

plt.show()

'''# Create Plot

fig, ax1 = plt.subplots(2, 2)
#ax1.figure(figsize = (10, 5))

#ax1[:,:].set_xlabel('Configuration',fontweight='bold', fontsize=11)
#ax1[:,:].set_ylabel('red_chi_square', color='black')
#ax1[0, 0].plot(s100_sub1_ox_vac_2mg_vac_red_chi_square, s100_sub1_ox_vac_2mg_vac_energy, color='red')
#ax1[0, 0].set_title('s100_sub1_ox_vac_2mg_vac')
#ax1[0, 1].plot(s100_sub1_ox_vac_mg_vac_red_chi_square, s100_sub1_ox_vac_mg_vac_energy, color = 'purple')
##ax1[0, 1].set_title('s100_sub1_ox_vac_mg_vac')
#ax1[1, 0].plot(s100_sub1_ox_vac_red_chi_square, s100_sub1_ox_vac_energy, color = 'orange')
##ax1[1, 0].set_title('s100_sub1_ox_vac')
#ax1[1, 1].plot(s100_sub1_mg_vac_red_chi_square, s100_sub1_mg_vac_energy, color= 'green')
#ax1[1, 1].set_title('s100_sub1_mg_vac')

print(ax1)
#ax1.tick_params(axis='y')
#plt.legend(fontsize= 6)

# Adding Twin Axes
ax2 = ax1.copy()
print(ax2)
ax2[0, 0] = ax1[0, 0].twinx()
ax2[0, 0].plot(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_red_chi_square, color='blue')
ax2[0, 1] = ax1[0, 1].twinx()
ax2[0, 1].plot(x_s100_sub1_ox_vac_mg_vac, s100_sub1_ox_vac_mg_vac_red_chi_square, color = 'blue')
ax2[1, 0] = ax1[1, 0].twinx()
ax2[1, 0].plot(x_s100_sub1_ox_vac, s100_sub1_ox_vac_red_chi_square, color = 'blue')
ax2[1, 1] = ax1[1, 1].twinx()
ax2[1, 1].plot(x_s100_sub1_mg_vac, s100_sub1_mg_vac_red_chi_square, color='blue')
#ax2[:,:].tick_params(axis='y')
for ax in ax1.flat:
    ax.set(xlabel='Config', ylabel='Energy')
for ax in ax2[:, 1].flat:
    ax.set(xlabel='Config', ylabel='Red Chi Sq')
    #ax.label_outer()
for ax in ax1.flat:
    ax.label_outer()


#plt.title('exafs_fitting_vacancy_study_reduced_data', fontweight='bold', fontsize=12)

# Show plot

plt.show()'''

# Create Plot

fig, ax1 = plt.subplots(3, 2)
plt.figure(figsize=(14,10))
plt.tight_layout(pad=2)

#ax1.figure(figsize = (10, 5))
#ax1[:,:].set_xlabel('Configuration',fontweight='bold', fontsize=11)
#ax1[:,:].set_ylabel('red_chi_square', color='black')
ax1[1, 1].scatter(s100_sub1_ox_vac_2mg_vac_energy, s100_sub1_ox_vac_2mg_vac_red_chi_square,
              color='red')#, label='Surf vacancies')
#ax1[1, 1].bar(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_energy,
#              color='yellow')
ax1[1, 1].set_title('s100_sub1_ox_vac_2mg_vac')
ax1[1, 1].set_ylim([0.0, 50])
ax1[1, 1].set_xlim([0, 5])

ax1[1, 0].scatter(s100_sub1_ox_vac_mg_vac_energy, s100_sub1_ox_vac_mg_vac_red_chi_square, color = 'purple')
ax1[1, 0].set_title('s100_sub1_ox_vac_mg_vac')
#ax1[1, 0].set_ylim([0, 1.0])
ax1[1, 0].set_xlim([0, 5])

ax1[0, 0].scatter(s100_sub1_ox_vac_energy, s100_sub1_ox_vac_red_chi_square, color = 'orange')
ax1[0, 0].set_title('s100_sub1_ox_vac')
#ax1[0, 0].set_ylim([0, 1.0])
ax1[0, 0].set_xlim([0, 5])

ax1[0, 1].scatter(s100_sub1_mg_vac_energy, s100_sub1_mg_vac_red_chi_square, color= 'green')
ax1[0, 1].set_title('s100_sub1_mg_vac')
#ax1[0, 1].set_ylim([0, 1.0])
ax1[0, 1].set_xlim([0, 5])

ax1[2, 0].scatter(s100_sub1_2ox_vac_mg_vac_energy, s100_sub1_2ox_vac_mg_vac_red_chi_square, color = 'green')
ax1[2, 0].set_title('s100_sub1_2ox_vac_mg_vac')
#ax1[2, 0].set_ylim([0, 1.0])
ax1[2, 0].set_xlim([0, 5])

ax1[2, 1].scatter(s100_sub1_2ox_vac_2mg_vac_energy, s100_sub1_2ox_vac_2mg_vac_red_chi_square, color = 'orange')
ax1[2, 1].set_title('s100_sub1_2ox_vac_2mg_vac')
ax1[2, 1].set_ylim([0, 50])
ax1[2, 1].set_xlim([0, 5])


#ax1.tick_params(axis='y')
#plt.legend(fontsize= 6)
'''
# Adding Twin Axes
ax2 = ax1.copy()
print(ax2)
ax2[1, 1] = ax1[1, 1].twinx()
ax2[1, 1].plot(x_s100_sub1_ox_vac_2mg_vac_surf,
               s100_sub1_ox_vac_2mg_vac_red_chi_square_surf, color='blue')
ax2[1, 1].plot(x_s100_sub1_ox_vac_2mg_vac, s100_sub1_ox_vac_2mg_vac_red_chi_square, color='blue')
ax2[1 ,0] = ax1[1, 0].twinx()
ax2[1, 0].plot(x_s100_sub1_ox_vac_mg_vac, s100_sub1_ox_vac_mg_vac_red_chi_square, color = 'blue')
ax2[0, 0] = ax1[0, 0].twinx()
ax2[0, 0].plot(x_s100_sub1_ox_vac, s100_sub1_ox_vac_red_chi_square, color = 'blue')
ax2[0, 1] = ax1[0, 1].twinx()
ax2[0, 1].plot(x_s100_sub1_mg_vac, s100_sub1_mg_vac_red_chi_square, color='blue')
ax2[2, 0] = ax1[2, 0].twinx()
ax2[2, 0].plot(x_s100_sub1_2ox_vac_mg_vac, s100_sub1_2ox_vac_mg_vac_red_chi_square, color='blue')
ax2[2, 1] = ax1[2, 1].twinx()
ax2[2, 1].plot(x_s100_sub1_2ox_vac_2mg_vac, s100_sub1_2ox_vac_2mg_vac_red_chi_square, color='blue')
ax2[2, 1].set_ylim([0, 70])
#ax2[:,:].tick_params(axis='y')'''

for ax in ax1[:, 0].flat:
    ax.set(ylabel='Red Chi Squared')
    #ax.label_outer()
for ax in ax1[2, :].flat:
    ax.set(xlabel='Relative Energy (eV)')
for ax in ax1[0:2,:].flat:
    #ax.get_xaxis().set_visible(False)
    ax.get_xaxis().set_ticklabels([])
#for ax in ax2[:, 1].flat:
#    ax.set(xlabel='Config', ylabel='Red Chi Sq')
#    #ax.label_outer()
#for ax in ax1.flat:
#    ax.label_outer()


#plt.title('exafs_fitting_vacancy_study_reduced_data', fontweight='bold', fontsize=12)

# Show plot

#ax1[1, 1].legend()
plt.show()