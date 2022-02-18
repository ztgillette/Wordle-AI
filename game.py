### TODO
# 4. once game is ready to go, figure out the AI part

### Import statements ###
from curses import termattrs
from dataclasses import asdict
import pygame
from english_words import english_words_lower_alpha_set
import random
from solve import *

pygame.font.init()

########################
### Global Variables ###
########################

letterlist = []
for i in range(26):
    letterlist.append('b')

words = []
wipe = False

#################################
### Display-related Functions ###
#################################

### Creating the game window ###
HEIGHT = 800
WIDTH = 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle AI")
FPS = 30

### color constants ###
BACKGROUND_COLOR = (18,18,19)
BOX_COLOR = (60, 60, 60)
GREEN = (82, 140, 77)
YELLOW = (181, 158, 59)
GRAY = (58, 58, 59)
WHITE = (255, 255, 255)

### font constants ###
TITLE_FONT = pygame.font.Font('freesansbold.ttf', 38)
SMALL_FONT = pygame.font.Font('freesansbold.ttf', 24)
SMALLEST_FONT = pygame.font.Font('freesansbold.ttf', 18)


### Drawing window ###
def draw_window(input1, row, arr, colors, lose, answer, win):
    WINDOW.fill(BACKGROUND_COLOR)
    draw_screen(colors, row)

    drawInstructions()
    
    drawWords(arr) 
    drawInput(input1, row)

    if(lose):
        drawAnswer(answer)
    if(win):
        drawNice()

    if(not lose and not win):
        drawLetterResults()

    pygame.display.update()

### Drawing screen ###
def draw_screen(colors, row):
    draw_title()
    draw_line()
    draw_box_grid(colors, row)

### Drawing title ###
def draw_title():
    title = TITLE_FONT.render("WORDLE AI", True, WHITE)
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
                draw_box(86 + x, 170 + y, GREEN)
            #print yellow
            elif colors[i][j] == 'y':
                draw_box(86 + x, 170 + y, YELLOW)
            #print gray
            elif colors[i][j] == 'w':
                draw_box(86 + x, 170 + y, GRAY)
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
def drawInput(input1, row):

    yadded = (row) * 66

    length = len(input1)
    fakeLength = length
    if length < 5:
        while(fakeLength < 5):
            input1 += ' '
            fakeLength += 1
    
    c1 = input1[:1]
    c2 = input1[1:2]
    c3 = input1[2:3]
    c4 = input1[3:4]
    c5 = input1[4:]

    c1display = TITLE_FONT.render(c1, True, WHITE)
    WINDOW.blit(c1display, (104, 183 + yadded))

    c2display = TITLE_FONT.render(c2, True, WHITE)
    WINDOW.blit(c2display, (170, 183 + yadded))

    c3display = TITLE_FONT.render(c3, True, WHITE)
    WINDOW.blit(c3display, (236, 183 + yadded))

    c4display = TITLE_FONT.render(c4, True, WHITE)
    WINDOW.blit(c4display, (302, 183 + yadded))

    c5display = TITLE_FONT.render(c5, True, WHITE)
    WINDOW.blit(c5display, (368, 183 + yadded))

### Draw words that have already been entered on to the screen ###
def drawWords(arr):
    
    for i in range(6):
        for j in range(5):

            x = 104 + ((j) * 66)
            y = 183 + ((i) * 66)

            if arr[i][j] == '*':
                letter = TITLE_FONT.render(' ', True, WHITE)
            else:
                letter = TITLE_FONT.render(arr[i][j], True, WHITE)
            WINDOW.blit(letter, (x, y))

### If player loses, this shows the answer ###
def drawAnswer(answer):
    result = TITLE_FONT.render(answer.upper(), True, WHITE)
    WINDOW.blit(result, (170, 700))

def drawNice():
    nice = TITLE_FONT.render("Nice!", True, WHITE)
    WINDOW.blit(nice, (190, 700))

def drawLetterResults():
    global letterlist
    green = []
    yellow = []
    gray = []
    black = []

    for i in range(26):
        if letterlist[i] == 'g':
            green.append(chr(65+i))
        elif letterlist[i] == 'y':
            yellow.append(chr(65+i))
        elif letterlist[i] == 'w':
            gray.append(chr(65+i))
        else:
            black.append(chr(65+i))

    ### convert arrays of letters into a string to display
    gr = "Green: "
    for i in range(len(green)):
        gr += green[i] + ", "

    ye = "Yellow: "
    for i in range(len(yellow)):
        ye += yellow[i] + ", "

    gra = "Gray: "
    for i in range(len(gray)):
        gra += gray[i] + ", "

    bl = "Unknown: "
    for i in range(len(black)):
        bl += black[i] + ", "

    ### cutting off extra commas ###
    if len(gr) >= 2:
        gr = gr[:len(gr)-2]
    if len(ye) >= 2:
        ye = ye[:len(ye)-2]
    if len(gra) >= 2:
        gra = gra[:len(gra)-2]
    if len(bl) >= 2:
        bl = bl[:len(bl)-2]

    g = SMALL_FONT.render(gr, True, GREEN)
    y = SMALL_FONT.render(ye, True, YELLOW)
    w = SMALL_FONT.render(gra, True, GRAY)
    ### making bl have an extra line if need be
    if len(bl) >= 41:
        b = SMALL_FONT.render(bl[:41], True, WHITE)
        b2 = SMALL_FONT.render(bl[42:], True, WHITE)
        WINDOW.blit(b2, (20, 760))
    else:
        b = SMALL_FONT.render(bl, True, WHITE)

    WINDOW.blit(g, (20, 600))
    WINDOW.blit(y, (20, 640))
    WINDOW.blit(w, (20, 680))
    WINDOW.blit(b, (20, 720))

def drawInstructions():
    s = "Press esc to quit program, press tab for new game."
    sout = SMALLEST_FONT.render(s, True, WHITE)
    WINDOW.blit(sout, (25, 100))


    
##############################
### Game-related Functions ###
##############################

### Pick word that Wordle AI will try and find ###
def generateWordList():
    wordlist = []
    with open('wordle-allowed-guesses.txt') as file:
        with open('wordle-answers-alphabetical.txt') as file2:
            wordlist = file.readlines() + file2.readlines()

    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i][:5]
        wordlist[i] = wordlist[i].upper()

    return wordlist

def pickWord():

    answerlist = []
    with open('wordle-answers-alphabetical.txt') as file:
        answerlist = file.readlines()

    word = random.choice(answerlist)

    word = word[:5]
    word = word.upper()

    return word

### Check if input word is a valid word
def checkWord(input1, wordlist):
    if(input1 in wordlist):
        return True
    return False
    

def showResults(input1, answer, colors, row):
    
    answer = answer.upper()

    #First, get all the greens
    for c in range(5):
        for a in range(5):
        
            if input1[c:c+1] == answer[a:a+1]:
                
                if c==a:
                    #green
                    colors[row][a] = 'g'
                    answer = answer[:c] + '&' + answer[c+1:]

                    #store input1[c:c+1] as a green letter
                    storeResults(input1[c:c+1], 'g')

    #Next, get all the yellow
    for c in range(5):
        for a in range(5):
        
            if input1[c:c+1] == answer[a:a+1]:
                
                #yellow
                if(colors[row][c] != 'g'):
                    colors[row][c] = 'y'
                    answer = answer[:a] + '%' + answer[a+1:]

                    #store input1[c:c+1] as a yellow letter
                    storeResults(input1[c:c+1], 'y')

    #Make everything else gray
    for i in range(5):
        if colors[row][i] != 'g' and colors[row][i] != 'y':
            colors[row][i] = 'w'
            answer = answer[:i] + '@' + answer[i+1:]

            #store input1[c:c+1] as a gray letter
            storeResults(input1[i:i+1], 'w')
    
    return colors

def checkWin(row, colors):
    #check to see if won
    for i in range(5):
        if colors[row][i] != 'g':
            return False
    return True

### store the results for each letter ###
def storeResults(letter, color):

    #A = 65
    #corresponding index in letter list = val-97

    index = ord(letter) - 65
    global letterlist
    letterlist[index] = color

### returns results array so it can be used in solve.py
def returnResults():
    global letterlist
    return letterlist
            


######################
### Main game loop ###
######################

def loop():

    ### Set up the game
    wordlist = generateWordList()
    answer = pickWord()
    
    
    run = True

    ### Setting Clock ###
    clock = pygame.time.Clock()

    ### Variables ###
    input1 = ""
    row = 0
    global words
    words = [['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*']]
    colors = [['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b'],['b','b','b','b','b']]
    win = False
    lose = False
    global letterlist
    letterlist = []
    for i in range(26):
        letterlist.append('b')
    global wipe

    
    print("ROUND: ", row)
    print("AI's Pick: ", chooseWord(letterlist, words, colors, row, wipe), '\n')
    
    wipe = False
    while run:
        clock.tick(FPS)

        ### Quit program ###
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
            exit()

        ### New game ###
        if keys[pygame.K_TAB]:
            #print("New game")
            run = False
            wipe = True
            
        ### Key input1 ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            ### Text input1 ###
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input1 = input1[:-1]
                elif event.key == pygame.K_RETURN:
                    if (len(input1) == 5 or row == 5) and checkWord(input1, wordlist):
                        ### "lock in" input as final answer ###
                        
                        if(row <= 5):
                            ### Store input ###
                            words[row][0] = input1[:1]
                            words[row][1] = input1[1:2]
                            words[row][2] = input1[2:3]
                            words[row][3] = input1[3:4]
                            words[row][4] = input1[4:]

                            colors = showResults(input1, answer, colors, row)

                            


                            win = checkWin(row, colors)
                            if(win):             
                                row = 1000
                            else:
                                #game gives advice here
                                choice = chooseWord(letterlist, words, colors, row, wipe)
                                
                                print("ROUND: ", row+1)
                                print("AI's Pick: ", choice, '\n')
                            
                            input1 = ""
                            row += 1

                            if(row == 6 and win == False):
                                lose = True
                               
                else:
                    if len(input1) < 5 and row<6:
                        l = event.unicode
                        if l.isalpha():
                            input1 += l.upper()
        
        ### Draw display ###
        draw_window(input1, row, words, colors, lose, answer, win)

def main():
    while True:
        loop()

if __name__ == "__main__":
    main()
