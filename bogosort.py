#BogoSort "sorts" a list by swaping two random indices
#until the list is in ascending order

import random
import time


#User can input how many numbers they want to be sorted
#I don't recommend going above 10
def inputListAmount():
    n = raw_input ("How many numbers do you want in the list? ")
    while (not n.isdigit()) or (int(n)< 1):
        n = raw_input ("Error. Please enter a whole number greater than 0: ")
    n = int(n)
    
    return n


#Makes a list with size of the input
#For example: Inputting 4 would generate [0, 1, 2, 3]
def generateList(size):
    list = []
    for i in range(0, size):
        list.append(i)
    
    return list


#Shuffles list since it was created in ascended order
def listRandomizer(list):
    random.shuffle(list)
    
    return list


#Sorting algorithm. Two random indices are chosen and its respective
#values are swapped.
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


#User can choose to run the program again
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
    
    
        