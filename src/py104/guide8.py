from to_do import TODO


def guide8(items: list[str]) -> list[str]:

    # solution 1: for loop
    """
    result = []
    scandinavia = ["denmark", "norway", "sweden", "finland", "iceland", "faroe islands", "greenland", "åland"]

    for country in items:
        if country.lower() in scandinavia:
            result.append(country)

    return result

    # solution 2: list comprehension
    scandinavia = ["denmark", "norway", "sweden", "finland", "iceland", "faroe islands", "greenland", "åland"]
    return [country for country in items if country.lower() in scandinavia]

    # solution 3:
    scandinavia = ["denmark", "norway", "sweden", "finland", "iceland", "faroe islands", "greenland", "åland"]
    filtered_list = filter(lambda country: country.lower() in scandinavia, items)
    return list(filtered_list)
    """

    # solution 4: Refactoring in filter
    scandinavia = ["denmark", "norway", "sweden", "finland", "iceland", "faroe islands", "greenland", "åland"]
    return list(filter(lambda country: country.lower() in scandinavia, items))


if __name__ == "__main__":

    # items = ["Sweden", "Denmark", "Panama","Finland", "Spain"]
    print((guide8(items = ["Sweden", "Denmark", "Panama","Finland", "Spain"])))

    # items = ["Sweden","Denmark"]
    print((guide8(items = ["Sweden","Denmark"])))
