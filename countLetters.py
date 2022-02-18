answerlist = []
with open('wordle-answers-alphabetical.txt') as file:
    answerlist = file.readlines()

#array of ints used to count the frequency of corresponding letters
freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#storing frequencies
for i in range(len(answerlist)):
    word = answerlist[i]
    word = word.lower()

    for j in range(5):

        letter = word[j:j+1]
        index = ord(letter)-97
        freq[index] += 1

#returning the letters in order
orderedList = []
max = freq[0]
maxIndex = 0
for j in range (26):
    for i in range(26):
        if(freq[i] > max):
            max = freq[i]
            maxIndex = i
    orderedList.append(chr(maxIndex+97))
    freq[maxIndex] = -1
    max = freq[0]
    maxIndex = 0

print(orderedList)




    

