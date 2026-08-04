"""
Exercise: Rectangle Test

Description:
Simple usage example for the Rectangle class.
"""

from rectangle import Rectangle

my_test_rectangle: Rectangle = Rectangle(123, 321)

print(f"height: {my_test_rectangle.height}")
print(f"width: {my_test_rectangle.width}")

print(f"Area: {my_test_rectangle.area()}")
print(f"Perimiter: {my_test_rectangle.perimiter()}")
print(f"Is it square? {my_test_rectangle.is_square()}")



