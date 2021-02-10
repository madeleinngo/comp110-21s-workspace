"""A vaccination calculator."""

__author__ = "730272774"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population:"))
doses_administered: int = int(input("Doses administered:"))
doses_per_day: int = int(input("Doses per day:"))
target_percent_vaccinated: int = int(input("Target percent vaccinated:"))
days_started: int = int(doses_administered // doses_per_day)
target_percent_vaccinated_float: float = float(target_percent_vaccinated * 0.01)
target_per_vac_str: str = str(target_percent_vaccinated)
target_population: int = int(target_percent_vaccinated_float * population)
amount_of_doses: int = int(target_population * 2)
days: int = int(amount_of_doses // doses_per_day)
updated_days: int = int(days - days_started)
days_new: int = int(round(updated_days))
upd_day_str: str = str(days_new)
today: datetime = datetime.today()
day_vac: timedelta = timedelta(days_new)
day_vac_datetime: datetime = today + day_vac
print("We will reach " + target_per_vac_str + "% vaccination in " + upd_day_str + " days, which falls on " + day_vac_datetime.strftime("%B %d, %Y"))