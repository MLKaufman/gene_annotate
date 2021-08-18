import os
import argparse
import pandas as pd

if os.name == 'nt':
    import pyreadline # non-standard library input history
else:
    import readline # for input history; does not work in windows

os.chdir(os.path.dirname(os.path.abspath(__file__)))

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interactivemode", action='store_true', help= "activate interactive mode") #file to annotate
parser.add_argument("-s", "--species", help="species to use; defualt = human; currently supported:human,mouse,gallus,danio", default = 'human', type = str)
parser.add_argument("-a", "--annotatemode", help="input file to annotate (csv or tsv)", default = None, type = str)
parser.add_argument("-c", "--column", help="column # to use for getting gene symbol for annotating", default = 0, type = int)

argument = parser.parse_args()

database_path = 'databases' + os.sep

def load_species_db(species):
    if species == "human":
        df = pd.read_csv(database_path + 'genelist_human_complete_12032019.csv', header=0, sep=',')
    if species == "mouse":
        df = pd.read_csv(database_path + 'genelist_mouse_complete_12032019.csv', header=0, sep=',')
    if species == "gallus":
        df = pd.read_csv(database_path + 'genelist_gallus_complete_12032019.csv', header=0, sep=',')
    if species == "danio":
        df = pd.read_csv(database_path + 'genelist_danio_complete_12032019.csv', header=0, sep=',')
    return df

    
##TODO:
### Function Block - For importing as module ###
def return_match_single(gene, species):
    results = {}
    df = load_species_db(species)

    return results

def return_match_list(gene_list, species):
    results = {}

    df = load_species_db(species)

    return results

def return_specific(gene, species, record):
    results = {}

    df = load_species_db(species)

    return results
###

def main():
    # run file as a script
    if argument.interactivemode is True:
        df = load_species_db(argument.species) # load species database
        print("Activating Interactive Mode")
        print("Species: " + argument.species)

        exit_mode = False
        
        while exit_mode is False:
            gene = input("Enter a gene symbol, (or Q to quit):")

            if gene == 'q' or gene == 'Q':
                break
            # ensure proper species conversion of gene name
            if argument.species == 'human': gene = gene.upper()
            if argument.species == 'mouse': gene = gene.title()
            if argument.species == 'gallus': gene = gene.upper()
            if argument.species == 'danio': gene = gene.lower()

            # search for gene
            print(gene)
            print(df[df['Gene_Symbol'].str.contains(gene)][['Gene_Symbol', 'Gene_Name', 'Protein_Class', 'Molecular_Function']])

    elif argument.annotatemode is not None: # annotate file; need column to scan for genes; tack on annotations to right column
        df = load_species_db(argument.species) # load species database
        print("Annotating File")
        print("Species: " + argument.species)


        indexed_annotation = [x[:-1] for x in df['Gene_Symbol']]

        #load file
        file_path = argument.annotatemode
        an_df = pd.read_table(file_path, header=0)

        # add columns to loaded df
            # default: Gene_Name, Protein_Class
            # full: deafult + Molecular_Function + Biological_Process + Cellular_Component
            # vs: MF_Complete + BP_Complete + CC_Complete

        an_df['Gene_Name'] = ""
        an_df['Protein_Class'] = ""
        an_df['Molecular_Function'] = ""
        an_df['Biological_Process'] = ""
        an_df['Cellular_Component'] = ""

        entries = 0
        failed = 0
        for index, row in an_df.iterrows():

            try:
                annotation_index = indexed_annotation.index(row[argument.column])

                an_df.loc[index, 'Gene_Name'] = df['Gene_Name'][annotation_index]
                an_df.loc[index, 'Protein_Class'] = df['Protein_Class'][annotation_index]
                an_df.loc[index, 'Molecular_Function'] = df['Molecular_Function'][annotation_index]
                an_df.loc[index, 'Biological_Process'] = df['Biological_Process'][annotation_index]

                entries+=1

            except ValueError:
                print(row[argument.column], "was not found in database.")
                failed+=1

        print('')
        print('Added annotations for', entries)
        print('Failed for', failed)

        an_df.to_csv(file_path + '_annotated.csv', index=False)

        # save a copy of file with _annotated.<file_extension>

if __name__ == "__main__":
    main()