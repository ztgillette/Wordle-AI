import game

### this file will simulate games to determine the AI's average 
# score (how many rounds it takes)

TESTS = 4
###

sumOfRounds = 0
numOfRounds = 0
average = 0

def calcAverage(rounds):
    global sumOfRounds
    global numOfRounds
    sumOfRounds += rounds
    numOfRounds += 1
    global average
    average = sumOfRounds / numOfRounds

######################
# SIMULATION SECTION #
######################

for i in range(TESTS):

    game.loop()

    ### Use pyautogui to get the guess, type it in, 
    # and once won, click tab to begin new game

    rounds = game.getRounds()
    calcAverage(rounds)

print(average)
