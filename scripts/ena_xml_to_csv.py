#!/usr/bin/env python3

###############################################################################
# script name: ena_xml_to_csv.py
# developed by: Savvas Paragkamian
# framework: ISD Crete
###############################################################################
# GOAL:
# Aim of this script is to transform the xml available attributes from 
# ENA assigned to each sample of ISD Crete 2016 to csv.
###############################################################################
# usage:./ena_xml_to_csv.py
###############################################################################
import xml.etree.ElementTree as ET
import csv
import os,sys
import pandas as pd

# Directory containing the XML files
xml_dir = 'ena_samples_attr/'

# Output TSV file
output_file = 'ena_metadata/ena_isd_2016_attributes.tsv'

# List to store the extracted data
data = []

# Iterate over each XML file in the directory
for filename in os.listdir(xml_dir):
    if filename.endswith('.xml'):
        # Parse the XML file
        
        tree = ET.parse(os.path.join(xml_dir, filename))
        root = tree.getroot()
        #pd_df = pd.read_xml(os.path.join(xml_dir, filename))
        #print(pd_df)

        print(filename)
        print(root)
        print(root.tag)
        for child in root.iter():
            #print(child.tag)
            #print(child.attrib)
            print(child.text)


        print("end of loop")
        
        xml_elem = []
        for sample in root.findall("./SAMPLE/"):
            xml_elem.append(sample.tag)
            print(sample.text)
        
        
        title = []
        for titl in root.findall("./SAMPLE/TITLE"):
            title.append(titl.tag)
            title.append(titl.text)
        
        
        links = []
        for link in root.findall("./SAMPLE/SAMPLE_LINKS/SAMPLE_LINK/XREF_LINK/"):
            links.append(link.tag)
            links.append(link.text)
        
        attribs = []
        for attrib in root.findall("./SAMPLE/SAMPLE_ATTRIBUTES/SAMPLE_ATTRIBUTE/"):
            attribs.append(attrib.tag)
            attribs.append(attrib.text)
        
        print(xml_elem, title, links, attribs)
        #print(sample_attribute.attrib)
        # Loop all sentence in the xml
            #for opinion in sample_attribute.iter('Opinion'):
            # Loop all Opinion of a particular sentence.
                #print([opinion.attrib['polarity'], sentence.find('text').text, opinion.attrib['category']])
        # Extract data from XML and store in a dictionary
        #    xml_data = {}
        #    xml_data['Filename'] = filename  # Example: storing the filename
        #    xml_data['Value1'] = root.find('PRIMARY_ID').text  # Example: extracting value from XML element
        #    xml_data['Value2'] = root.find('ID').text  # Example: extracting another value
        
        # Append the dictionary to the data list
        sys.exit()
        data.append(xml_data)

# Get the list of keys from the first dictionary in the data list
fieldnames = data[0].keys()

# Write the data to TSV file
with open(output_file, 'w', newline='') as tsvfile:
    writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
    
    # Write the header
    writer.writeheader()
    
    # Write the data rows
    writer.writerows(data)

print(f"Conversion complete. The TSV file '{output_file}' has been created.")


