"""
You are given a map called classroom in which the key represents a student’s
first and last name and the value is their final grade.

Determine how many students have a last name that ends with sson.

Example Solution
Assume that
classroom is
{
    "Ann Johannsson" to 10.0,
    "Pat Ericsson" to 9.5,
    "Pat Lark" to 9.0
}
Then
result is 2
"""
from to_do import TODO


def guide7(classroom: dict[str, float]) -> int:

    result = 0
    for name in classroom.keys():
        first, last = name.split(" ")
        if len(last) >= 4 and last[-4:] == "sson":
            result += 1

    return result

if __name__ == "__main__":

    # classroom = {"Ann Johannsson" : 10.0,"Pat Ericsson" : 9.5,"Pat Lark" : 9.0}
    print(guide7(classroom = {"Ann Johannsson" : 10.0,"Pat Ericsson" : 9.5,"Pat Lark" : 9.0}))

    # classroom = {"Ann Johannson" : 10.0,"Pat Ericsson" : 9.5,"Pat Lark" : 9.0}
    print(guide7(classroom={"Ann Johannson": 10.0, "Pat Ericsson": 9.5, "Pat Lark": 9.0}))

