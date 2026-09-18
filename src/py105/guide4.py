"""
You are given a map called supermarket in which the keys are the names of
products and the values are their prices.

You are also given a list called ingredients, which is a list of ingredients
you need to buy.

Calculate how much it will cost you to buy all the ingredients.

In case an ingredient from the list is not available in the supermarket,
then it means you cannot buy it.

Save your result in a variable called result

Example Solution
Assume that
supermarket is
{
    "cheese" to 10.0,
    "eggs" to 5.0,
    "milk" to 30.0
}
ingredients is
["cheese", "eggs", "juice"]
Then
result is 15.0
Module 105
"""
from to_do import TODO


def guide4(supermarket: dict[str, float], ingredients: list[str]) -> float:

    result = 0.0
    for item in ingredients:
        cost = supermarket.get(item, 0.0)
        result += cost

    return result


if __name__ == "__main__":

    #supermarket = {"cheese": 10.0,"eggs": 5.0,"milk": 30.0},ingredients = ["cheese", "eggs", "juice"]
    print(guide4(supermarket = {"cheese": 10.0,"eggs": 5.0,"milk": 30.0},
                 ingredients = ["cheese", "eggs", "juice"]))
