from to_do import TODO


def guide12(hard_drive: dict[str, float]) -> float:

    result = 0.0
    extensions = ["kt","py","yml","json","java"]
    for file,space in hard_drive.items():
        name, extension = file.split(".")
        if extension not in extensions:
            result += space

    return result

if __name__ == "__main__":

    # hardDrive =  {"cv.pdf":5.5,"screen.png":1.0,"app.py":3.4}
    print(guide12(hard_drive =  {"cv.pdf":5.5,"screen.png":1.0,"app.py":3.4}))
