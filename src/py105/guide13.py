"""
You are given a map called hardDrive in which the keys represent file names and the values represent the size in megabytes of each file.

You are also given a variable called corrupted, which represents a file that is corrupted.

Delete the corrupted file from the hard drive and return the hard drive without the corrupted file.

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


def guide13(hard_drive: dict[str, float], corrupted: str) -> dict[str, float]:
    """
    # solution 1: for loop
    result = {}
    for file,space in hard_drive.items():
        if file != corrupted:
            result[file] = space

    return result

    # solution 2: Dictionary comprehension
    return {file : space for file,space in hard_drive.items() if file != corrupted}
    """
    # solution 3: Delete
    if corrupted in hard_drive:
        del hard_drive[corrupted]

    return hard_drive

if __name__ == "__main__":

    # name = {"cv.pdf":5.5,"screen.png":1.0,"app.py":3.4}, corrupted = ""screen.png"
    print(guide13(hard_drive = {"cv.pdf":5.5,"screen.png":1.0,"app.py":3.4},
                  corrupted = "screen.png"))
