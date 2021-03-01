"""First project for COMP 110."""

__author__ = "730272774"


def main() -> None:
    """Entrypoint of the program."""
    greet()
    PLAYER: str = str("")
    POINTS: int = int(0)
    EMOJI: str = str("\U0001FD90")
    choice: str = str(input("What would you like to do? explore room 1/explore room 2/exit"))
    if choice == "exit":
        return "Thanks for playing, see you later!"
    else:
        if choice == "explore room 1":
            room_1()
        else:
            if choice == "explore room 2":
                room_2(points)


def greet() -> None:
    """Greets the player when beginning game."""
    global PLAYER
    PLAYER: str(input("Hi! Welcome, what's your name?"))
    print(f"Hi {PLAYER}! Glad you could join us for this choose your own adventure game.")
    return


def room_1() -> None:
    """Starts exploration of room 1."""
    global EMOJI
    global PLAYER
    print(f"This game experience will have you search through mystery room 1 {EMOJI}!")
    print("Let's get to it!")
    choice_1: int(input(f"To begin,{PLAYER}, how many letters are in your name?"))
    choice_1_added: int = randint(1, 100) + choice_1
    global POINTS
    if choice_1_added % 2 == 0:
        print("\U0001F34E")
        POINTS += 100
        print("Congratualations, you've found an apple! You get one hundred points!")
    else: 
        print("\U0001F34A")
        POINTS += 50
        print("Congratualtions, you've found an orange! You get 100 points!")
    choice_2: str(input("Nice! You've found one fruit. Now choose between option one or two."))
    if choice_2 == "one":
        print("\U0001F9FA")
        POINTS += 100
        print("You've found a basket! You get 100 more points.")
    else:
        print("\U0001F37D")
        POINTS += 200
        print("Wow, you've found a plate and utensils kit! You get 200 more points.")
    choice_3: str(input("Last choice, hot or cold?"))
    if choice_3 == "hot":
        print("\U00012615")
        POINTS += 200
        print("Nice, you've got a hot beverage! You get 200 more points.")
    else:
        print("\U0001F379")
        POINTS += 150
        print("Nice, you've got a tropical drink! You get 150 more points.")
    final_choice: str(input("Can you guess what this room is for?"))
    if final_choice == "picnic":
        print("\U0001F60E")
        POINTS += 1000
        print("Amazing! You guessed it correctly! Therefore you get 1000 points!")
    else:
        if final_choice == "food":
            print("\U0001F609")
            POINTS += 500
            print("You're really close! But this room is specifically for a picnic. You get 500 points!")
        else:
            print("\U0001F62E")
            POINTS += 100
            print("Sorry, that's not exactly it. This room is for a picnic! You get 100 points for guessing.")
    print("Thanks for exploring this room! You can continue to explore the other room or quit at main!")
    return 


def room_2(points: int) -> int:
    """Starts exploration of room 2."""
    global EMOJI
    global PLAYER
    print(f"This game experience will have you search through mystery room 2 {EMOJI}.")
    print("Let's get to it!")
    choice_1: str(input(f"First, {PLAYER}, how many vowels does your name have?"))
    if choice_1 == "2":
        print("\U0001F33B")
        points += 100
        print("You found a sunflower! 100 points are awarded to you.")
    else:
        print("\U0001F335")
        points += 75
        print("You found a catcus! 75 points are awarded to you.")
    choice_2: str(input("Next, water or air?"))
    if choice_2 == "water":
        print("\U0001F438")
        points += 150
        print("You've found a nice frog boy! Here's 100 points for you!")
    else:
        print("\U0001F98B")
        points += 100
        print("You've found a nice butterfly! Here's 100 points for you!")
    choice_3: str(input("Last choice, round or straight?"))
    if choice_3 == "round":
        print("\U0001F344")
        points += 150
        print("You've found a big mushroom to sit on. 150 points for you!")
    else:
        print("\U0001FAB5")
        points += 100
        print("You've found a sturdy wooden log to sit on. 100 points for you!")
    final_choice: str(input("Now that you've got all your things, what do you think this room is?"))
    if final_choice == "garden":
        print("\U0001F3E1")
        points += 1000
        print("Wow, you got it! For that guess, you get 1000 points!")
    else:
        print("\U0001F140")
        points += 100
        print("Not quite, this room is the garden of the house. For your guess though, you get 100 points!")
    print("Thanks for exploring this room! You can continue to explore the other room or quit at main!")
    return points


if __name__ == "__main__":
    main()
