import re

arrWithAllItems = []

with open('test.txt', 'r', encoding='utf-8') as thefile:
    numOfLines = len(thefile.readlines())
    thefile.seek(0)
    for line in range(0, numOfLines):
        arrWithAllItems.append(thefile.readline())

myRegex = re.compile('[0-9]+')
tempArr1 = []

for item in arrWithAllItems:
    if ("TYP" in item):
        print(item + "Dobre łączenia:\n")
    regExInLine = myRegex.findall(item)
    tempArr1 = regExInLine
    if (len(tempArr1) > 2):
        tempArr1 = [*map(int, tempArr1)]
        itemA = tempArr1[0] + tempArr1[2]
        itemB = tempArr1[3] + tempArr1[5]
        itemC = tempArr1[6] + tempArr1[8]
        if(itemA >= itemB):
            if(itemC - itemA == 1):
                print(item)
        elif(itemA < itemB):
            if(itemC - itemB == 1):
                print(item)
