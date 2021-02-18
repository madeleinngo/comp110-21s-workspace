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
    days_new: int = days_to_target(population, doses, doses_per_day, target)
    print(days_new)
    # TODO 4: Call future_date and store result in a variable.
    day_vac_datetime: str = future_date(days_new)
    # TODO 5: Print the expected output using the variables above.
    target_str: str = str(target)
    days_new_str: str = str(days_new)
    print("We will reach " + target_str + "% vaccination in " + days_new_str + " days, which falls on " + day_vac_datetime + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    target_percent: int = int(target * 0.01)
    target_population: int = int(target_percent * population)
    amount_doses: int = int(target_population * 2)
    days: int = int(amount_doses // doses_per_day)
    days_started: int = int(doses // doses_per_day)
    days_new: int = int(days - days_started)
    days_new: int = int(round(days_new))
    return days_new


# TODO 3: Define future_date function
def future_date (days_new: int) -> str:
    today: datetime = datetime.today()
    day_vac: timedelta = timedelta(days_new)
    day_vac_datetime: datetime = today + day_vac
    return day_vac_datetime.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
