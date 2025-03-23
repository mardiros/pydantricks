"""Type inference."""

from types import UnionType
from typing import Any, Literal, get_origin


def is_literal(typ: type[Any] | UnionType) -> bool:
    """Used to detect unions like Optional[T], Union[T, U] or T | U."""
    type_origin = get_origin(typ)
    if type_origin:
        if type_origin is Literal:
            return True
    return False


def is_union(typ: type[Any] | UnionType) -> bool:
    """Used to detect unions like  T | U."""
    type_origin = get_origin(typ)
    if type_origin:
        if type_origin is UnionType:  # T | U
            return True
    return False
