"""
You are given a map called supermarket in which the keys are product names
and the values are another map with information about the product.

Determine the name of the cheapest product and save your result in a variable
called result

Example Solution
Assume that
supermarket is
{
    "milk" to {
        "price" to 10.5,
        "brand" to "Bonlac"
    },
    "cheese" to {
        "price" to 5.2,
        "brand" to "Young"
    },
    "yogurt" to {
        "price" to 3.0,
        "brand" to "Bonlac"
    },
}
Then
result is yogurt
Hint
The inner map will always have a key called price where you can find the price
of the product.
"""

from typing import Any
import math
from to_do import TODO


def guide19(supermarket: dict[str, dict[str, Any]]) -> str:

    cheapest_product = ""
    cheapest_price = math.inf

    for product,details in supermarket.items():
         prod_price = details["price"]
         if prod_price < cheapest_price:
             cheapest_product = product
             cheapest_price = prod_price

    return cheapest_product

if __name__ == "__main__":

    grocery = {"milk":{"price":10.5,"brand":"Bonlac"},
               "cheese":{"price":5.2,"brand":"Young"},
               "yogurt":{"price":3.0,"brand":"Bonlac"}}
    print(guide19(supermarket = grocery))

