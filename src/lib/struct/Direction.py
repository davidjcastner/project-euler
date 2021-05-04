from __future__ import annotations


class Direction:
    '''integer vector representing a cardinal direction and magnitude,
    cannot have magnitude of zero'''

    def __init__(self, x: int, y: int):
        assert isinstance(x, int) and isinstance(y, int)
        assert x != 0 or y != 0
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Direction(x={self.x}, y={self.y})'

    def scale(self, scalar: int) -> Direction:
        return Direction(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    d = Direction(1, 2)
    print(d)
    print(d.scale(4))
