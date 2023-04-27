""""
Is divisible by 3 checker
Author: Skyler Uhler
"""


def is_div3(num: int) -> bool:
    """Return True if num is divisible by 3, False otherwise."""
    sumnum = 0
    sumnum2 = 0
    for i in str(num):
        sumnum += int(i)

    if len(str(sumnum)) > 1:
        for i in str(sumnum):
            sumnum2 += int(i)

    if sumnum == 3 or sumnum == 6 or sumnum == 9:
        return True
    elif sumnum2 == 3 or sumnum2 == 6 or sumnum2 == 9:
        return True
    else:
        return False


def is_div3_str(num: str) -> str:
    """Return a string indicating whether num is divisible by 3."""
    if num.isnumeric():
        return f"{num} is {'divisible by 3' if is_div3(int(num)) else 'not divisible by 3'}."
    else:
        return f"Please enter a number"
