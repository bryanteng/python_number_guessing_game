import random
def start():
    user_input = 0
    random_num = str(random.randint(1,6))
    print(random_num)
    while user_input != "exit" or user_input != random_num:
        user_input = str(input("guess a number : "))
        if user_input == random_num:
            print("you win i guess")
            break

start()
