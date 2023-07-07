#!/usr/bin/env python3
""" Annotate pre-existing code
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ The function """
    return [(i, len(i)) for i in lst]
