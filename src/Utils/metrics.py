
from typing import Callable

import numpy as np


__results__: dict[str, list] = {}


def metrify(func: Callable):
    """Decorator to track function results in a dictionary.

    Args:
        func: The function to be decorated.

    Returns:
        A wrapper function that tracks the results of the decorated function.
    """
    key = func.__qualname__

    def wrapper(*args, **kwargs):
        # Get the function signature as a key

        # Create a new list for the results if it doesn't exist
        if key not in __results__:
            __results__[key] = []

        # Append the result to the list
        result = func(*args, **kwargs)
        __results__[key].append(result)

        return result
    return wrapper


def get_results(funct: str) -> np.ndarray:

    return np.array(__results__[funct])
