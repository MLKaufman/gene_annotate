# gene_annotate
### CLI tool to annotate csv or tsv files containing a column of gene symbols. Outputs formal gene name and protein function/class to table.  
<HR>  

## Installation:  

Prefered method of installation using pipx: https://pypa.github.io/pipx/  
```  
pip install pipx  

pipx install git+https://github.com/MLKaufman/gene_annotate.git
```

## Example Usage:

```
usage: gene_annotate.py [-h] [-i] [-s SPECIES] [-a ANNOTATEMODE] [-c COLUMN]

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactivemode
                        activate interactive mode
  -s SPECIES, --species SPECIES
                        species to use; defualt = human; currently
                        supported:human,mouse,gallus,danio
  -a ANNOTATEMODE, --annotatemode ANNOTATEMODE
                        input file to annotate (csv or tsv)
  -c COLUMN, --column COLUMN
                        column # to use for getting gene symbol for annotating
```
