"""
You are given a map called classroom in which the keys are student names and
the value is another map with information about the student, such as the
classes they are enrolled in.

The solution to the task is given, but such a solution has a number of errors.
Debug the code so that the correct behavior is produced.

The expected behavior is that each class name shall be modified so that the
letters in the even positions are capitalized and the letters in the odd
positions are lowercase. Additionally, all classes that are null are to be
excluded from the final result.

Assume that
classroom is
{
    "John" to {
        "grade" to 9.3,
        "classes" to [
            "Math",
            "Chemistry",
            null,
            "Programming"
            ]
        },
    "James" to {
        "grade" to 9.3,
        "classes" to [
            "Music",
            "History",
            null,
            null,
            "Albegra"
            ]
        },
    "Jane" to {
        "grade" to 4.1,
        "classes" to [
            null,
            null,
            null
        ]
    },
}
Then
result is
{
    "John" to {
        "grade" to 9.3,
        "classes" to [
            "MaTh",
            "ChEmIsTrY",
            "PrOgAmMiNg"
            ]
        },
    "James" to {
        "grade" to 9.3,
        "classes" to [
            "MuSiC",
            "HiStORy",
            "AlGeBrA"
            ]
        },
    "Jane" to {
        "grade" to 4.1,
        "classes" to []
    },
}
Hint
The inner map will always have a key called classes where you can find the
size of the file.
Assume the map is never empty.
"""
def guide7(
    classroom: dict[str, dict[str : list[str]]]
) -> dict[str, dict[str : list[str]]]:
    for student, details in classroom.items():
        new_classes = []

        for course in details["classes"]:
            if course is None:
                continue

            new_class_name = ""
            for index,letter in enumerate(course):
                if index % 2 == 0:
                    new_class_name += letter.upper()
                else:
                    new_class_name += letter.lower()

            new_classes.append(new_class_name)

        classroom[student]["classes"] = new_classes

    return classroom


if __name__ == "__main__":
    # Tell them to begin by using a simple example instead of a complex one
    data = {
        "John": {"grade": 9.3, "classes": ["Math", "Chemistry", None, "Programming"]},
        "James": {"grade": 9.3, "classes": ["Music", "History", None, None, "Algebra"]},
        "Jane": {"grade": 4.1, "classes": [None, None, None]},
    }

    print(guide7(classroom = data))
