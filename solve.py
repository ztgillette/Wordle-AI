from game import *

def possibleWords(letterlist, words):

    #using qualifications from letter list,
    #determine all the possible words to choose from
    
    remainingWords = []

    for word in words:
        
        #first, add all the words with correct letter placememt
        #(i.e. green letters in correct spots)
        for i in letterlist:
            #f letterlist[i] == 'g':
            #just realized that we didn't include placement info...

        #last, get add remaining words 
        #(words that don't have any 'w' letters)
        for i in letterlist:
            if chr(i + 65) in word == False or letterlist[i] != 'w':
                remainingWords.append(word)
    
    return remainingWords