# ISD - Island Sampling Day Crete 2016

This repository contains the scripts for the analysis of the ISD Crete 2016.
ISD Crete 2016 is a soil microbiome sampling from 72 distinct sites around 
Crete island, Greece. 

During the 18th Genome Standards Consortium workshop the participants along
with members from Hellenic Centre for Marine Research organised the Island 
Sampling Day Crete 2016.

The goal of this sampling was to put metagenomic standards into play.

For more info regarding the methodology of the sampling 
visit the [website](https://lab42open-team.github.io/isd-crete-website/).

## Structure of the repository



## Data

The sequences of the ISD Crete 2016 are available in ENA project [PRJEB21776](https://www.ebi.ac.uk/ena/browser/view/PRJEB21776)
and were downloaded using the ENA API. The script is available [here](scripts/get_isd_crete_2016_fastq.sh) for the
raw data and [here](scripts/get_isd_crete_2016_attributes.py) for the metadata.
The metadata are in `xml` format and using this [script](https://github.com/savvas-paragkamian/isd-crete/blob/main/scripts/ena_xml_to_csv.py) we transform them to
tabular format.

## Reads summary

In this [script](scripts/isd_crete_raw_data_summary.sh) there are some oneliners
to provide some basic information regarding the reads.

Total reads

Primers

Numbers of Ns in reads




## Taxonomic assignement
We used PEMA and DADA2 for the clustering of OTUs and ASVs, respectively.

## Sampling metadata

## Remote sensing data


