"""

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