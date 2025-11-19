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




