from to_do import TODO


def task13(assessments: str) -> str:

    result = assessments [0:3]
    # assessments [-5:-2]
    return result

if __name__ == "__main__":

    #assessments = LMHFFLM
    print(task13(assessments="LMHFFLM"))
    print(task13(assessments="LMFHM"))


