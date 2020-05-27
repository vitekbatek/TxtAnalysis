import datetime
import os
from Lib.CheckFile import check
from Lib.ReadFile import read
from Lib.GetFilenames import getnames

#Get data
now = datetime.datetime.now()



#Write logfile
with open(str(os.getcwd())+"/checklogs.txt", "w") as filelogs:
    filelogs.write(
        'Проверка текстовых файлов НПРЧ на дублирование значений по столбцам\nДата выполнения: ' + now.strftime(
            "%d-%m-%Y %H:%M") + '\n')

    # Input path
    try:
        path = str(input('Введите Директорию для проверки: '))
    except ValueError:
        filelogs.write('Директория для проверки введена неверно. Проверка будет выполнена в текущей директории\n')
        print('Директория для проверки введена неверно. Проверка будет выполнена в текущей директории')
        path = os.getcwd()
    if path == '':
        filelogs.write('Директория для проверки не введена. Проверка будет выполнена в текущей директории\n')
        print('Директория для проверки не введена. Проверка будет выполнена в текущей директории')
        path = os.getcwd()
    if not os.path.exists(path):
        filelogs.write('Директория не найдена. Проверка будет выполнена в текущей директории\n')
        print('Директория не найдена. Проверка будет выполнена в текущей директории')
        path = os.getcwd()

    filelogs.write('Директория: ' + str(path) + '\n')

    try:
        columns = list(map(int, input('Введите через пробел номера столбцов по которым необходимо сделать проверку:  ').split(" ")))
    except ValueError:
        filelogs.write('Осуществлен некорректный ввод столбцов. Проверка не выполнена\n')
        print('Осуществлен некорректный ввод столбцов. Проверка не выполнена')
        exit(0)


    filenames = getnames(path)

    if columns == []:
        filelogs.write('   Столбцы для проверки не введены\n')
        print('Столбцы для проверки не введены')
        exit(0)
    else:
        filelogs.write('Столбцы для проверки:' + str(columns) + '\n')
        print('Столбцы для проверки:' + str(columns))
    print('Проверка:', end=' ')

    i = 6
    for filename in filenames:
        print('.', end=' ')
        if i%29 == 0:
            i = 0
            print('')
        i+=1
        # Read Lines to List
        listlines = read(str(filename))
        filelogs.write(filename + '\n')

        # Check List
        listerr = check(listlines, columns)
        for err in reversed(listerr):
            filelogs.write(err + '\n')