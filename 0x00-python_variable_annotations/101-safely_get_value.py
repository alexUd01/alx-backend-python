#!/usr/bin/env python3
""" Annotation Exercice """
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T', bound=Any)


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """" The function to annotate """
    if key in dct:
        return dct[key]
    else:
        return default
