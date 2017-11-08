import string
import random
from time import sleep
def evolution(goal):
    loopcount = 0
    choices = string.ascii_letters + string.digits + '''~`!@#$%^&*()_ -+={[]}:;""'\<>,.?/|'''
    stringcount = len(goal)
    randstring = ''.join(random.choices(choices, k=stringcount))
    print("The string that will mutate into your string looks like this:\n", randstring)
    input("Press 'Enter' to start mutating!")
    while randstring != goal:
        charnum = random.randint(0, (stringcount))
        loopcount += 1
        if goal[(charnum-1):charnum] != randstring[(charnum-1):charnum]:
            replacer = random.choice(choices)
            replaced = randstring[(charnum-1):charnum]
            randlist = list(randstring)
            randlist[(charnum - 1)] = replacer
            randstring = ''.join(randlist)
            if loopcount % 200 == 0:
                print("After ", loopcount," loops, this is the string:\n", randstring)
                sleep(0.5)
    print("Done! After ", loopcount, "loops, the mutated string now looks like this:\n", randstring)
if __name__ == '__main__':
    usergoal = input("Choose a string and watch another string mutate into it!\n> ")
    evolution(usergoal)
