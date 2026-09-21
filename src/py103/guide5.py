"""
You are given the variable capital, which represents the capital of a
country. Determine if the given capital is Sweden’s capital.

Save your result in a variable called result

Example Solution
Assume that
capital is Oslo
Then
result is false
Note
Your solution cannot be case sensitive
"""

from to_do import TODO


def guide5(capital: str) -> bool:

    # Input capital
    # If the capital is stockholm
         # set the result to be True
    # else entered other capital of the country
         # set the result to be false
    # return the result


    if capital.lower() == "stockholm":
         result = True
    else:
         result = False

    return result


    #return capital.lower() == "stockholm"

if __name__ == "__main__":

    # capital = Oslo ---> False
    print(guide5(capital = "Oslo"))

    # capital = Stockholm ---> True
    print(guide5(capital = "Stockholm"))

    # capital = Rome ---> False
    print(guide5(capital = "copenhagen"))

    # capital = StoCkHoLM ---> True
    print(guide5(capital="StoCkHoLM"))

    # capital = stockholm ---> True
    print(guide5(capital="stockholm"))

    # capital = STOCKHOLM ---> True
    print(guide5(capital="STOCKHOLM"))

