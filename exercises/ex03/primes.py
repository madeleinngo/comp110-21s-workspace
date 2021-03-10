"""EX03 - prime functions."""

__author__: str = "730272774"


def main() -> None:
    """Entrypoint of the program."""


def is_prime(a: int) -> bool:
    """Verifies if a number is prime."""
    if a <= 1:
        return False
    while a > 1: 
        if a % 1 == 0 and a % a == 0 and a % 2 == 0:
            return False
    return True


def list_primes(a: int, b: int) -> list[int]:
    """Outputs list of possibly prime numbers."""
    xs: list[int] = []
    while a < b:
        if is_prime(a):
            xs.append(a)
            a += 1
        else:
            a += 1
    return xs


if __name__ == "__main__":
    main()
