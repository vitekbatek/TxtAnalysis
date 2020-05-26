import fnmatch
from os import walk

def getnames(directory):
    listfilenames = []
    for (dirpath, dirnames, filenames) in walk(directory, topdown=True):
        for filename in fnmatch.filter(filenames, '*.txt'):
            #print("Filename = " + str(dirpath) + "\\" + str(filename))
            listfilenames.append(str(dirpath) + "\\" + str(filename))
    return listfilenames