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

    # capital = Rome ---> True
    print(guide5(capital = "copenhagen"))

    # capital = StoCkHoLM ---> True
    print(guide5(capital="StoCkHoLM"))

    # capital = stockholm ---> True
    print(guide5(capital="stockholm"))

    # capital = STOCKHOLM ---> True
    print(guide5(capital="STOCKHOLM"))
