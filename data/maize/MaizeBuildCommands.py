#########
# Maize #
#########

import camoco as co
import pandas as pd

# Build the RefGen
co.RefGen.from_gff(
    'RefGen/ZmB73_5b_FGS.gff.gz',
    'Zm5bFGS',
    'Maize 5b Filtered Gene Set',
    '5b',
    'Zea Mays'
)

# Get the RefGen
Zm5bFGS = co.RefGen('Zm5bFGS')

# Add the aliases
Zm5bFGS.add_aliases('Other/Zmb73_aliases.txt', id_col=2, alias_col=0, headers=True)

# Add functional annotations
Zm5bFGS.add_annotations('Other/ZmFuncNoOrtho.tsv', sep="\t", gene_col=0)

# Build ZmGo
co.GOnt.from_obo(
    'Other/go.obo.bz2',
    'Other/zm_go.tsv.bz2',
    'ZmGO',
    'Maize Gene Ontology',
    Zm5bFGS
)

# Build ZmRoot
co.COB.from_table(
    'COB/ZmRoot/ROOTFPKM.tsv.gz',
    'ZmRoot',
    'Diverse Maize Root Genotype',
    Zm5bFGS,
    rawtype='RNASEQ',
    max_gene_missing_data=0.3,
    max_accession_missing_data=0.08,
    min_single_sample_expr=1,
    min_expr=0.001,
    quantile=False,
    max_val=300
)

# Build ZmPAN
co.COB.from_table(
    'COB/ZmPAN/PANGenomeFPKM.txt.gz',
    'ZmPAN',
    'Maize PAN Genome (Hirsch et al.)',
    Zm5bFGS,
    sep=',',
    rawtype='RNASEQ',
    max_gene_missing_data=0.3,
    max_accession_missing_data=0.08,
    min_single_sample_expr=1,
    min_expr=0.001,
    quantile=True,
    max_val=300
)

# Build ZmSAM
co.COB.from_table(
    'COB/ZmSAM/TranscriptomeProfiling_B73_Atlas_SAM_FGS_LiLin_20140316.txt.gz',
    'ZmSAM',
    'Maize B73 Tissue/Devel Atlas',
    Zm5bFGS,
    rawtype='RNASEQ',
    max_gene_missing_data=0.3,
    max_accession_missing_data=0.08,
    min_single_sample_expr=1,
    min_expr=0.001,
    quantile=True,
    max_val=250
)

# Build ZmWallace and add FDR results
df = pd.DataFrame.from_csv(
    'GWAS/ZmWallace/Wallace_etal_2014_PLoSGenet_GWAS_hits-150112.txt.bz2',
    index_col=None,
    sep='\t')

co.GWAS.from_DataFrame(
    df,
    'ZmWallace',
    'Wallace PLoS ONE Dataset.',
    Zm5bFGS,
    term_col='trait',
    chr_col='chr',
    pos_col='pos',
    strongest_attr='rmip',
    strongest_higher=False
)

co.Overlap.from_csv(dir='GWAS/ZmWallace/FDR', name='ZmWallace')

# Build ZmIonome and add FDR results 
df = pd.DataFrame.from_csv(
    'GWAS/ZmIonome/sigGWASsnpsCombinedIterations.longhorn.allLoc.csv.gz',
    index_col=None)

co.GWAS.from_DataFrame(
    df,
    'ZmIonome',
    'Maize Ionome',
    Zm5bFGS,
    term_col='el',
    chr_col='chr',
    pos_col='pos',
    strongest_attr='numIterations',
    strongest_higher=False
)

co.Overlap.from_csv(dir='GWAS/ZmIonome/FDR', name='ZmIonome')

