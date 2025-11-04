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
