population = int(input("Population size: "))
dead_cnt = 0
lst = ["alive"]*population
turn = 0
while(dead_cnt!= (population-1)):
    if(lst[turn%population]=="alive"):
        turn_temp = turn%population+1
        while(lst[turn_temp%population]=="dead"):
            turn_temp += 1
        lst[turn_temp%population] = "dead"
        dead_cnt += 1
    turn+=1
for i in range (population):
    if(lst[i] == "alive"):
        print("The winning number is: ", i+1)
        break