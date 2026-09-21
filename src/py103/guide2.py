"""
You are given the variable month which represents a month of the year.

Create a solution that returns true when the given month is November and
false for all other months.

Save your result in a variable called result.

Example Solution 1
Assume that
month is December
Then
result is false
Example Solution 2
Assume that
month is November
Then
result is true
Note
Your solution cannot be case sensitive
"""

from to_do import TODO


def guide2(month: str) -> bool:

     if month.upper() == "NOVEMBER":
         result = True
     else:
         result = False

     return result

     # return month.lower() == "november"

     #return month.upper() == "NOVEMBER"



if __name__ == "__main__":

     # month ="December"
     print(guide2(month = "December"))

     # month ="November"
     print(guide2(month = "November"))

     # month ="March"
     print(guide2(month="March"))

     # month ="NOVEMBER"
     print(guide2(month="NOVEMBER"))

     # month ="January"
     print(guide2(month="January"))

     # month ="NoVemBeR"
     print(guide2(month="NoVemBeR"))


