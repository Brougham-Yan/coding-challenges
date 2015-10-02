#this program finds all possible combinations of coins in pound sterling in which the sum is 2£
moneyNames = ["1p", "2p", "5p", "10p", "20p", "50p", "1£", "2£"]
money = [0, 0, 0, 0, 0, 0, 0, 0]
combinations = 0

def checkForSum():
    sum = money[0] + (2 * money[1]) + (5 * money[2]) + (10 * money[3]) + (20 * money[4]) + (50 * money[5]) + (100 * money[6]) + (200 * money[7])
    if(sum < 200):
        money[0] = 200 - sum
        sum = 200
    if(sum == 200):
        for i in range(7):
            if money[i] > 0:
                print(money[i], end="*")
                print(moneyNames[i], end=", ")
        print("")
        return 1
    return 0

while(money[7] < 1):
    money[0] = 0

    combinations+= checkForSum()

    if(money[1] > 99): #2p
        money[1] = 0
        money[2]+= 1
        combinations+=checkForSum()
    if(money[2] > 39): #5p
        money[2] = 0
        money[3]+= 1
        combinations+=checkForSum()
    if(money[3] > 19): #10p
        money[3] = 0
        money[4]+= 1
        combinations+=checkForSum()
    if(money[4] > 9): #20p
        money[4] = 0
        money[5]+= 1
        combinations+=checkForSum()
    if(money[5] > 3): #50p
        money[5] = 0
        money[6]+= 1
        combinations+=checkForSum()
    if(money[6] > 1): # 1£
        money[6] = 0
        money[7]+= 1
        combinations+=checkForSum()
    money[1]+=1

print("There are ", combinations, " ways you can have 2£")
input("press enter to continue...")
