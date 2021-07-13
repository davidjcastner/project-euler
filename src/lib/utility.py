import os
from typing import Callable
from typing import TypeVar
from src.lib.struct.Matrix import Matrix


__data_directory = os.path.join('.', 'src', 'data')

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


def get_data_directory() -> str:
    '''returns the directory of data files'''
    return os.path.abspath(os.path.join('.', 'src', 'data'))


def read_raw_data(filename: str) -> str:
    '''reads the entire data file and returns it as a string'''
    assert isinstance(filename, str)
    filepath = os.path.join(get_data_directory(), filename)
    print(filepath)
    assert os.path.isfile(filepath)
    with open(filepath, 'r') as contents:
        data = contents.read()
    return data


def read_lines(filename: str) -> str:
    '''reads file and returns a list of strings based on new lines,
    strips empty lines'''
    lines = read_raw_data(filename).splitlines()
    return list(filter(lambda s: len(s) > 0, lines))


def read_matrix(filename: str, delimiter: str = ',') -> Matrix:
    '''reads file and returns a matrix based on new lines and delimiter'''
    lines = read_lines(filename)
    data = [[int(n) for n in line.split(delimiter)] for line in lines]
    return Matrix.from_data(data)


def read_delimited_data(filename: str, delimiter: str = ',') -> list[str]:
    '''reads a file containing strings that use a single delimited,
    ignores newlines'''
    data = read_raw_data(filename)
    data = [value.strip() for value in data.split(delimiter)]
    data = [value for value in data if len(value) > 0]
    return data


if __name__ == '__main__':
    print(read_matrix('d_011.txt', delimiter=' '))
