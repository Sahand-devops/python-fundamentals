"""
Exercise: Countdown Loop

Description:
Demonstrates a countdown implemented with a while loop.
"""

from time import sleep


def show_soome_looping():
    the_number: int = 10
    while the_number > 1:
        print(f"not yet...{the_number}")
        sleep(1)
        the_number -= 1
        print("Happy New Year")


show_soome_looping()

