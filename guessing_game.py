import random
import time
import sys

def start(num):
    user_input = 0
    nums = range(1,int(num)+1)
    animation = ''.join(str(num) for num in nums)

    print("Picking a random number ")
    for i in range(50):

        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print "\nDone!"
    sys.stdout.flush()

    random_num = str(random.randint(1,int(num)))
    print(random_num)
    while user_input != "exit" or user_input != random_num:
        user_input = raw_input("guess a number : ")
        if user_input == random_num:
            print("you win!")
            break;
        elif user_input == "exit":
            print("cya!")
            break;
        else:
            print("incorrect! guess again!")

start(raw_input("Pick an upperbound of numbers to guess between! : 1 .. "))
