#!/usr/bin/env python3
""" Annotation Exercice """
from typing import Any, Mapping, Union


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[Any, None] = None
) -> Union[Any, None]:
    """" The function to annotate """
    if key in dct:
        return dct[key]
    else:
        return default
