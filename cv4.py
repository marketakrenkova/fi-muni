from random import random, randint

def dice():
    return randint(1, 6)

def turn():
    suma = 0
    n = 2
    while n % 2 == 0:
        n = randint(1, 6)
        suma += n
        #print(n)
    return suma

def drunkman_simulator(size, steps, output=False):
    position = size//2
    for i in range(steps):
        move = randint(1, 2)
        if move == 1:     #go right
            position += 1
            #print("home", (position-1)*".", "*", (size-position)*".", "pub")
        else:            #go left
            position -= 1
            #print("home", (position-1)*".", "*", (size-position)*".", "pub")

        if position == 0:
            #print("Ended at home.")
            return True
        elif position == (size+1):
            #print("Ended in the pub again.")
            return False
    #print("Drunkman fell asleep in the street.")
    
def drunkman_analysis(size, steps, count):
    home = 0
    for i in range(count):
        if drunkman_simulator(size, steps, output=False) == True:
            home += 1
    print("Arriving home in ",home/count*100, "% of cases.")
    
    
