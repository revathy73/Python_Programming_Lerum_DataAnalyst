"""
Create an enum class called Pizza which contains the following values:

Small
Medium
Large
Family
You are given a variable called attendees which represents the number of people attending an event. Based on the number of attendees, the host will order the appropriate pizza size.

Determine how big the pizza needs to be and save the result in a variable called result

Assume the following:

A Small pizza is ideal for 1 to 3 people
A Medium pizza is ideal for 4 to 6 people
A Large pizza is ideal for 7 to 9 people
A Family pizza is ideal for 10 to 12 people.
Notes
Assume that attendees will always be a number between 1 and 12
"""
from to_do import TODO
from enum import Enum

class Pizza(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    FAMILY = 4


def guide2(attendees: int) -> Pizza:
    if attendees in range(1, 4):
        return Pizza.SMALL
    elif attendees in range(4, 7):
        return Pizza.MEDIUM
    elif attendees in range(7, 10):
        return Pizza.LARGE
    else:
        return Pizza.FAMILY
