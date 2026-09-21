"""
You are given a map called hardDrive in which the keys represent file names and the values represent the size in megabytes of each file.

Determine how much space in megabytes non-programming files occupy.

Save your result in a variable called result

Example Solution
A file that has one of the following extensions is considered a programming file:

kt
py
yml
json
java
Assume that
hardDrive is
{
    "cv.pdf" to 5.5,
    "screen.png" to 1.0,
    "app.py" to 3.4
}
Then
result is 6.5
"""

from to_do import TODO


def guide12(hard_drive: dict[str, float]) -> float:

    result = 0.0
    extensions = ["kt","py","yml","json","java"]
    for file,space in hard_drive.items():
        name, extension = file.split(".")
        if extension not in extensions:
            result += space

    return result

if __name__ == "__main__":

    # hardDrive =  {"cv.pdf":5.5,"screen.png":1.0,"app.py":3.4}
    print(guide12(hard_drive =  {"cv.pdf":5.5,"screen.png":1.0,"app.py":3.4}))
