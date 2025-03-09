from switch import *


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"

    def is_leap_year(self):
        return ((self.year % 400 == 0) or
                (self.year % 4 == 0 and self.year % 100 != 0))

    def days_in_month(self):
        no_of_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if self.month == 2 and self.is_leap_year():
            return 29
        else:
            return no_of_days[self.month]

    def normalize(self):
        days_in_month = self.days_in_month()

        if self.day > days_in_month:
            self.month += self.day // days_in_month
            self.day %= days_in_month

        if self.month > 12:
            self.year += self.month // 12
            self.month %= 12

    def __add__(self, other):
        date = Date(self.day, self.month, self.year)

        date.day += other.day
        date.normalize()

        date.month += other.month
        date.normalize()

        date.year += other.year
        date.normalize()

        return date


def calculate_tomorrow_for_input():
    print()
    day, month, year = list(map(int, input("Input Date(DD-MM-YYYY): ").split('-')))
    tom = Date(day, month, year) + Date(1, 0, 0)
    return f"Tomorrow's Date: {tom}"


switch = Switch()
switch.add_case("Calculate Tomorrow", lambda: print(calculate_tomorrow_for_input()))
switch.run()
