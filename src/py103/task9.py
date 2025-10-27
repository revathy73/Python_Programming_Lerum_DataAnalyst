from to_do import TODO


def task9(temperature: str) -> str:

    temp_scale = temperature[-1].upper()
    temp = int(temperature[:-1])
    if temp_scale == "F":
        c = (temp - 32) * 5 / 9
        return f"{int(c)}C"
    elif temp_scale == "C":
        f = (temp * 9 / 5) + 32
        return f"{int(f)}F"
    else:
        return "Temperature must end with C or F"

if __name__ == "__main__":

    # temperature = 15C
    print(task9(temperature = "15C"))

    # temperature = 60F
    print(task9(temperature="150f"))
