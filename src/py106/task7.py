"""
You are given the variable sentence. Count the number of letters and digits

Save your result in a variable called result.

Set the count of digits and letters to 0 if sentence is null
result must have the keys letters and digits.
Example Solution #1
Assume that
sentence is H3ll0
Then
result is
{
    "letters" to 3,
    "digits" to 2
}
Example Solution #2
Assume that
sentence is null
Then
result is
{
    "letters" to 0,
    "digits" to 0
}
Notes
Ignore characters that are not letters or digits.
"""
from to_do import TODO


def task7(sentence: str) -> dict[str, int]:


    if sentence is None or sentence == "" :
        return {"letters" : 0, "digits" : 0}

    result = {"letters" : 0, "digits" : 0}
    #result["letters"] = 0
    #result["digits"] = 0
    for char in sentence:
        if char.isalpha():
            result["letters"] = result["letters"] + 1
        elif char.isdigit():
            result["digits"] = result["digits"] + 1

    return result

if __name__ == "__main__":

    # sentence = "H3ll0"
    print(task7(sentence = "H3ll0"))

    # sentence = None
    print(task7(sentence = "None"))
