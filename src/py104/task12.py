"""
In each question, you are given the variable guests. It represents a list of people attending an event.

Each attendee in guests has one of the following conditions at the end of
their name:

Vegetarian: Specified by the -V
Allergic: Specified by the -A
Brings kids: Specified by the -K
Use this information to solve the questions below.

Besides guests, you are given the variable condition.

Filter guests to only have the attendees with the specified condition.

Save your result in a variable called result.

Example Solution
Assume that
condition is -K
guests is
["Lia-K","Mar-A", "Luz-K","Ulf-V"]
Then
result is ["Lia-K", "Luz-K"]
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task12(guests: list[str], condition: str) -> list[str]:

    result = []
    for name in guests:
        if name[-2:] == condition:
            result.append(name)
    return result

if __name__ == "__main__":
    # Change the situation to either "-V", "-A", or "-K" to test your code under different situation
    situation = "-A"
    guest_list = [
        "Stéphanie-A",
        "Edmée-K",
        "Maëlla-K",
        "Océanne-K",
        "Géraldine-K",
        "Maëline-K",
    ]

    # NOTE: Uncomment the code below when you are ready to test your answers
    print(
        f"The attendees with condition '{situation}' are {task12(guest_list, situation)}"
    )
