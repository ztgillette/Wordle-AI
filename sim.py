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
    numOfRounds += 0.5
    global average
    average = sumOfRounds / numOfRounds
    
for i in range(TESTS*2):

    game.loop()
    rounds = game.getRounds()
    calcAverage(rounds)

print(average)
