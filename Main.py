import datetime
import os
from Lib.CheckFile import check
from Lib.ReadFile import read
from Lib.GetFilenames import getnames

now = datetime.datetime.now()
#Input path
try:
    path = str(input('Введите Директорию для проверки: '))
except ValueError:
    print("Директория для проверки введена неверно\n")
    exit(0)
if path == "":
    print("Директория для проверки не введена\n")
    exit(0)
if not os.path.exists(path):
    print('Директория не найдена')
    exit(0)

#Write logfile
with open("../checklogs.txt", "w") as filelogs:

    filenames = getnames(path)
    filelogs.write("Проверка файлов. Дата выполнения " + now.strftime("%d-%m-%Y %H:%M") + ':\n')

    try:
        columns = list(map(int, input('Введите через пробел номера столбцов по которым необходимо сделать проверку:  ').split(" ")))
    except ValueError:
        filelogs.write("Осуществлен некорректный ввод столбцов\n")
        print("Осуществлен некорректный ввод столбцов\n")
        exit(0)



    if columns == []:
        filelogs.write("Столбцы для проерки не введены\n")
        print("Столбцы для проерки не введены\n")
        exit(0)

    for filename in filenames:
        # Read Lines to List
        print(filename)
        listlines = read(str(filename))
        filelogs.write(filename + '\n')

        # Check List
        #columns = [2, 3]
        listerr = check(listlines, columns)
        print("   " + str(listerr))
        for err in reversed(listerr):
            filelogs.write(err + '\n')