import time
import array as arr
import os
from colorama import init
from termcolor import colored
approval = 0; reInputnum = 0; reInput = 0; exits = 0; newFlag = 0
i = 0; num = 0; mem = []; snum = 1; prmpt = str; byp = str; rep = str

init()


#Good/Bad sector state counter#

def counter():
    gsec = 0
    bsec = 0
    time.sleep(0.7)
    for i in range(0, num):
        if (mem[i] in ('g', 'G')):
            gsec += 1
        elif (mem[i] in ('b', 'B')):
            bsec += 1
    print("")
    print(colored("Number of good sectors: %d" % gsec, 'green'))
    print(colored("Number of bad sectors: %d" % bsec, 'red'))
    time.sleep(1)


#Displaying sector states#

def stream():
    time.sleep(1)
    if(newFlag == 1):
        print("\nNew data stream: ", end='')
    elif(newFlag == 0):
        print("\nData stream: ", end='')
    print("\nStart -> ", end='')
    time.sleep(0.4)
    for i in range(0, num):
        if(mem[i] in ('g', 'G')):
            print("\033[0;32m" + mem[i], end=' ')
            time.sleep(0.2)
            if(mem[i] in ('g', 'G', 'b', 'B')):
                print(end='')
        elif(mem[i] in ('b', 'B')):
            print("\033[0;31m" + mem[i], end=' ')
            time.sleep(0.2)
        else:
            continue
    print("\033[0m<- End")
    time.sleep(0.9)


#Bypassing sectors#

def bypass():
    newFlag = 1
    for i in range(0, num):
        if(mem[i] in ('g', 'G')):
            continue
        elif(mem[i] in ('b', 'B')):
            mem[i] = "skip"


#Repairing sectors#

def repair():
    newFlag = 1
    for i in range(0, num):
        if(mem[i] in ('g', 'G')):
            continue
        elif(mem[i] in ('b', 'B')):
            mem[i] = 'G'
        else:
            continue


############ Main ############

while (exits != 1):
    while (reInputnum != 1):
        try:
                     ############ Sector state input ############
            num = int(input("Number of sectors to simulate: "))
            print("")
            if (num > 0):
                print("Enter sector states (Good/Bad): ")
                for i in range(0, num):
                    mem.append(input("State of sector %d: " % snum))
                    snum += 1
                snum = 1
                          ############ Scanning sectors ############
                os.system("cls")
                print("\n\nRunning memory diagnostic...")
                time.sleep(1.5)
                print("")
                for i in range(0, num):
                    if (mem[i] in ('g', 'G')):
                        print(colored("Sector %d good" % snum, 'green'))
                        time.sleep(0.9)
                        snum += 1
                    elif(mem[i] in ('b', 'B')):
                        print(colored("\t\t\tBad sector found at %d!" % snum, 'red'))
                        time.sleep(0.9)
                        snum += 1
                    else:
                        print(colored("\t\t\t\t\t\t\tInvalid entry found at sector %d: " % snum + mem[i], 'yellow'))
                        time.sleep(0.9)
                        snum += 1
            elif(num == 0):
                exits = 1
                reInputnum = 1
                reInput = 1
                approval = 1
                           ############ Displaying scan result(s) ############
            while(approval != 1):
                stream()
                counter()
                print("" * 2)
                while(reInput != 1):
                           ############ Prompt for bypass/repair ############
                    prmpt = str(input("Proceed with bypassing / repairing sectors? (Y/N): "))
                    if(prmpt in ('y', 'YES', 'Y', 'Yes', 'yes')):
                        byp = str(input("Bypass bad sectors?: "))
                        if (byp in ('y', 'YES', 'Y', 'Yes', 'yes')):
                               ############ Bypassing sectors ############
                            print("\nAttempting to create bypasses over bad sectors...")
                            bypass()
                            newFlag = 1
                            stream()
                            counter()
                            print(colored("\nAll bad sectors have successfully been bypassed!", 'yellow'))
                            print(colored("In order to repair these bad sectors, please run", 'yellow'))
                            print(colored("the diagnostic tool again and select the repair", 'yellow'))
                            print(colored("option.", 'yellow'))

                            exits = 1
                            reInputnum = 1
                            approval = 1
                            reInput = 1
                        elif(byp in ('n', 'NO', 'N', 'No', 'no')):
                            rep = str(input("Repair bad sectors?: "))
                            if(rep in ('y', 'YES', 'Y', 'Yes', 'yes')):
                                ############ Repairing sectors ############
                                print("\nAttempting to repair bad sectors...")
                                repair()
                                newFlag = 1
                                stream()
                                counter()
                                print(colored("\nAll bad sectors have successfully been repaired!", 'yellow'))

                                exits = 1
                                reInputnum = 1
                                approval = 1
                                reInput = 1
                            elif(rep in ('n', 'NO', 'N', 'No', 'no')):
                                exits = 1
                                reInputnum = 1
                                approval = 1
                                reInput = 1
                        else:
                            print("\nInvalid input. Please try again.\n")
                    elif(prmpt in ('n', 'NO', 'N', 'No', 'no')):
                        exits = 1
                        reInputnum = 1
                        approval = 1
                        reInput = 1
                    else:
                        print("\nInvalid input. Please try again.\n")
        except:
            print("\nInvalid input. Please enter an integer value\n")
print("\nThank you for using D-DART! Press any key to exit...")
input()
