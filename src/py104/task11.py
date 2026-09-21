"""
In each question you are given the variable guests. It represents a list
of people attending an event.

Each attendee in guests has one of the following conditions at the end of
their name:

Vegetarian: Specified by the -V
Allergic: Specified by the -A
Brings kids: Specified by the -K
Use this information to solve the questions below.

How many people are attending the event?

Save your result in a variable called result.

Example Solution
Assume that
guests is
["Lia-K", "Mar-A", "Luz-K","Ulf-V"]
Then
result is 4
"""

from to_do import TODO


def task11(guests: list[str]) -> int:

    result = len(guests)
    return result

if __name__ == "__main__":
    guest_list = [
        "Stéphanie-A",
        "Edmée-K",
        "Maëlla-K",
        "Océanne-K",
        "Géraldine-K",
        "Maëline-K",
    ]

    # NOTE: Uncomment the code below when you are ready to test your answers
    print(f"The event has a total of {task11(guest_list)} guests.")
