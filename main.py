#!/usr/bin/python3
import re
import csv
allowedCharacers = []
vocabList = []
kana = []
allowedRegEx = ""
kanaRegEx = ""
endlist = [["Kanji", "Type"]]
typeWord = ""
with open('known-kanji.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        allowedCharacers.append(line[0])
with open('kana.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        kana.append(line[0])
with open('kana.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        allowedCharacers.append(line[0])
with open('wordlist.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        vocabList.append(line[0])

for list in allowedCharacers:
    allowedRegEx = allowedRegEx + list
for list in kana:
    kanaRegEx = kanaRegEx + list
for list in vocabList:
    kanaOnly = bool(re.match("^[" + kanaRegEx + "]+$", list))
    kanjiKnown = bool(re.match("^[" + allowedRegEx + "]+$", list))


    if kanaOnly == True:
        typeWord = "kana only word"
    else:
        if kanjiKnown == True:
            typeWord = "word with all kanji known"
        else:
            typeWord = "word with unknown kanji"
    #print(list, typeWord)
    endlist.append([list, typeWord])
# print(endlist)
with open('output.csv', 'w') as newfile:
    linewrite = csv.writer(newfile, delimiter=',')
    for line in endlist:
        linewrite.writerow(line)
#print(endlist[1][1])
with open('outputKnownOnly.csv', 'w') as newfile:
    linewrite = csv.writer(newfile, delimiter=',')
    for line in endlist:
        if line[1] == "word with all kanji known" or line[1] == "Type":
            print(line)
            linewrite.writerow(line)
