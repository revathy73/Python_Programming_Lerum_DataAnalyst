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


