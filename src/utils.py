from typing import Union
from math import modf


def trunc(x: Union[int, float], numbers=3):
    frac, p = modf(x)
    prec = numbers - len(str(int(abs(p))))
    if p == 0:
        while abs(frac) < 1:
            frac *= 10
            prec += 1
    if prec<0:
        x = int(x)
    return round(x, prec)


def group(lst, n):
    """ Группировка элементов последовательности по count элементов """
    return [lst[i:i + n] for i in range(0, len(lst), n)]
