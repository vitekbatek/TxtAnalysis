from Lib.CheckFile import check
from Lib.ReadFile import read
from Lib.GetFilenames import getnames

#Read get filenames
print("#Get")
ListFilenames = getnames("E:\\testfiles")

for filename in ListFilenames:
    # Read Lines to List
    #print("#Read")
    print(filename)
    ListLines = read(str(filename))
    #print(ListLines)

    # Check List
    #print("#Check")
    Columns = [1, 2]
    ListErr = check(ListLines, Columns)
    if len(ListErr) != 0:
        print("   " + str(ListErr))

