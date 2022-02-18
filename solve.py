from operator import pos
from turtle import color
from game import *

def setAnswerList():
    with open('wordle-answers-alphabetical.txt') as file:
        answerlist = file.readlines()

    for i in range(len(answerlist)):
        answerlist[i] = answerlist[i][:5]
        answerlist[i] = answerlist[i].upper()

    return answerlist

#this function takes results from game input and returns
#all the possible words that could remain
def possibleWords(letterlist, words, colors, row):

    #INPUTS: these will be used to narrow down letter list
    #to a list of remaining words that qualify:
    
    #it is easiest to remove the words that don't work, rather than
    #selecting the ones that do

    #A word is removed from the list if one of the following is true:

    #1. If a word contains gray letters
    #2. If a word contains a yellow letter in the same spot it was entered
    
    remainingWords = setAnswerList()
        
    #identify yellow letters and their locations
    #1 means yellow present, 0 means absent
    yellowLetters = []

    #find yellow letters
    for i in range(6):
        for j in range(5):
            if colors[i][j] == 'y':
                #want to remove any words that have that letter in that index
                letter = [words[i][j], j]
                yellowLetters.append(letter)

    #print(yellowLetters)

    #remove yellow letters in wrong spot
    c = False
    size = len(remainingWords)
    for j in range(size):

        word = remainingWords[j]

        for letter in yellowLetters:
            if(c == False):
                for i in range(5):
                    if(c == False):
                        if word[i:i+1] == letter[0] and i == letter[1] and word.count(letter[0]) == 1 and word != '*':
                            remainingWords[j] = '*'
                            #print("Removed2: ", word, " because: ", letter)
                            c = True
                            
                    else:
                        break
            else:
                break

        c = False
    
    #all remaining words need to have that yellow letter though...
    for j in range(len(remainingWords)):
        word = remainingWords[j]
        for letter in yellowLetters:
            if word.count(letter[0]) == 0 and word != '*':
                #print("Removed4: ", word, " becayse: ", letter)
                remainingWords[j] = '*'
             
                

    #remove words where green letter is not present in correct place
    greenLetters = []
    for i in range(6):
        for j in range(5):
            if colors[i][j] == 'g':
                
                letter = [words[i][j], j]
                greenLetters.append(letter)

    #remove the words
    for j in range(len(remainingWords)):
        word = remainingWords[j]
        for letter in greenLetters:
            for i in range(5):
                if word[i:i+1] != letter[0] and i == letter[1] and word != '*':
                    remainingWords[j] = '*'
                    #print("Removed3: ", word, " because: ", letter)
                    
                    

    #1 identify gray letters and remove words that have them
    grayLetters = []
    for i in range(26):
        if letterlist[i] == 'w':
            grayLetters.append(chr(i+65))
    #print(grayLetters)

    #remove the gray letters
    c = False
    size = len(remainingWords)
    for j in range(size):

        word = remainingWords[j]

        for letter in grayLetters:
            if c == False:
                for i in range(5):
                    if c == False:
                        #if not multiple of same letter in words row where one of the letters is yellow or green
                        if word[i:i+1] == letter and word != '*':

                            #find all of the letter of question in the input
                            cancel = False
                            for a in range(5):
                                if(colors[row][a] == 'y' or colors[row][a] == 'g') and words[row][a] == letter:
                                    cancel = True

                            if cancel == False:
                                remainingWords[j] = '*'
                                #print("Removed: ", word, " because: ", letter)
                             
                                c = True
                    else:
                        break
            else:
                break
    
        c = False

    return remainingWords

#given a set of possible answer choices, this function will 
#determine the "best" (not really the best) word to play 
#for the next round. This will be done by assigning a score value 
#to words based on the frequency of the letters within the word
#and picking the word with the highest score
def chooseWord(letterlist, words, colors, row, wipe):

    remainingWords = possibleWords(letterlist, words, colors, row)

    if wipe:
        remainingWords = setAnswerList()

    #as determined from countLetters.py, the most common letters are as follows:
    #['e', 'a', 'r', 'o', 't', 'l', 'i', 's', 'n', 'c', 'u', 'y', 
    # 'd', 'h', 'p', 'm', 'g', 'b', 'f', 'k', 'w', 'v', 'z', 'x', 
    # 'q', 'j']
    # This means that 'e' will correspond to 26 in this model, while j
    # will correspond to 1

    scoreArr = [25, 9, 17, 14, 26, 8, 10, 13, 20, 1, 7, 21, 11, 18, 23, 12, 2, 24, 19, 22, 16, 5, 6, 3, 15, 4]

    bestScore = 0
    bestIndex = 0

    for j in range(len(remainingWords)):
        word = remainingWords[j]
        if(word != '*'):
            word = word.lower()
            score = 0
            for i in range(5):
                letter = word[i:i+1]
                index = ord(letter) - 97

                #getting the same letter again isn't as helpful
                #so I'm going to only give half points for that
                if word.count(letter) == 1:
                    score += scoreArr[index]
                else:
                    score += int((scoreArr[index])/2)
            
            if(score > bestScore):
                bestScore = score
                bestIndex = j
    #print("Words left: ", count)

    #if(count <= 50):
        #printarr(remainingWords)
    
    return remainingWords[bestIndex]
    

def printarr(arr):
    for i in range(len(arr)):
        if arr[i] != '*':
            print(arr[i])
