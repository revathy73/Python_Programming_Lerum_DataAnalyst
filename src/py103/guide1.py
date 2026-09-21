"""
You are given the variable country which represents a country in the world.

Create a solution that returns true when the given country is Sweden and
false for all other countries.

Save your result in a variable called result.

Example Solution 1
Assume that
country is Panama
Then
result is false
Example Solution 2
Assume that
country is Sweden
Then
result is true
Note
Your solution cannot be case sensitive
"""
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


