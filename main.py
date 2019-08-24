#!/usr/bin/python3
import re
import csv
import sys
arguments = sys.argv
del arguments[0]
inKanji = "known-kanji.csv"
inWord = "wordlist.csv"
outFile = "output.csv"
exportType = "all"
for a in arguments:
    if a[:2] == "k:":
        inKanji = a[2:]
    if a[:2] == "w:":
        inWord = a[2:]
    if a[:2] == "o:":
        outFile = a[2:]
    if a[:2] == "t:":
        exportType = a[2:]
allowedCharacers = []
vocabList = [["Word", "kana"]]
kana = []
allowedRegEx = ""
kanaRegEx = ""
endlist = [["Kanji", "Type"]]
typeWord = ""
with open(inKanji, 'r') as csv_file:
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
with open(inWord, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        vocabList.append(line)

for list in allowedCharacers:
    allowedRegEx = allowedRegEx + list
for list in kana:
    kanaRegEx = kanaRegEx + list
for list in vocabList:
    kanaOnly = bool(re.match("^[" + kanaRegEx + "]+$", list[0]))
    kanjiKnown = bool(re.match("^[" + allowedRegEx + "]+$", list[0]))
    if kanaOnly == True:
        typeWord = "kana only word"
    else:
        if kanjiKnown == True:
            typeWord = "word with all kanji known"
        elif list[0] == "Word":
            typeWord = "type"
        else:
            typeWord = "word with unknown kanji"

    endlist.append([list[0], list[1], typeWord])

del endlist[0]
with open(outFile, 'w') as newfile:
    linewrite = csv.writer(newfile, delimiter=',')
    if exportType == "all":
        for line in endlist:
            linewrite.writerow(line)
    elif exportType == "alk":
        for line in endlist:
            if line[2] == "word with all kanji known" or line[0] == "Word":
                linewrite.writerow(line)
    elif exportType == "ku":
        for line in endlist:
            if line[2] == "word with unknown kanji" or line[0] == "Word":
                linewrite.writerow(line)
    elif exportType == "ko":
        for line in endlist:
            if line[2] == "kana only word" or line[0] == "Word":
                linewrite.writerow(line)
    else:
        print("Unknown export type, type set to all")
        for line in endlist:
            linewrite.writerow(line)
