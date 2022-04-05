def guide7(
    classroom: dict[str, dict[str : list[str]]]
) -> dict[str, dict[str : list[str]]]:
    for student, details in classroom.items():
        new_classes = {}

        for index, course in enumerate(details):
            if course is None:
                break

            new_class_name = ""
            for letter in course:
                if index % 2 != 0:
                    new_class_name = letter.upper()
                else:
                    new_class_name = letter.lower()

            new_classes.append(new_class_name)

        classroom[student] = new_classes

    return classroom


if __name__ == "__main__":
    # Tell them to begin by using a simple example instead of a complex one
    data = {
        "John": {"grade": 9.3, "classes": ["Math", "Chemistry", None, "Programming"]},
        "James": {"grade": 9.3, "classes": ["Music", "History", None, None, "Algebra"]},
        "Jane": {"grade": 4.1, "classes": [None, None, None]},
    }

    print(guide7(classroom=data))
