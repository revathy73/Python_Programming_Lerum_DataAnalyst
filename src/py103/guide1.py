from to_do import TODO


def guide1(country: str) -> bool:
    # If country sweden gives output true
    # else false

    return country.lower() == "sweden"
    """
    if country.lower() == "sweden":
       return True
    else:
       return False
    """


if  __name__ == "__main__":

    # country = "Australia"
    print(guide1(country = "Australia"))

    # country = "India"
    print(guide1(country = "Italy"))

    # country = "Sweden"
    print(guide1(country = "Sweden"))

    # country = "sweden"
    print(guide1(country = "sweden"))

    # country = "SWEDEN"
    print(guide1(country = "SWEDEN"))

    # country = "SwEDeN"
    print(guide1(country= "SwEDeN"))


