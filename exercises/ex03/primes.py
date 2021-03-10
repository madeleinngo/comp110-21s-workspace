"""EX03 - prime functions."""

__author__: str = "730272774"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(5))
    print(list_primes(10, 20))


def is_prime(a: int) -> bool:
    if a <= 1:
        return False
    while a > 1: 
        if a % 1 == 0 and a % a == 0 and a % 2 == 0:
            return False
        return True


def list_primes(a: int, b: int) -> list[int]:
    xs: list[int] = []
    i: int = 0 
    c: int = range(1, len(b), b - 1)
    while i < c:
        if is_prime(i):
            xs.append[i]
            i += 1
        else:
            i += 1
        return 


if __name__ == "__main__":
    main()
