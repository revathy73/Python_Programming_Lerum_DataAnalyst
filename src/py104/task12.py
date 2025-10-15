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
