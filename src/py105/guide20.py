"""
You are given a map called hardDrive in which the keys are file names and
the values are another map with information about the file.

Determine the file extension of the file with the smallest size.

Assume that
hardDrive is
{
    "app" to {
        "size" to 9.3,
        "extension" to "py"
    },
    "main" to {
        "size" to 4.1,
        "extension" to "kt"
    },
    "run" to {
        "size" to 2.9,
        "extension" to "pdf"
    },
}
Then
result is pdf
Hint
The inner map will always have a key called size where you can find the size
of the file.
The inner map will always have a key called extension where you can find the
extension of the file.
"""

from typing import Any
import math
from to_do import TODO


def guide20(hard_drive: dict[str, dict[str, Any]]) -> str:

    smallest_extension = ""
    smallest_size = math.inf
    for filename, details  in hard_drive.items():
        size = details["size"]
        extension = details["extension"]

        if size < smallest_size:
            smallest_extension = extension
            smallest_size = size

    return smallest_extension

if __name__ == "__main__":

     harddrive = {"app":{"size":9.3,"extension":"py"},
     "main":{"size":4.1,"extension":"kt"},
     "run":{"size":2.9,"extension":"pdf"}}
     print(guide20(hard_drive = harddrive))


