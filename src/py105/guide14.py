"""
You are given a map called hardDrive in which the keys represent file names
and the values represent the size in megabytes of each file.

You are also given a variable called corrupted, which represents a file that
is corrupted.

Delete the corrupted file from the hard drive and return the hard drive without
the corrupted file.

Assume that
corrupted is screen.png
hardDrive is
{
    "cv.pdf" to 5.5,
    "screen.png" to 1.0,
    "app.py" to 3.4
}
Then
result is
{
    "cv.pdf" to 5.5,
    "app.py" to 3.4
}
Notes
Your solution must be case-sensitive.
"""

from to_do import TODO


def guide14(scandinavia: dict[str, str]) -> dict[str, str]:

    scand_countries = ["denmark", "norway", "sweden", "finland", "iceland",
                       "faroe Islands", "greenland", "åland"]

    result = {}
    for country,language in scandinavia.items():
        if country.lower() in scand_countries:
            result[country] = language

    return result

if __name__ == "__main__":

    # scandinavia = {"Sweden":"sv","Norway":"no","Panama":"es"}
    print(guide14(scandinavia = {"Sweden":"sv","Norway":"no","Panama":"es"}))
