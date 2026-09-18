"""
You are given a map called universities in which no key and no value is
repeated.

The keys of the map represent university names, and the values are the
countries where those universities are located.

Swap the keys for the values so that the country becomes the key and the
university name becomes the value.

Save your result in a variable called result

Example Solution
Assume that
universities is
{
    "UTP" to "Panama",
    "KTH" to "Sweden",
    "MIT" to "USA"
}
Then
result is
{
    "Panama" to "UTP",
    "Sweden" to "KTH",
    "USA" to "MIT"
}
"""
from to_do import TODO


def guide5(universities: dict[str, str]) -> dict[str, str]:

    """
    # solution : For loop
    result = {}

    for university,country in universities.items():
        result[country] = university

    return result
    """
    # solution : Dictionary comprehension
    result = {country : university for university, country in universities.items()}
    return  result


if __name__ == "__main__":

    # {"UTP" to "Panama","KTH" to "Sweden","MIT" to "USA"} --> {"Panama" : "UTP","Sweden" : "KTH","USA" :"MIT"}
    print(guide5({"UTP":"Panama","KTH":"Sweden","MIT":"USA"}))

    print(guide5({"a":"A", "b":"B", "c":"C"}))