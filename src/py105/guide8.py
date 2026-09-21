"""
You are given a map called hardDrive in which the keys represent file names
and the values represent the size in megabytes of each file.

Determine how many files are programming-related. Save your result in a
variable called result

Example Solution::
A file that has one of the following extensions is considered a programming
file:

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
result is 1
"""
from to_do import TODO


def guide8(hard_drive: dict[str, float]) -> int:

    result = 0
    
    pgm_extensions = ["kt","py","yml","json","java"]
    for file in hard_drive.keys():
        programme, extension = file.split(".")
        if extension in pgm_extensions:
            result += 1

    return result

if __name__ == "__main__":

    # hardDrive = {"cv.pdf" : 5.5,"screen.png" : 1.0, "app.py" : 3.4}
    print(guide8(hard_drive = {"cv.pdf":5.5,"screen.png":1.0, "app.py":3.4}))