#!/usr/bin/env python3

""" Module that contains a type-annotated function (sum_list)
that takes a list (input_list) of floats as arguments
and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Function to return the sum of list of float.
    """
    sum = 0.0

    for num in input_list:
        if isinstance(num, float):  # If type(num) is a float:
            sum += num

    return sum
