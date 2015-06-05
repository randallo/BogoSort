import random
import time

def inputListAmount():
    n = raw_input ("How many numbers do you want in the list? ")
    while (not n.isdigit()) or (int(n)< 1):
        n = raw_input ("Error. Please enter a whole number greater than 0: ")
    n = int(n)
    
    return n

def generateList(size):
    list = []
    for i in range(0, size):
        list.append(i)
    
    return list

def listRandomizer(list):
    random.shuffle(list)
    
    return list

def sort(list, n):
    counter = 0
    while sorted(list) != list:
        print list
        FirstIndex = random.randint(0, n-1)
        SecondIndex = random.randint(0, n-1)
        while FirstIndex == SecondIndex:
            SecondIndex = random.randint(0, n-1)
        list[FirstIndex], list[SecondIndex] = list[SecondIndex], list[FirstIndex]
        counter = counter + 1
    
    return counter

def repeat():
    choice = raw_input ("Would you like to run BogoSort again? ")
    choice = choice.lower()
    while not(choice == 'yes' or choice == 'no' or choice == 'y' or choice == 'n'):
        choice = raw_input ("Invalid input. Please input 'Yes' or 'No': ")
    
    if choice == 'yes' or choice == 'y':
        print "\n"
        return True
    else:
        print " "
        return False

def main():
    size = inputListAmount()
    timerBegin = time.time()
    list = generateList(size)
    list = listRandomizer(list)
    count = sort(list, size)
    print count, "attempts"
    timerEnd = time.time()
    if (timerEnd - timerBegin) > 60:
        print "BogoSort took", (timerEnd - timerBegin)/60, "minutes to sort", size, "numbers."
    else:
        print "BogoSort took", (timerEnd - timerBegin), "seconds to sort", size, "numbers."
    
    if repeat():
        main()
    
main()
    
    
        