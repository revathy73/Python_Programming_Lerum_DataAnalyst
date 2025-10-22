from to_do import TODO


def task12(assessments: str) -> str:

    result = assessments[len(assessments)//2]
    return result


if __name__ =="__main__":

    # assessments = PHONE
    print(task12(assessments = "PHONE"))
