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

