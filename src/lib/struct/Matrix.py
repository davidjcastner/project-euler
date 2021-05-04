from __future__ import annotations

from typing import Generator
from typing import Generic
from typing import TypeVar
from src.lib.struct import Direction


T = TypeVar('T')


class Matrix(Generic[T]):
    '''two dimensional matrix of data, cannot be empty'''

    def __init__(self, rows: int, cols: int, default_value: T = 0) -> None:
        assert isinstance(rows, int) and rows > 0
        assert isinstance(cols, int) and cols > 0
        self.__default = default_value
        self.rows = rows
        self.cols = cols
        self.size = rows * cols
        self.data = [default_value for _ in range(self.size)]

    @staticmethod
    def from_data(data: list[list[T]]) -> None:
        '''creates a matrix from an existing two dimensional list'''
        assert isinstance(data, list) and len(data) > 0
        assert isinstance(data[0], list) and len(data[0]) > 0
        rows = len(data)
        cols = len(data[0])
        assert all((len(row) == cols for row in data))
        matrix = Matrix(rows, cols)
        matrix.data = [item for sublist in data for item in sublist]
        return matrix

    def __repr__(self):
        row = f'rows: {self.rows}'
        col = f'cols: {self.cols}'
        data = f'data: {self.data}'
        return f'Matrix({row}, {col}, {data})'

    def blank_copy(self) -> Matrix:
        return Matrix(self.rows, self.cols, self.__default)

    def get_index(self, row: int, col: int) -> int:
        '''returns the index for the row and col in the matrix'''
        assert isinstance(row, int) and row >= 0 and row < self.rows
        assert isinstance(col, int) and col >= 0 and col < self.cols
        return row * self.cols + col

    def get_row_col(self, index: int) -> tuple[int, int]:
        '''returns the (row, col) for the index in the matrix'''
        assert isinstance(index, int) and index >= 0 and index < self.size
        return (index // self.cols, index % self.cols)

    def __iter__(self):
        for val in self.data:
            yield val

    def __getitem__(self, key: int):
        return self.data[key]

    def __setitem__(self, key: int, value: T):
        self.data[key] = value

    def iter_rows_cols(
        self,
        reverse: bool = False
    ) -> Generator[tuple[int, int], None, None]:
        '''generates all (row, col) pairs'''
        assert isinstance(reverse, bool)
        for row in range(self.rows):
            for col in range(self.cols):
                if reverse:
                    yield self.rows - 1 - row, self.cols - 1 - col
                else:
                    yield row, col

    def sub_sequences(
        self,
        direction: Direction,
        length: int
    ) -> Generator[list[T], None, None]:
        '''generates all sub sequences of a length in a direction'''
        assert isinstance(direction, Direction)
        assert isinstance(length, int) and length > 0
        for row, col in self.iter_rows_cols():
            sub_sequence = list()
            is_valid_sequence = True
            for scalar in range(length):
                item_row = row + direction.y * scalar
                if item_row < 0 or item_row >= self.rows:
                    is_valid_sequence = False
                    break
                item_col = col + direction.x * scalar
                if item_col < 0 or item_col >= self.cols:
                    is_valid_sequence = False
                    break
                sub_sequence.append(self[self.get_index(item_row, item_col)])
            if is_valid_sequence:
                yield sub_sequence
