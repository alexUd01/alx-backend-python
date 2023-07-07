#!/usr/bin/env python3
"""A module that contains a type-annotated function `floor` which
takes a float `n` as argument and returns the floor of the float.
"""
from math import floor as flr


def floor(n: float) -> int:
    """ The function """
    return flr(n)
