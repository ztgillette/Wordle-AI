### TODO
# 1. github
# 3. find and implement word dictionary - US Scrabble dictionary
# 4. once game is ready to go, figure out the AI part

### Import statements ###
from curses import termattrs
import pygame
from english_words import english_words_lower_alpha_set
import random
pygame.font.init()

#################################
### Display-related Functions ###
#################################

### Creating the game window ###
HEIGHT = 800
WIDTH = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle AI")
BACKGROUND_COLOR = (18,18,19)
BOX_COLOR = (60, 60, 60)
FPS = 30
TITLE_FONT = pygame.font.Font('freesansbold.ttf', 38)

### Drawing window ###
def draw_window(input, row, arr, colors):
    WINDOW.fill(BACKGROUND_COLOR)
    draw_screen(colors, row)
    
    drawWords(arr) 
    drawInput(input, row)
    pygame.display.update()

### Drawing screen ###
def draw_screen(colors, row):
    draw_title()
    draw_line()
    draw_box_grid(colors, row)

### Drawing title ###
def draw_title():
    title = TITLE_FONT.render("WORDLE AI", True, (255, 255, 255))
    WINDOW.blit(title, (135, 30))

def draw_line():
    pygame.draw.rect(WINDOW, BOX_COLOR, pygame.Rect(86, 75, 324, 1))

### Draw box grid ###
def draw_box_grid(colors, row):
    x = 0
    y = 0
    for i in range(6):
        for j in range(5):

            #draw colored boxes
            #print green
            if colors[i][j] == 'g':
                draw_box(86 + x, 170 + y, (82, 140, 77))
            #print yellow
            elif colors[i][j] == 'y':
                draw_box(86 + x, 170 + y, (181, 158, 59))
            #print gray
            elif colors[i][j] == 'w':
                draw_box(86 + x, 170 + y, (58, 58, 59))
            else:
                draw_box(86 + x, 170 + y, (BACKGROUND_COLOR))
            x += 66
        x = 0
        y += 66

### Draw box ###
def draw_box(x, y, color):
    if(color != (18,18,19)):
        pygame.draw.rect(WINDOW, color, pygame.Rect(x, y, 60, 60))
    else:
        pygame.draw.rect(WINDOW, BOX_COLOR, pygame.Rect(x, y, 60, 60))

    pygame.draw.rect(WINDOW, color, pygame.Rect(x+2, y+2, 56, 56))

### present input on screen ###
def drawInput(input, row):

    yadded = (row) * 66

    length = len(input)
    fakeLength = length
    if length < 5:
        while(fakeLength < 5):
            input += ' '
            fakeLength += 1
    
    c1 = input[:1]
    c2 = input[1:2]
    c3 = input[2:3]
    c4 = input[3:4]
    c5 = input[4:]

    c1display = TITLE_FONT.render(c1, True, (255, 255, 255))
    WINDOW.blit(c1display, (104, 183 + yadded))

    c2display = TITLE_FONT.render(c2, True, (255, 255, 255))
    WINDOW.blit(c2display, (170, 183 + yadded))

    c3display = TITLE_FONT.render(c3, True, (255, 255, 255))
    WINDOW.blit(c3display, (236, 183 + yadded))

    c4display = TITLE_FONT.render(c4, True, (255, 255, 255))
    WINDOW.blit(c4display, (302, 183 + yadded))

    c5display = TITLE_FONT.render(c5, True, (255, 255, 255))
    WINDOW.blit(c5display, (368, 183 + yadded))

### Draw words that have already been entered on to the screen ###
def drawWords(arr):
    
    for i in range(6):
        for j in range(5):

            x = 104 + ((j) * 66)
            y = 183 + ((i) * 66)

            if arr[i][j] == '*':
                letter = TITLE_FONT.render(' ', True, (255, 255, 255))
            else:
                letter = TITLE_FONT.render(arr[i][j], True, (255, 255, 255))
            WINDOW.blit(letter, (x, y))
    
    
##############################
### Game-related Functions ###
##############################

### Pick word that Wordle AI will try and find ###
def generateWordList():
    wordlist = []
    for word in english_words_lower_alpha_set:
        if(len(word) == 5):
            wordlist.append(word)

    return wordlist

def pickWord(wordlist):

    word = random.choice(wordlist)
    return word

### Check if input word is a valid word
def checkWord(input, wordlist):
    if(input in wordlist):
        return True
    return False
    

def showResults(input, answer, colors, row):
    
    answer = answer.upper()

    #First, get all the greens
    #print("CHECKING GREENS")
    for c in range(5):
        for a in range(5):
        
            if input[c:c+1] == answer[a:a+1]:
                
                if c==a:
                    #green
                    colors[row][a] = 'g'
                    answer = answer[:c] + '&' + answer[c+1:]
    #print("Input: ", input)
    #print("Answer: ", answer)
    #print(colors)

    #Next, get all the yellow
    #print("CHECKING YELLOWS")
    for c in range(5):
        for a in range(5):
        
            if input[c:c+1] == answer[a:a+1]:
                
                #yellow
                if(colors[row][c] != 'g'):
                    colors[row][c] = 'y'
                    answer = answer[:a] + '%' + answer[a+1:]
    #print("Input: ", input)
    #print("Answer: ", answer)
    #print(colors)
    
    #Make everything else gray
    #print("EVERYTHING ELSE GRAY")
    for i in range(5):
        if colors[row][i] != 'g' and colors[row][i] != 'y':
            colors[row][i] = 'w'
            answer = answer[:i] + '@' + answer[i+1:]

    #print("Input: ", input)
    #print("Answer: ", answer)
    #print(colors)
    
    #NOTE:
    #if a letter is in the right spot and there are no more of them, 
    #it should not be yellow in other spots
    
    return colors

def checkWin(row, colors):
    #check to see if won
    for i in range(5):
        if colors[row][i] != 'g':
            return False
    return True
            


######################
### Main game loop ###
######################
run = True
def loop():

    ### Set up the game
    wordlist = generateWordList()
    answer = pickWord(wordlist)

    ### Setting Clock ###
    clock = pygame.time.Clock()

    ### Variables ###
    input = ""
    row = 0
    words = [['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*']]
    colors = [['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b']]
    win = False
    
    while True:
        clock.tick(FPS)

        ### Quit program ###
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
            break
            
        ### Key input ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            

            ### Text input ###
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                elif event.key == pygame.K_RETURN:
                    if (len(input) == 5 or row == 5) and checkWord(input.lower(), wordlist):
                        ### "lock in" input as final answer ###
                        
                        if(row <= 5):
                            ### Store input ###
                            words[row][0] = input[:1]
                            words[row][1] = input[1:2]
                            words[row][2] = input[2:3]
                            words[row][3] = input[3:4]
                            words[row][4] = input[4:]

                            colors = showResults(input, answer, colors, row)

                            win = checkWin(row, colors)
                            if(win):
                                print(row)
                                row = 1000
                                print("Winner!")
                                print("The word was: ", answer)
                            
                            input = ""
                            row += 1

                            if(row == 6 and win == False):
                                print("You lose!")
                                print("The word was: ", answer)

                else:
                    if len(input) < 5 and row<6:
                        l = event.unicode
                        if l.isalpha():
                            input += l.upper()
        

        

        ### Draw display ###
        draw_window(input, row, words, colors)

def main():
    loop()
    pygame.quit()

if __name__ == "__main__":
    main()
