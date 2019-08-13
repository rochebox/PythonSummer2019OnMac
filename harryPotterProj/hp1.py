## Harry Potter experiement

fileName = "harry_potter_s_stone.txt"
print(f" Trying to open {fileName}")

f=open(fileName, "r")
contents = ""
if f.mode == "r":
    contents = f.read()
f.close()

hCount = 0
theCount = 0
aCount = 0
doughnutCount = 0

wordList = contents.split()

for i in range(len(wordList)):
    wordList[i] = wordList[i].strip()

    if wordList[i].startswith('"'):
        w = wordList[i]
        wordList[i] = w[1:len(wordList[i])]

    if wordList[i].endswith('"'):
        w = wordList[i]
        wordList[i] = w[ :len(wordList[i])-1]

    if wordList[i].endswith(',') or wordList[i].endswith('.'):
        w = wordList[i]
        wordList[i] = w[ :len(wordList[i])-1]

    elif wordList[i].endswith("'s") :
        w = wordList[i]
        wordList[i] = w[ :len(wordList[i])-2]

    if wordList[i].lower() == 'harry':
        hCount += 1
    elif wordList[i].lower() == 'the':
        theCount += 1
    elif wordList[i].lower() == 'doughnut':
        doughnutCount += 1
    elif wordList[i].lower() == 'a':
        aCount += 1

totalWords = len(wordList)
print(f"Total words in book {totalWords}")        
print (f"Number of Times 'Harry' is mentioned: {hCount}")
print (f"Number of Times 'The' or 'the' is used: {theCount}")
print (f"Number of Times 'A' or 'a' is used: {aCount}")
print (f"Number of Times 'Doughnut' is used: {doughnutCount}")
    
    
##for w in wordList:
##    print(w)







