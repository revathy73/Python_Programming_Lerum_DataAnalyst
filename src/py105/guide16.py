from to_do import TODO


def guide16(hard_drive: dict[str, float]) -> dict[str, float]:
    """ Update method
    #result = {}
    for filenames,megabytes in hard_drive.items():
        gigabytes = megabytes * 0.0009765625
        hard_drive.update({filenames:gigabytes})

    return hard_drive

    # solution 2:
    result = {}
    for filenames, megabytes in hard_drive.items():
        gigabytes = megabytes * 0.0009765625
        result[filenames] = gigabytes # hard_drive[filenames] = gigabytes

    return result

    # Dictionary comprehension:
    result = {filenames : megabytes * 0.0009765625 for filenames, megabytes in hard_drive.items()}
    return  result
    """
    # Transform method:
    return dict(map(lambda item: (item[0], item[1] * 0.0009765625) ,hard_drive.items() ))

if __name__ == "__main__":

    # hardDrive = {"cv.pdf": 5.5,"screen.png" :1.0,"app.py":3.4}
    print(guide16(hard_drive = {"cv.pdf": 5.5,"screen.png" :1.0,"app.py":3.4}))


