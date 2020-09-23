"""
Author: Long Le
Date: 9/23/2020

Find rhyme words in Vietnamese for writing song lyrics.
"""

#declaration
consonants = ['b', 'ch', 'c', 'd', 'đ', 'gi', 'gh', 'g', 'h', 'k', 
'kh', 'l', 'm', 'n', 'ngh', 'ng', 'nh', 'ph', 'p', 'qu', 'r', 's', 
'th', 'tr', 't', 'v', 'x']
vieDict = {}

#opening text file
f = open("wordlist.txt", encoding = "utf-8")
allWords = f.readlines()

def findEnding(word):
    rhyme = ''
    firstThree = word[:3]
    firstTwo = word[:2]
    firstOne = word[:1]
    if firstThree in consonants:
        rhyme = word[3:]
        return rhyme
    elif firstTwo in consonants:
        rhyme = word[2:]
        return rhyme
    elif firstOne in consonants:
        rhyme = word[1:]
        return rhyme
    else:
        return word

#process the word and add to the dictionary
for i in range(len(allWords)):
    word = allWords[i].strip('\n')
    allWords[i] = word
    lastWord = word.split(' ')[-1]
    rhyme = findEnding(lastWord)
    #add to dictionary
    if rhyme in vieDict.keys():
        list = vieDict[rhyme]
        list.append(word)
    else:
        vieDict[rhyme] = [word]
f.close()

while True:
    find = input("Tìm vần với: ")
    inputEnding = findEnding(find.split(" ")[-1])
    if inputEnding in vieDict.keys():
        print("Kết quả: ")
        print(vieDict[inputEnding])
    else:
        print("Không tìm thấy kết quả") 
    print("Nhấn Ctlr + D để kết thúc, hoặc tiếp tục nhập...\n")
    