numExclamPoints = 1

def hello():
    global numExclamPoints
    print("Hello" + ("!" * numExclamPoints))
    numExclamPoints += 1

for i in range(20):
    hello()