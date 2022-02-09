from english_words import english_words_lower_alpha_set
wordlist = []

for word in english_words_lower_alpha_set:
    if(len(word) == 5):
        wordlist.append(word)
        print(word)