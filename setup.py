from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]

setup(
    name='gene_annotate',
    version='1.0',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    package_dir={'gene_annotate': 'gene_annotate'},
    include_package_data=True,
    entry_points={'console_scripts': ['gene_annotate=gene_annotate.gene_annotate:main']},
    python_requires=">=3.6",
    install_requires=["pandas", "setuptools-git"]
)