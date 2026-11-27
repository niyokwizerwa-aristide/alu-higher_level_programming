#!/usr/bin/python3
"""100-matrix_mul module.

This module provides the function matrix_mul(m_a, m_b)
that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: list of lists of integers or floats.
        m_b: list of lists of integers or floats.

    Raises:
        TypeError: if m_a or m_b is not a valid matrix.
        ValueError: if m_a or m_b is empty or can't be multiplied.

    Returns:
        The matrix product of m_a and m_b.
    """
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not isinstance(m, list):
            raise TypeError("{} must be a list".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if not all(isinstance(row, list) for row in m):
            raise TypeError("{} must be a list of lists".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        if len(m) == 0 or len(m[0]) == 0:
            raise ValueError("{} can't be empty".format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        for row in m:
            for elem in row:
                if not isinstance(elem, (int, float)):
                    raise TypeError(
                        "{} should contain only integers or floats"
                        .format(name))
    for name, m in (("m_a", m_a), ("m_b", m_b)):
        for row in m:
            if len(row) != len(m[0]):
                raise TypeError(
                    "each row of {} must be of the same size".format(name))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for row in m_a:
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += row[k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
