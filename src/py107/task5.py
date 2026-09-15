"""
Create a function called groceries that satisfies the following requirements:

1. One argument of type List<Map<String, Any>>.
2. The return type is a Double.
3. The function takes as argument a List of Maps. Each element in the list represents
a grocery item that has price and quantity. The function returns the total price
of the shopping cart.
Example Solution #1::
1) Assume the input is
[
    {
        "product" to "Milk",
        "quantity" to 1,
        "price" to 1.50
    }
]
a) The function returns
1.50
Example Solution #2::
1) Assume the input is
[
    {
        "product" to "Milk",
        "quantity" to 3,
        "price" to 1.50
    },
    {
        "product" to "Meat",
        "quantity" to 3,
        "price" to 2.50
    }
]
a) The function returns
12.0
Example Solution #3::
1) Assume the input is
[ ]
a) The function returns
0.0
Notes::
The map must have the keys product, quantity, and price
"""
from typing import Any

def groceries(supermarket : list[dict[str, Any]]) -> float:

    if len(supermarket) == 0:
        return 0.0

    #total = 0.0
    overall_total = 0.0

    for grocery in supermarket:
        total = grocery["quantity"] * grocery["price"]
        overall_total += total

    return  overall_total


if __name__ == "__main__":

    print(groceries([
    {
        "product" : "Milk",
        "quantity" : 3,
        "price" : 1.50
    },
    {
        "product" : "Meat",
        "quantity" : 3,
        "price" : 2.50
    }
    ]))

