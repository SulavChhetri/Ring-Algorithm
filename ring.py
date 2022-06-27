#initalizing the leader variable
leader = 1
#taking the number of input processes and their status, while choosing the leader which is the highest active input process
numberProcess = int(input("Enter the number of processes : "))
numberProcessList = list()
for i in range(1,numberProcess+1):
    numberProcessList.append(i)
statuslist = list()
for i in range(numberProcess):
    #A process can either be active-> 1 or inactive-> 0
    n = int(input(f"Enter the status of the process {numberProcessList[i]} - active/inactive(1/0) : "))
    statuslist.append(n)
    if(statuslist[i]):
        leader = i+1
#display function for all the processes and their status, and the leader of the election
def display(leader):
    print("\n")
    print("\n")
    print("Processes : \n")
    for i in numberProcessList:
        print(f'{i}',end="\t")
    print('\n')
    print("Alive  : \n")
    for i in statuslist:
        print(f'{i}',end="\t")
    print("\n")
    print(f"The leader is : {leader}\n")

#ring algorithm function
def ring(leader):
    print("Enter")
    print("1.Crash\n2.Activate\n3.Display\n4.Exit\n")
    ring = int(input())
    #Using a loop untill the user input the correct options out of 1, 2, 3, 4
    while(True):
        if ring == 1:
            crashID = int(input(f"Enter a process to crash : (1 to {numberProcessList[-1]}) : "))
            if(statuslist[crashID-1]):
                statuslist[crashID-1] = 0
                print(f"Process {crashID} is crashed.\n")
            elif(statuslist[crashID-1] ==0):
                print(f"Process {crashID} is already dead.\n")
            elecGen = int(input("Enter the process to generate the election leader : "))
            while True:
                if statuslist[elecGen-1] == 0:
                    print('Cannot generate a election from a crashed process\n')
                    elecGen = int(input("Enter a alive process to generate the election leader : "))
                else:
                    break
            while(leader == elecGen):
                print("Enter a valid leader.")
                elecGen = int(input("Enter the process to generate the election leader : "))
            print('\n')
            if(leader == crashID):
                i = elecGen+1
                while (True):
                    print(f"Message is sent from {elecGen} to {i}")
                    if(elecGen==i):
                        break
                    if statuslist[i-1]:
                        if i>elecGen:
                            print(f"Response is sent from {i} to {elecGen}")
                            elecGen = i
                    
                    if(i == len(numberProcessList)):
                        i = 1
                    else:
                        i=i+1
                    print('\n')
                leader = elecGen
            display(leader)
            break
        elif ring==2:
            activateID = int(input(f"Enter a process to activate : (1 to {numberProcessList[-1]}) : "))
            if(statuslist[activateID-1]==0):
                statuslist[activateID-1]=1
            elif(statuslist[activateID-1]):
                print("The process is already alive. ")
            if activateID == len(numberProcessList):
                j = 1
            if activateID <len(numberProcessList):
                j = activateID+1 
            while (True):
                print(f"Message is sent from {activateID} to {j}")
                if(activateID==j):
                    break
                if statuslist[j-1]:
                    if j>activateID:
                        print(f"Response is sent from {j} to {activateID}")
                        activateID = j
                    
                if(j == len(numberProcessList)):
                    j = 1
                else:
                    j=j+1
                print('\n')
            leader = activateID
            display(leader)
            break
        elif ring ==3:
            display(leader)
            break
        elif ring ==4:
            exit()
        else:
            print("Enter correct input : ")
            print("1.Crash\n2.Activate\n3.Display\n4.Exit\n")
            ring = int(input())

print('\n')
print("Enter : ")
print("1.Ring Algorithm\n2.Display\n3.Exit\n")
decision = int(input())
while(True):
    if decision ==1:
        ring(leader)
        break
    elif decision == 2:
        display(leader)
        break
    elif decision ==3:
        exit()
    else:
        print("Enter correct input : ")
        print("1.Ring Algorithm\n2.Display\n3.Exit\n")
        decision = int(input())