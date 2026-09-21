"""
You are given the variable items, which represents a collection of countries.

Remove all the countries that are not Scandinavian countries.

Example Solution
The Scandinavian countries are the following:

Denmark
Norway
Sweden
Finland
Iceland
Faroe Islands
Greenland
Åland
Assume that
items is
[
    "Sweden",
    "Panama",
    "Canada",
    "Denmark",
    "Spain"
]
Then
result is ["Sweden", "Denmark"]
Notes
Your solution cannot be case-sensitive
"""

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
