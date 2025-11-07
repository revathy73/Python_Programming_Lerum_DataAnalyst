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

