from __future__ import annotations

from typing import Iterable
from typing import Union


class Matrix:
    '''2d list of integers'''

    def __init__(self, rows: int, cols: int) -> None:
        assert rows > 0 and cols > 0
        self.rows = rows
        self.cols = cols
        self.data = [[0 for col in range(cols)] for row in range(rows)]

    def __str__(self) -> str:
        s = [[str(val) for val in row] for row in self.data]
        s = [(', ').join(row) for row in s]
        s = [f'[ {row} ]' for row in s]
        return ('\n').join(s)

    @staticmethod
    def from_data(data: list[list[int]]) -> None:
        rows = len(data)
        cols = len(data[0])
        assert rows > 1
        assert all((len(row) == cols for row in data))
        matrix = Matrix(rows, cols)
        matrix.data = data
        return matrix

    def blank_copy(self) -> Matrix:
        return Matrix(self.rows, self.cols)

    def get(
            self,
            row: Union[int | None] = None,
            col: Union[int | None] = None,
            index: Union[int | None] = None) -> int:
        assert (
            row is not None and col is not None and index is None
        ) or (
            row is None and col is None and index is not None
        )
        use_index = index is not None
        if use_index:
            assert False, 'Not implemented'
        else:
            return self.data[row][col]

    def set(
            self,
            row: Union[int | None] = None,
            col: Union[int | None] = None,
            index: Union[int | None] = None,
            value: int = 0) -> int:
        assert (
            row is not None and col is not None and index is None
        ) or (
            row is None and col is None and index is not None
        )
        use_index = index is not None
        if use_index:
            assert False, 'Not implemented'
        else:
            self.data[row][col] = value

    def each_row_col(self, reverse: bool = False) -> Iterable[tuple[int, int], None, None]:
        for row in range(self.rows):
            for col in range(self.cols):
                if reverse:
                    yield self.rows - 1 - row, self.cols - 1 - col
                else:
                    yield row, col
