'''
Generate an edges file from the filenames in data_names.py
The file is saved as edges.txt
'''



import graph
from data_names import files
import json
from entrance import Door
import re

def a():
    print('yolo')

'''
Generates the original edges.txt file
'''
def make_edges():
    g = {}                                  #dictionary for edges
    #each json file is read in and is loaded into data
    for filename in files:
        with open(filename) as fin:
            data = json.load(fin)     

        #Parses through the json to grab wanted variables out
        # It associates the start "region" to the end "exit"  
        # Then assignes a length of "0" for the edge temporarily    
        for region in data:
            g[region['region_name']] = []
            if "exits" in region.keys():
                for exits in region['exits']:
                    tup  = [exits , 0]
                    g[region['region_name']].append(tup)
    
    #Edits the format of the text file
    with open("edges.txt", 'w') as fout:
        text = str(g)
        text = re.sub(r"\],( )'","],\n'", text)
        text = text.replace("{", "")
        text = text.replace("}", "")
        print(text)
        fout.write(text)

    #Continued format edit !!!Combine into the same function in future!!!
    optimize_edges("edges.txt")


'''
With the original file of edges from the json, performs a step to make
the lines in the file more readable and usable by future functions

This optimize_edges() function should be combined with generate_edges() and 
refactored.  Currently inefficient but it does the job
'''
def optimize_edges(filename):
        fin = open(filename, 'r')
        text = ""
        lines = fin.readlines()

        #steps through each line in the file editing the format
        for line in lines:
            node = re.findall(r"'([a-zA-Z ]+)", line)
            ends = re.findall(r"\['([a-zA-Z ]+)", line)
            ends_distance = re.findall(r'\d+', line)
            for x in range(0, len(ends)):
                text += str(node[0])+", "+str(ends[x])+", " +  str(ends_distance[x]+"\n")

        fin.close()
        fout = open(filename, 'w')
        fout.write(text)
        fout.close()


