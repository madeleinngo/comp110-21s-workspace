"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730272774"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str: 
    answer: int = randint(1, 100)
    if answer < 25:
        return"You will see a good doggo today."
    else:
        if answer < 50:
            return"You've got major pizazz."
        else:
            if answer < 75:
                return"Your life will be full of joy and inner peace."
            else:
                if answer < 100:
                    return"You're on your way to greatness!"
                else:
                    if answer == 100:
                        return"Congrats friend, you will receive a free boba very soon!"

# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()