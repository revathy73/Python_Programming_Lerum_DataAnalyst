from to_do import TODO


def guide17(education: dict[str, dict[str, int]]) -> str:

    most_enrolled_class = ""
    most_enrolled_students = 0
    for course, details in education.items():
        no_of_enrolled_students = details["enrolled"]
        if no_of_enrolled_students > most_enrolled_students:
            most_enrolled_class = course
            most_enrolled_students = no_of_enrolled_students

    return most_enrolled_class

if __name__ == "__main__":
    edu = {
            "history":{"enrolled":30,"days":3},
            "programming":{"enrolled":100,"days":5},
            "physics":{"enrolled":80,"days":2}
            }
    print(guide17(education=edu))