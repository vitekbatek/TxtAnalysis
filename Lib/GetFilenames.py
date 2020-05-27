import fnmatch
from os import walk

def getnames(path):
    filenames = []
    for (dirpath, dirnames, files) in walk(path, topdown=True):
        for filename in fnmatch.filter(files, '*.txt'):
            filenames.append(str(dirpath) + '\\' + str(filename))

    return filenames