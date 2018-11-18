import random
import time
import sys

def start(num):
    while int(num) <= 1:
        num = raw_input("Please pick a number greater than 1: ")
    user_input = 0
    nums = range(int(num)+1)
    animation = ''.join(str(num) for num in nums)
    tries = 0

    print("Picking a random number ")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print "\nRandom number selected!"
    print "You have a " + str(1/float(num)*100) +"% chance of getting it right on the first try!"
    sys.stdout.flush()

    random_num = str(random.randint(1,int(num)))

    while user_input != "exit" or user_input != random_num:
        user_input = raw_input("guess a number or type exit to end the game : ").strip()
        tries+=1
        if user_input == random_num:
            print("you win! It took you " + str(tries) + " tries!")
            break;
        elif user_input == "exit":
            print("cya!")
            break;
        else:
            print("incorrect! guess again!")
            if tries != 1:
                print "You now have a " + str(tries/float(num)*100) +"% chance of getting it right!"



start(raw_input("Pick an upperbound of numbers to guess between! : 1 .. "))
