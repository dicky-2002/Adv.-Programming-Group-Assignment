# %% import libraries:
import matplotlib.pyplot as plt
import pandas as pd
#rdkit libs:
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem as Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
from rdkit.Chem import Descriptors, AllChem
from rdkit.ML.Descriptors import MoleculeDescriptors
# %% Data preprocessing:

df_tested_mol = pd.read_csv('tested_molecules.csv')
df_backup_original_data=df_tested_mol.copy()

# #check for duplicates:
# duplicates = df_tested_mol.duplicated()
# duplicate_count = duplicates.sum()

# #check for empty rows:
# empty_rows = df_tested_mol.isnull()
# empty_count = empty_rows.sum()

# #check for NAN:
# Nan_bool = df_tested_mol.notna()
# nan_count = Nan_bool.sum()

def get_descriptor_names_and_functions():
    descriptor_names = [desc[0] for desc in Descriptors.descList]
    descriptor_functions = [desc[1] for desc in Descriptors.descList]
    df_descriptors=pd.DataFrame({'names': descriptor_names, 'functions': descriptor_functions})
    
    return df_descriptors


# Define a function to convert SMILES to molecular descriptors
def get_general_descriptors_from_smiles(smiles):
    mol = Chem.MolFromSmiles(smiles)
    df_general_descriptors = get_descriptor_names_and_functions()
    if mol:
        descriptors = [func(mol) for func in df_general_descriptors["functions"]]
        return descriptors
    else:
        return [None] * len(df_general_descriptors["functions"])


def smiles_to_descriptors_for_df(df, show_head=False):
    df=df.copy()          
    df_general_descriptors = get_descriptor_names_and_functions()

    #create empty df for descriptors and go over every molecule 
    #and write descriptors to this df:
    df_descriptors=pd.DataFrame(columns=df_general_descriptors["names"])
    for smls in df["SMILES"]:
        Descriptors=get_general_descriptors_from_smiles(smls)
        new_descriptors=pd.DataFrame([Descriptors],columns=df_general_descriptors['names'])
        df_descriptors=pd.concat([df_descriptors, new_descriptors], axis=0, ignore_index=True)                             
    df = pd.concat([df, df_descriptors], axis=1)

    if show_head == True:
        print(df.head())
    return df


df_molecules_with_descriptors=smiles_to_descriptors_for_df(df_tested_mol)
