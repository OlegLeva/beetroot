from typing import Optional, Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 1
    if exp < 0:
        raise ValueError('This function works only with exp > 0.')
    return x * to_power(x, exp - 1)


print(to_power(2, 3))
#print(to_power(2, -5))

def sum_of_digits(digit_string: str) -> int:
    if digit_string > 9:
        return digit_string % 10 + sum_of_digits(digit_string//10)
    else:
        return int(digit_string)

print(sum_of_digits(123456789))




