"""
odd/even number checker
Author: Wolf Paulus (https://wolfpaulus.com)
"""


def is_div3(num: int) -> bool:
    """Return True if num is divisible by 3, False otherwise."""
    snumber = str(num)
    sumnum = 0
    for i in snumber:
        sumnum += int(i)

    return sumnum % 3 == 0


def is_div3_str(num: str) -> str:
    """Return a string indicating whether num is odd or even."""
    if num.isnumeric():
        return f"{num} is {'divisible by 3' if is_div3(int(num)) else 'not divisible by 3'}."
    else:
        return "Please enter a number."
