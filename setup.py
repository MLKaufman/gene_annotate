from gene_annotate import setup

setup(
    name='gene_annotate',
    version='1.0,
    entry_points={
        'console_scripts': ['gene_annotate=gene_annotate.gene_annotate:main']
    }
)
