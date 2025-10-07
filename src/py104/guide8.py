from to_do import TODO


def guide8(items: list[str]) -> list[str]:

    # solution 1: for loop
    result = []
    scandinavia = ["denmark", "norway", "sweden", "finland", "iceland", "faroe islands", "greenland", "åland"]

    for country in items:
        if country.lower() in scandinavia:
            result.append(country)

    return result

if __name__ == "__main__":

    # items = ["Sweden", "Denmark", "Panama","Finland", "Spain"]
    print((guide8(items = ["Sweden", "Denmark", "Panama","Finland", "Spain"])))

    # items = ["Sweden","Denmark"]
    print((guide8(items = ["Sweden","Denmark"])))
