"""
You are given the variable temperature. It is a String representing a
temperature in formats such as: 15C or 60F.

Convert the given temperature to the opposite unit.

Save your result in a variable result.

Example Solution #1
Assume that
temperature is -30C
Then
result is -22F
Example Solution #2
Assume that
temperature is 50f
Then
result is 10C
Conversion Formulas:
Celsius → Fahrenheit: °F = (°C × 9/5) + 32
Fahrenheit → Celsius: °C = (°F − 32) × 5/9
Notes
Your code must work when temperature is a positive or negative value.
The unit in result must be in uppercase.
The unit in temperature can be given in uppercase or lowercase. Your code
must handle both.
The unit in temperature will always be either Celsius or Fahrenheit.
Provide your solution without decimals
Do not use floor division
"""

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
