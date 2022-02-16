from game import *

answerlist = []
with open('wordle-answers-alphabetical.txt') as file:
    answerlist = file.readlines()

for i in range(len(answerlist)):
    answerlist[i] = answerlist[i][:5]
    answerlist[i] = answerlist[i].upper()

def possibleWords(letterlist, words):
    global answerlist

    #using qualifications from letter list,
    #determine all the possible words to choose from
    
    remainingWords = []

    for word in answerlist:
        
        #first, add all the words with correct letter placememt
        #(i.e. green letters in correct spots)
        for i in letterlist:
            if letterlist[i] == 'g':
                print()
            

        #last, get add remaining words 
        #(words that don't have any 'w' letters)
        for i in letterlist:
            if chr(i + 65) in word == False or letterlist[i] != 'w':
                remainingWords.append(word)
    
    return remainingWords