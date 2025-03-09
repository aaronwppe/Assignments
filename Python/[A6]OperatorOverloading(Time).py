from switch import *


class NegativeTime(Exception):
    pass


class Time:
    def __init__(self, hrs=0, mins=0):
        if hrs < 0 or mins < 0:
            raise NegativeTime

        self.hrs = hrs
        self.mins = mins
        self.normalise()

    def normalise(self):
        hrs = self.mins // 60
        self.mins %= 60
        self.hrs += hrs

    def in_minutes(self):
        return self.mins + (self.hrs * 60)

    def __add__(self, other):
        mins = self.mins + other.mins
        hrs = self.hrs + other.hrs
        return Time(hrs, mins)

    def __lt__(self, other):
        return self.in_minutes() < other.in_minutes()

    def __sub__(self, other):
        if self < other:
            mins = other.in_minutes() - self.in_minutes()
        else:
            mins = self.in_minutes() - other.in_minutes()

        return Time(0, mins)

    def __mul__(self, n):
        mins = self.in_minutes() * n
        return Time(0, mins)

    def __str__(self):
        return f"({self.hrs}:{self.mins})"


def multiply(time: Time):
    n = input("Multiply by: ")
    if n.isnumeric():
        return f"t1{time} * {n} = {time * int(n)}"
    else:
        return "ERROR: Value provided is not numeric!"


def input_time(prompt):
    break_line = "\n" + ("=" * 20) + "\n"

    print(prompt)
    hrs = int(input("Hours: "))
    mins = int(input("Minutes: "))

    try:
        time = Time(hrs, mins)
        print(f"Time set to {time}", end=break_line)
    except NegativeTime:
        print(f"ERROR: Time cannot be negative!")
        time = input_time(prompt)

    return time


t1 = input_time("Set Time t1")
t2 = input_time("Set Time t2")

switch = Switch()
switch.add_case("Addition", lambda: print(f"t1{t1} + t2{t2} = {t1 + t2}"))
switch.add_case("Difference", lambda: print(f"Difference between t1{t1} and t2{t2} = {t1 - t2}"))
switch.add_case("Multiply t1", lambda: print(multiply(t1)))

switch.run()
