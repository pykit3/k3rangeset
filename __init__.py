"""
Segmented range which is represented in a list of sorted interleaving range.

A range set can be thought as: `[[1, 2], [5, 7]]`.

"""

from importlib.metadata import version

__version__ = version("k3rangeset")

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
    "union",
]
