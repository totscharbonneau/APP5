import os

def extractData():
    resourcesPath = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'resources')
    authorDict = {}
    for author in os.listdir(resourcesPath):
        currentAuthorPath = os.path.join(resourcesPath, author)
        authorDict[author] = {}
        for text in os.listdir(currentAuthorPath):
            if ".txt" in text:
                authorDict[author][(os.path.join(currentAuthorPath, text))] = {}
    for author in authorDict:
        currentAuthor = authorDict[author]
        for textPath in currentAuthor:
            print(textPath)
            currentText = open(textPath, 'r', encoding='utf-8').read()
            currentText = customSeparators(currentText)
            authorDict[author][textPath] = customSplit(currentText)
    return authorDict

def customSeparators(inputText):
    separators = ',', '.', '«', '»', "'", '!', '?', '  ', '\n', '-', ';', ':', '(', ')', '[', ']'
    for sep in separators:
        inputText = inputText.replace(sep, ' ')
        inputText = inputText.lower()
    return inputText


# texte = customSeparators(texte)


def customSplit(inputText):
    wordlist = inputText.split()
    wordDict = {}
    for word in wordlist:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1

    for word in list(wordDict):
        if len(word) <= 2:
            wordDict.pop(word)
    return wordDict


# wordDict = customSplit(texte)

# file.close()