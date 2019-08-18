#!/usr/bin/python3
import re
import csv
allowedCharacers = []
vocabList = []
kana = []
allowedRegEx = ""
kanaRegEx = ""
endlist = [[]]
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
    endlist.append([list, ])


    if kanaOnly == True:
        typeWord = "kana only word"
    else:
        if kanjiKnown == True:
            typeWord = "word with all kanji known"
        else:
            typeWord = "word with unknown kanji"
    print(list, typeWord)
    endlist.append([list, typeWord])
# print(endlist)
