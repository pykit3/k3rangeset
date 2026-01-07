# k3rangeset

[![Action-CI](https://github.com/pykit3/k3rangeset/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3rangeset/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3rangeset/badge/?version=stable)](https://k3rangeset.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3rangeset)](https://pypi.org/project/k3rangeset)

Segmented range represented as sorted interleaving intervals.

A range set can be thought of as: `[[1, 2], [5, 7]]`.

k3rangeset is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3rangeset
```

## Quick Start

```python
import k3rangeset

# Create a RangeSet and perform operations
rs = k3rangeset.RangeSet([[1, 5], [10, 20]])

# Union two range sets
rs2 = k3rangeset.union(rs, [[3, 12]])
print(rs2)  # [[1, 20]]

# Intersection
rs3 = k3rangeset.intersect([[0, 10]], [[5, 15]])
print(rs3)  # [[5, 10]]
```

## API Reference

::: k3rangeset

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
