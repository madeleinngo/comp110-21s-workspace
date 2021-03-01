"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730272774"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    day_datetime: str = future_date(days)
    # TODO 5: Print the expected output using the variables above.
    target_str: str = str(target)
    days_str: str = str(days)
    print("We will reach " + target_str + "% vaccination in " + days_str + " days, which falls on " + day_datetime + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculates days to reach target vaccination."""
    target_percent: float = float(target * 0.01)
    current_percent: float = float(doses // (population * 2))
    x: float = float(target_percent - current_percent)
    round(x)
    vaccines_still_needed: int = int((x * population) * 2)
    days: int = int(vaccines_still_needed // doses_per_day)
    round(days)
    return days


# TODO 3: Define future_date function
def future_date(days_new: int) -> str:
    """Calculates date of when target vaccination reached."""
    today: datetime = datetime.today()
    day_vac: timedelta = timedelta(days_new)
    day_vac_datetime: datetime = today + day_vac
    return day_vac_datetime.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
