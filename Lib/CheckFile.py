def check(listlines, columns):
    listerr = []
    i = 0
    errfile = False

    if len(listlines) != 3600:
        listerr.append("   Формат файла задан неверно: кол-во строк не соответствует 3600 и равно " + str(len(listlines)))
        errfile = True
    else:
        for i in range(3600):
            try:
                for column in columns:
                    temp = str(listlines[i][int(column) - 1])
            except IndexError:
                listerr.append("   Формат файла задан неверно: невозможно преобразовать данные в строке №" + str(i+1))
                errfile = True
    i=0
    if not errfile:
        for i in range(len(listlines)):
            if i == len(listlines)-1:
                for column in columns:
                    if str(listlines[i][int(column) - 1]) == "":
                        listerr.append("   Строка: " + str(i+1) + " Столбец: " + str(int(column)) + " - нет данных")
            else:
                for column in columns:
                    if str(listlines[i][int(column)-1]) != "" and (str(listlines[i][int(column)-1]) == str(listlines[i + 1][int(column)-1])):
                        listerr.append("   Строка: " + str(i+1) + " и " + str(i+2) + " Столбец: " + str(int(column)) + " - значения равны")
                    if str(listlines[i][int(column)-1]) == "":
                        listerr.append("   Строка: " + str(i+1) + " Столбец: " + str(int(column)) + " - нет данных")
        if len(listerr) == 0:
            listerr.append("   Ошибок в строках нет")
        else:
            listerr.append("   Кол-во ошибок в строках: " + str(len(listerr)))
    return listerr
