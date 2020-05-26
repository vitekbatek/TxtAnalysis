def read(input_file_txt):
    file = open(input_file_txt, "r")
    listlines = []
    i = 0
    for line in file.readlines():
        listlines.append("")
        listlines[i] = line.replace(":", ";").split(";")
        i = i+1
    return listlines
