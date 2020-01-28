import re
from data_names import files
from data_names import files_MQ


'''
Function takes a list of json files to reformat.  Incomming default json
files do not parse corretly with json().  This fixes the files

'''
def fix_json(files):

    #each files is read in then parsed to fix text
    for jfile in files:
        fin = open(jfile, 'r')
        text = fin.read()
        fin.close()

        text = re.sub(r'"\s+','"', text)    #removes whitespaces from returned lines after quote
        text = re.sub(r'[a-zA-Z)](\s\s+)', "", text) #removes whitespaces
        text = re.sub(r"#[a-zA-Z0-9\w '.,\/\/\s()]+", "", text) #removes comments
        text = re.sub(r'[(](\s+)', "", text)
        fout = open(jfile, "w")
        fout.write(text)
        fout.close()

#runs on both standard files and MQ files
fix_json(files)
fix_json(files_MQ)

