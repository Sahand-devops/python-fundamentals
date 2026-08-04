"""
Exercise: Rectangle

Description:
Demonstrates a simple rectangle class with basic properties and methods.
"""


class Rectangle:
    def _init_(self, height: int, width: int) -> None:
        self._height = height
        self._width = width


def get_height(self) -> int:
    return self._height


def set_height(self, new_height: int) -> None:
    self._height = new_height


def get_width(self) -> int:
    return self._width


def set_width(self, new_width: int) -> None:
    self._width = new_width


# Beräkna arean
def area(self) -> float:
    return self._height * self._width


# Beräkna omkrets
def perimeter(self) -> int:
    return 2 * (self._height + self._width)


# Beräkna om det är en kvadrat
def is_square(self) -> bool:
    return self._height == self._width

