"""EX03 - avoid_fifth function."""

__author__: str = "730272774"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("The sentence we have here possesses E's galore!"))
    print(avoid_fifth("hello"))


def avoid_fifth(a: str) -> str:
    """Output a string without any e's in it."""
    i: int = 0
    b: str = ""
    while i < len(a):
        if a[i] == "e" or "E":  # ignore the e, move on, then put the other letters that are not e into the new variable for output
            i += 1
        else:
            b += a[i]
            i += 1
    return b


if __name__ == "__main__":
    main()
