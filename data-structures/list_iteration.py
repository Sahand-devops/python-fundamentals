"""
Exercise: List Iteration

Description:
Demonstrates iterating over a list and printing each item with its index.
"""

animals: list = ["cat", "mouse"]
for animal in animals:
    print(f"{animal} at index {animals.index(animal)}")

