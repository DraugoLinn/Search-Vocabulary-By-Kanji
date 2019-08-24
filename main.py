#!/usr/bin/python3
import re
import csv
import sys
arguments = sys.argv
del arguments[0]
inKanji = "known-kanji.csv"
inWord = "wordlist.csv"
outFile = "output.csv"
for a in arguments:
    if a[:2] == "k:":
        inKanji = a[2:]
    if a[:2] == "w:":
        inWord = a[2:]
    if a[:2] == "o:":
        outFile = a[2:]
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
        else:
            typeWord = "word with unknown kanji"
    #print(list, typeWord)
    endlist.append([list[0], list[1], typeWord])
# print(endlist)
del endlist[0]
with open(outFile, 'w') as newfile:
    linewrite = csv.writer(newfile, delimiter=',')
    for line in endlist:
        linewrite.writerow(line)
'''
with open('outputKnownOnly.csv', 'w') as newfile:
    linewrite = csv.writer(newfile, delimiter=',')
    for line in endlist:
        if line[1] == "word with all kanji known" or line[1] == "Type":
#            print(line)
            linewrite.writerow(line)
'''
#print(endlist)
