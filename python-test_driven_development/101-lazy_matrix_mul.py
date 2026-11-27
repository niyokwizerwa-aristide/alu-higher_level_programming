#!/usr/bin/python3
"""101-lazy_matrix_mul module.

This module provides the function lazy_matrix_mul(m_a, m_b)
that multiplies 2 matrices by using the module NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: first matrix.
        m_b: second matrix.

    Returns:
        The matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
