'''
Functions for generating nodes.txt
'''

import graph
from data_names import files
import json
from entrance import Door
import re


'''
uses the files in data_names.py to generate nodes (Regions) with a size of the
number of locations in the region
'''
def make_nodes():
    g = {}                  #holds the data from .json files
    for filename in files:
            
            #each file dumps its json to data then in the dictionary g{}, the
            #region is associated with the amount of locations it has
            with open(filename) as fin:
                data = json.load(fin)
            for region in data:
                if 'locations' in region.keys():
                    #print(len(region['locations']))
                    g[region['region_name']] = len(region['locations'])
                else:
                    g[region['region_name']] = 0

    #edits the final output to the nodes.txt to be nice and usable

    text = str(g)
    text = re.sub(r', ','\n', text)
    text = re.sub(r"[{}']","", text)
    text = text.replace(":", ",")

    with open("nodes.txt", 'w') as fout:
        fout.write(text)
