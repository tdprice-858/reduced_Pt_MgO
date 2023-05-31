import os

from ase.neighborlist import natural_cutoffs, NeighborList
from ase.io import read, write
from ase.visualize import view

input_structure = '/Users/tdprice/Desktop/02_pt-mgo-ethylene/\
24_s100_sub1_bare/small_unit_cell/opt_PBE_400_221/vasprun.xml'
element_of_interest = 'Pt'
vacancies={'Mg':2, 'O':1}
rootdir = '/Users/tdprice/Documents/py/code/submission/structures'
script = '/Users/tdprice/Documents/py/code/submission/structures/opt_submit_job.py'
os.chdir(rootdir)
def tag_nearest_neighbors(input_structure, element_of_interest='Pt'):
    atoms = read(input_structure)
    pt_index = [a.index for a in atoms if a.symbol == element_of_interest]
    cutoff = natural_cutoffs(atoms)
    #The problem with the following line is that it will generate two Pt atoms in the file traj
    nl = NeighborList(cutoff, bothways=True, self_interaction=True)
    # assign labels to all the neighbors in a list
    nl.update(atoms)
    neigh = nl.get_neighbors(pt_index[0])[0]
    ox_tags = [i for i in range(1, 7, 1)]
    mg_tags = [i for i in range(1, 13, 1)]
    i= 0
    j = 0
    ox_tag_neigh_dict = {}
    mg_tag_neigh_dict = {}
    for atom in atoms:
        if atom.index in neigh and atom.symbol == 'O':
            atom.tag = ox_tags[i]
            i += 1
            ox_tag_neigh_dict[f"{atom.tag}"] = atom.index
        elif atom.index in neigh and atom.symbol == 'Mg':
            atom.tag = mg_tags[j]
            j += 1
            mg_tag_neigh_dict[f"{atom.tag}"] = atom.index
        elif atom.index == 88:
            atom.tag = ox_tags[i]
            i += 1
            ox_tag_neigh_dict[f"{atom.tag}"] = atom.index
        else:
            continue
    return atoms, neigh, ox_tag_neigh_dict, mg_tag_neigh_dict

atoms, neigh, ox_tag_neigh_dict, mg_tag_neigh_dict = \
    tag_nearest_neighbors(input_structure, element_of_interest)
print(neigh)
for atom in atoms:
    atoms_cp = atoms.copy()
    if atom.tag != 0 and atom.symbol=='O':
        index = atom.index
        del atoms_cp[[atom.index]]
        if not os.path.exists(f"{rootdir}/s100_sub1_ox_vac"):
            os.system(f"mkdir s100_sub1_ox_vac")
        os.chdir('s100_sub1_ox_vac')
        if not os.path.exists(f"{rootdir}/s100_sub1_ox_vac_{index}"):
            os.system(f"mkdir s100_sub1_ox_vac_{index}")
        os.chdir(f"s100_sub1_ox_vac_{index}")
        os.system(f"cp {script} .")
        write(f"s100_sub1_ox_vac_{index}.traj", atoms_cp)
        os.system(f"mv s100_sub1_ox_vac_{index}.traj start.traj")
        #os.system('sbatch opt_submit_job.py')
        os.chdir(rootdir)
        for atom in atoms_cp:
            atoms_cp_cp = atoms_cp.copy()
            if atom.tag != 0 and atom.symbol == 'Mg':
                tag = atom.tag
                del atoms_cp_cp[[atom.index]]
                if not os.path.exists(f"{rootdir}/s100_sub1_ox_vac_mg_vac"):
                    os.system(f"mkdir s100_sub1_ox_vac_mg_vac")
                os.chdir('s100_sub1_ox_vac_mg_vac')
                if not os.path.exists(f'{rootdir}/s100_sub1_ox_vac_mg_vac/s100_sub1_ox_vac_mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}'):
                    os.system(f'mkdir s100_sub1_ox_vac_mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}')
                os.chdir(f's100_sub1_ox_vac_mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}')
                os.system(f"cp {script} .")
                write(f's100_sub1_ox_vac_mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}.traj', atoms_cp_cp)
                os.system(f'mv s100_sub1_ox_vac_mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}.traj start.traj')
                # os.system('sbatch opt_submit_job.py')
                os.chdir(rootdir)
                for atom in atoms_cp_cp:
                    new_tag = atom.tag
                    atoms_cp_cp_cp = atoms_cp_cp.copy()
                    if not os.path.exists(f"{rootdir}/s100_sub1_ox_vac_2mg_vac"):
                        os.system(f"mkdir s100_sub1_ox_vac_2mg_vac")
                    os.chdir('s100_sub1_ox_vac_2mg_vac')

                    if atom.tag != 0 and atom.symbol == 'Mg':
                        if not os.path.exists(
                                f'{rootdir}/s100_sub1_ox_vac_2mg_vac/s100_sub1_ox_vac_2mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}_{mg_tag_neigh_dict[f"{new_tag}"]}'):
                            os.system(
                                f'mkdir s100_sub1_ox_vac_2mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}_{mg_tag_neigh_dict[f"{new_tag}"]}')
                        os.chdir(
                            f's100_sub1_ox_vac_2mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}_{mg_tag_neigh_dict[f"{new_tag}"]}')
                        del atoms_cp_cp_cp[[atom.index]]
                        os.system(f"cp {script} .")
                        write(f's100_sub1_ox_vac_2mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}_{mg_tag_neigh_dict[f"{new_tag}"]}.traj', atoms_cp_cp_cp)
                        os.system(f'mv s100_sub1_ox_vac_2mg_vac_{index}_{mg_tag_neigh_dict[f"{tag}"]}_{mg_tag_neigh_dict[f"{new_tag}"]}.traj start.traj')
                        # os.system('sbatch opt_submit_job.py')
                    os.chdir(rootdir)
    elif atom.tag !=0 and atom.symbol=='Mg':
        os.chdir(rootdir)
        if not os.path.exists(f"{rootdir}/s100_sub1_mg_vac"):
            os.system(f"mkdir s100_sub1_mg_vac")
        os.chdir('s100_sub1_mg_vac')
        index = atom.index
        del atoms_cp[[atom.index]]
        if not os.path.exists(f"{rootdir}/s100_sub1_mg_vac/s100_sub1_mg_vac_{index}"):
            os.system(f"mkdir s100_sub1_mg_vac_{index}")
        os.chdir(f's100_sub1_mg_vac_{index}')
        os.system(f"cp {script} .")
        write(f"s100_sub1_mg_vac_{index}.traj", atoms_cp)
        os.system(f"mv s100_sub1_mg_vac_{index}.traj start.traj")
        # os.system('sbatch opt_submit_job.py')
        os.chdir(rootdir)
    else:
       continue



