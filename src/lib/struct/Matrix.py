from __future__ import annotations

from typing import Generator
from typing import Generic
from typing import TypeVar


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
        assert isinstance(data, list) and len(data) > 0
        assert isinstance(data[0], list) and len(data[0]) > 0
        rows = len(data)
        cols = len(data[0])
        assert all((len(row) == cols for row in data))
        matrix = Matrix(rows, cols)
        matrix.data = data
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

    def iter_rows_cols(
        self,
        reverse: bool = False
    ) -> Generator[tuple[int, int], None, None]:
        assert isinstance(reverse, bool)
        for row in range(self.rows):
            for col in range(self.cols):
                if reverse:
                    yield self.rows - 1 - row, self.cols - 1 - col
                else:
                    yield row, col

    def sub_sequences(
        self,
        # direction: D,
        length: int
    ) -> Generator[list[T], None, None]:
        pass
