#    Quick Start
#    To get started with Telabot, import the library and use its functions as needed. Here's a quick overview of the available functions:
#
#    bot_move(x, y, times, interval)
#    Moves the mouse pointer to the specified (x, y) coordinate multiple times at a specified interval.
#
#    x (int): The x-coordinate of the destination.
#    y (int): The y-coordinate of the destination.
#    times (int): The number of times to move the mouse pointer.
#    interval (float): The time interval (in seconds) between each movement.
#    bot_random(interval, x, y, times)
#    Moves the mouse pointer to random positions within the specified (x, y) boundaries multiple times at a specified interval.
#
#    interval (float): The time interval (in seconds) between each movement.
#    x (int): The maximum x-coordinate (exclusive) for the random movement boundary.
#    y (int): The maximum y-coordinate (exclusive) for the random movement boundary.
#    times (int): The number of times to move the mouse pointer randomly.
#
#
#    click_mouse(button)
#    Simulates a mouse click with the specified button.
#
#    button (str): The button for the mouse click, should be one of 'left', 'right', or 'middle'.
#    get_bot_position(times)
#    Prints the current position of the mouse pointer multiple times.
#
#    times (int): The number of times to print the current mouse position.
#    freeze(time_sec)
#    Freezes the execution of the script for the specified time duration.
#
#    time_sec (float): The time duration (in seconds) to freeze the execution.
#    Example Usage
#    python
#    Copy code

import time
import random
import pyautogui
from telabot import bot_move, bot_random, click_mouse, get_bot_position, freeze

# Move the mouse pointer to (100, 200) three times with an interval of 1 second
bot_move(100, 200, 3, 1)

# Move the mouse pointer randomly within the boundaries (800, 600) five times with an interval of 0.5 seconds
bot_random(0.5, 800, 600, 5)

# Click with the left mouse button
click_mouse('left')

# Get the current position of the mouse pointer five times
get_bot_position(5)

# Freeze the execution for 3 seconds
freeze(3)


#    Global stopFlag
#    The library includes a global variable stopFlag, which acts as a flag to stop loops gracefully in case of a keyboard interrupt (Ctrl+C). This is useful for terminating infinite loops without abruptly stopping the script.
#
#
#    Notes
#    Telabot is designed for automating mouse-related tasks and may not work correctly in certain scenarios (e.g., with elevated permissions or on systems with complex security measures).
#    Please use this library responsibly and avoid actions that may cause harm or violate any terms of service. Always respect the policies of the platforms and applications you interact with.
#
#
#    Conclusion
#    Telabot is a convenient Python library that simplifies mouse control and automation using the pyautogui library. With Telabot, you can easily move the mouse pointer, perform random mouse movements, simulate mouse clicks, and more, making it a valuable tool for various automation tasks. Happy coding!
