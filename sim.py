import game
import time

### this file will simulate games to determine the AI's average 
# score (how many rounds it takes)

### CHANGE THIS VALUE TO CHANGE NUMBER OF SIMULATIONS ###

TESTS = 1000
###

sumOfRounds = 0
numOfRounds = 0
averageRounds = 0

def calcAverage(rounds):
    global sumOfRounds
    global numOfRounds
    sumOfRounds += rounds
    numOfRounds += 1
    global averageRounds
    averageRounds = sumOfRounds / numOfRounds

wins = 0
solveRate = 0

def calcSolveRate(win, games):
    global wins
    global solveRate
    if(win):
        wins += 1
    solveRate = float((wins)/(games+1))


######################
# SIMULATION SECTION #
######################

start = time.time()

#sim loop
for i in range(TESTS):

    print("### SIMULATION", i+1, "###")
    game.loop(True)

    ### Use pyautogui to get the guess, type it in, 
    # and once won, click tab to begin new game

    rounds = game.getRounds()
    win = game.getWin()
    calcAverage(rounds)
    calcSolveRate(win, i)

end = time.time()
runtime = end - start

results = "\n\nRESULTS:" + "\n\nSimulations: " + str(numOfRounds) + "\nWin Rate (%): " + str(solveRate * 100) + "\nAvg Rounds/Solve: " + str(averageRounds) + "\n\nRuntime (s): " + str(runtime)

print(results)

with open('results.txt', 'w') as f:
    f.write(str(results))
