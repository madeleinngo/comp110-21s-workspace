"""EX03 - palindromify function."""

__author__: str = "730272774"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))
    print(palindromify("han", True))
    print(palindromify("race", False))
    print(palindromify("live on time ", False))


def palindromify(a: str, b: bool) -> str:
    """Makes inputs into palindromes."""
    word: str = a
    if b:
        # for even or true inputs
        i: int = 0 
        d: int = (len(a) - 1)
        while i < len(a):
            word += a[d]
            i += 1
            d -= 1
        return word
    else:
        # for odd or false inputs
        i: int = 0 
        d: int = (len(a) - 2)
        while i < (len(a) - 1):
            word += a[d]
            i += 1
            d -= 1
        return word


if __name__ == "__main__":
    main()
