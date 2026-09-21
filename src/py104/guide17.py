"""
You are given the variable called items, which represents a collection of files. Create a collection that only contains the programming files.

Save your result in a variable called result

Example Solution
A file that has one of the following extensions is considered a programming file:

kt
py
yml
json
java
Assume that
items is
[
    "cv.pdf",
    "screenshot.png",
    "app.py",
    "main.kt",
    "thesis.pptx"
]
Then
result is
["app.py", "main.kt"]
"""

from to_do import TODO


def guide17(items: tuple[str]) -> list[str]:
    """
     # solution 1: for loop
    result = []
    programming_extension = ["kt","py","yml","json","java"]
    for file in items:
        name, extensions = file.split(".")
        if extensions in programming_extension:
            result.append(file)

    return result

    # solution 1: list comprehension
    programming_extension = ["kt", "py", "yml", "json", "java"]
    result = [file for file in items if file.split(".")[1] in programming_extension]
    return result

    # solution 1: list comprehension(refactoring)
    programming_extension = ["kt", "py", "yml", "json", "java"]
    return [file for file in items if file.split(".")[1] in programming_extension]

    # solution 3: filter a list
    programming_extension = ["kt", "py", "yml", "json", "java"]
    result = filter(lambda file: file.split(".")[1] in programming_extension, items)
    return list(result)
    """

    # solution 3: Transform a list(refactoring)
    programming_extension = ["kt", "py", "yml", "json", "java"]
    return list(filter(lambda file: file.split(".")[1] in programming_extension, items))


if __name__ == "__main__":

    # items = ("cv.pdf","screenshot.png","app.py","main.kt","thesis.pptx")
    print(guide17(items = ["cv.pdf","screenshot.png","app.py","main.kt","thesis.pptx"]))
