"""
You are given a variable called scandinavia, which represents a collection
of countries with their details.

Determine the total population in Scandinavia based on the provided data
and save your result in a variable called result

Raise an Assertion exception in case one or more countries in the collection
do not belong to Scandinavia.

The Scandinavian countries are the following:

Denmark
Norway
Sweden
Finland
Iceland
Faroe Islands
Greenland
Åland
Example Solution 1
Assume that
scandinavia is
{
    "Sweden" to {
        "population" to 10.42,
        "capital" to "Stockholm"
    },
    "Norway" to {
        "population" to 5.4,
        "capital" to "Oslo"
    },
    "Finland" to {
        "population" to 5.5,
        "capital" to "Helsinki"
    },
}
Then
result is 21.32
Example Solution 2
Assume that
scandinavia is
{
    "Sweden" to {
        "population" to 10.42,
        "capital" to "Stockholm"
    },
    "Norway" to {
        "population" to 5.4,
        "capital" to "Oslo"
    },
    "Panama" to {
        "population" to 4.3,
        "capital" to "Panama"
    },
}
Then
An Assertion exception is raised
Notes
Assume the key population will always be present in the collection scandinavia
"""
from typing import Any

from to_do import TODO


def guide6(scandinavia: dict[str, dict[str, Any]]) -> float:


    scandinavia_countries = ["denmark","norway","sweden","finland","iceland","faroe Islands","greenland","åland"]

    # Get the List of countries in the collection are from sc
    countries = scandinavia.keys()

    # Validate that all countries in the collection are from sc
    for country in countries:
        assert country.lower() in scandinavia_countries

    # Loop over each country and retrieve the total population
    result = 0.0
    for country,details in scandinavia.items():
        population = details["population"]
        result += population # Inline : result += details["population"]

    return result
    # Solution 2:
    """
    result = 0.0
    scandinavia = ["denmark", "norway", "sweden", "finland", "iceland", "faroe Islands", "greenland", "åland"]

    # Get the List of countries in the collection are from sc
    countries = scandinavia.keys()
    
    result = 0.0
    for country, details in scandinavia.items():
        # Validate that all countries in the collection are from sc
        assert country.lower() in scandinavia_countries
        result += details[population]  
    """


if __name__ == "__main__":

    print(guide6(
    {
    "Sweden" : {"population" : 10.42,"capital": "Stockholm"},
    "Norway" : {"population" : 5.4,"capital": "Oslo"},
    "Finland" : {"population" : 5.5,"capital" : "Helsinki"}
    }
    ))




