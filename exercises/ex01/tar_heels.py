"""An exercise in remainders and boolean logic."""

__author__ = "730272774"


# Begin your solution here...49
answer: int = int(input("Enter an int:"))
if answer % 2 == 0 and answer % 7 == 0:
    print("TAR HEELS")
else:
    if answer % 2 == 0:
        print("TAR")    
    else:
        if answer % 7 == 0:
            print("HEELS")
        else:
            print("CAROLINA")