import game

### this file will simulate games to determine the AI's average 
# score (how many rounds it takes)

### CHANGE THIS VALUE TO CHANGE NUMBER OF SIMULATIONS ###

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

#sim loop
for i in range(TESTS):

    print("### SIMULATION", i, "###")
    game.loop(True)

    ### Use pyautogui to get the guess, type it in, 
    # and once won, click tab to begin new game

    rounds = game.getRounds()
    calcAverage(rounds)

print(average)

with open('results.txt', 'w') as f:
    f.write(str(average))
