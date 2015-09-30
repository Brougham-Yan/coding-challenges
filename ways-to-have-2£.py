#NOT ACTUALLY DONE YET
moneyNames = ["1p", "2p", "5p", "10p", "20p", "50p", "1£", "2£"]
money = [0, 0, 0, 0, 0, 0, 0, 1]
print("1*2£")
combinations = 1
while(money[0] < 199):
    if(money[1] > 0): #2p -> 2*1p
        money[1]-=1
        money[0]+=2
    elif(money[2] > 0): #5p -> 2*2p + 1p
        money[2]-=1
        money[1]+=2
        money[0]+=1
    elif(money[3] > 0): #10p -> 2*5p
        money[3]-=1
        money[2]+=2
    elif(money[4] > 0): #20p -> 2*10p
        money[4]-=1
        money[3]+=2
    elif(money[5] > 0): #50p -> 2*20p + 10p
        money[5]-=1
        money[4]+=2
        money[3]+=1
    elif(money[6] > 0): #1£ -> 2*50p
        money[6]-=1
        money[5]+=2
    elif(money[7] > 0): #2£ -> 2*1£
        money[7]-=1
        money[6]+=2
    for i in range(7):
        if money[i] > 0:
            print(money[i], end="*")
            print(moneyNames[i], end=", ")
    combinations +=1
    print("")


print("There are ", combinations, " ways you can have 2£")
input("press enter to continue...")
