from __future__ import division
import string

""" relativeWordFrequencies.py
by Eric J.Parfitt (ejparfitt@gmail.com)

Given a list of words, and a list of expected frequencies for those
words, this program sorts the words by how many times more or less the
word is found than would be "expected."

Version: 1.0 alpha
"""

class Word:
    totalWords = 0
    def __init__(self, name):
        self.name = name
        self.expected = 0
        self.count = 1
    def getObserved(self):
        return self.count / Word.totalWords
    def getRelativeFreq(self):
        return self.getObserved() / self.expected

def tally(myInput, expected):
    words = []
    for myString in myInput:
        isInWords = False
        for word in words:
            if myString == word.name:
                word.count += 1
                isInWords = True
                break
        if not isInWords:
            toAdd = Word(myString)
            words.append(toAdd)
            if myString in expected:
                toAdd.expected = expected[myString]
        Word.totalWords +=1
    return words

def removePunctuation(myString):
    return myString.translate(string.maketrans("",""), string.punctuation)

myInput = ["this", "is", "is", "a", "test"]
expected = {"this": .7, "is": .1, "test": .9}

words = tally(myInput, expected)
unexpectedWords = []
expectedWords = []
for word in words:
    if word.expected == 0:
        unexpectedWords.append(word)
    else:
        expectedWords.append(word)
unexpectedWords = sorted(unexpectedWords,
        key = lambda word: word.getObserved(), reverse = True)
expectedWords = sorted(expectedWords, key = lambda word:
        word.getRelativeFreq(), reverse = True)
print("Unexpected words:")
for word in unexpectedWords:
    print(word.name, word.getObserved())
print("Expected words:")
for word in expectedWords:
    print(word.name, word.getRelativeFreq())
