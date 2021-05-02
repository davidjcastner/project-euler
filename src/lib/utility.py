from typing import Callable
from typing import TypeVar

K = TypeVar('K')
V = TypeVar('V')


def merge_dict(
        overlap: Callable[[V, V], V],
        *args: tuple[dict[K, V]]
) -> dict[K, V]:
    '''combines all the dictionaries and calls the overlap function,
    when multiple dictionaries contain the same key'''
    result = dict()
    for dic in args:
        for key, val in dic.items():
            if key in result:
                result[key] = overlap(result[key], val)
            else:
                result[key] = val
    return result
