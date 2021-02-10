"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730272774"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
answer: int = randint(1, 100)
print("Your fortune cookie says... ")
if answer < 25:
    print("You will see a good doggo today.")
else:
    if answer < 50:
        print("You've got major pizazz.")
    else:
        if answer < 75:
            print("Your life will be full of joy and inner peace.")
        else:
            if answer < 100:
                print("You're on your way to greatness!")
            else:
                if answer == 100:
                    print("Congrats friend, you will receive a free boba very soon!")

print("Now, go spread positive vibes!")
