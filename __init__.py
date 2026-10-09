"""
Segmented range which is represented in a list of sorted interleaving range.

A range set can be thought as: `[[1, 2], [5, 7]]`.

"""

from .rangeset import (
    IntIncRange,
    IntIncRangeSet,
    Range,
    RangeDict,
    RangeException,
    RangeSet,
    ValueRange,
    intersect,
    substract,
    substract_range,
    subtract,
    subtract_range,
    union,
)

__all__ = [
    "IntIncRange",
    "IntIncRangeSet",
    "Range",
    "RangeDict",
    "RangeException",
    "RangeSet",
    "ValueRange",
    "intersect",
    "substract",
    "substract_range",
    "subtract",
    "subtract_range",
    "union",
]


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3rangeset")
