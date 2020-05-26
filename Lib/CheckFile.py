
def check(arr, Columns):
    ListErr = []
    i = 0
    err = False
    while i < (3600 - 1):
        for column in Columns:
            if str(arr[i][int(column)-1]) != "" and str(arr[i + 1][int(column)-1]) != "":
                err_line = ((float(arr[i][int(column)-1]) - float(arr[i + 1][int(column)-1])) == 0)
            if err_line:
                ListErr.append("Столбец: " + str(int(column)) + " Строка: " + str(i) + "<->" + str(i + 1))
        i = i + 1
    if len(ListErr) == 0:
        print("   Ошибок нет")
    else:
        print("   Кол-во ошибок: " + str(len(ListErr)))
    return ListErr
