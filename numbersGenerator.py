import re
import csv
from bwDict import bwdict

with open('originalorgInputFile.txt', 'r',encoding='utf-8') as orgInputFile:
    orgInputFile.seek(0)
    with open('1mod.txt', 'w', encoding='utf-8') as firstModFile:
        firstModFile.seek(0)
        for line in orgInputFile:
            if re.match('^SPRZEDAJ', line):
                pass
            elif re.match('^\t', line):
                pass
            elif re.match('^\n', line):
                pass
            else:
                firstModFile.write(line)
    firstModFile.close()
orgInputFile.close()

with open('1mod.txt', 'r', encoding='utf-8') as firstModFile:
    firstModFile.seek(0)
    with open('2mod.txt', 'w', encoding='utf-8') as secondModFile:
        for line in firstModFile:
            editedLine = line
            editedLine = editedLine.replace('Dobry ', "")
            editedLine = editedLine.replace('Dobra ', "")
            editedLine = editedLine.replace('Doskonała ', "")
            editedLine = editedLine.replace('Doskonały ', "") 
            editedLine = editedLine.replace(' (+1)', "")
            editedLine = editedLine.replace(' (+2)', "")
            editedLine = editedLine.replace(' (+3)', "")
            editedLine = editedLine.replace(' (+4)', "")
            editedLine = editedLine.replace(' (+5)', "")
            secondModFile.write(editedLine)
    secondModFile.close() 
firstModFile.close()

with open('2mod.txt', 'r', encoding='utf-8') as secondModFile:
    for line in secondModFile.readlines():
        first_word = line.split(" ")[0]
        last_word = line.split(" ")[-1].replace("\n","")

        print("{},{},{},{}".format(line.replace("\n",""),
            bwdict.get(first_word,0),
            bwdict.get(last_word,0),
            int(bwdict.get(first_word,0))+int(bwdict.get(last_word,0))))