"""
Gavin Gallant
Created on: Nov 2024
This program moves an LED in a square pattern.
"""

from microbit import *

# Initial setup
sleep(500)
display.clear()
display.show(Image.HAPPY)

# Function to move the LED in a square pattern
def move_led_in_square():
    display.clear()  # Clear the screen at the start
    sprite_x = 0  # Starting position of the LED
    sprite_y = 0

    # Variable to track which side of the square is being drawn
    current_side = 0

    # Repeat for all four sides of the square
    while current_side < 4:
        step_in_side = 0  # Variable to track steps along one side

        # Move the LED 5 times along the current side
        while step_in_side < 5:
            display.set_pixel(sprite_x, sprite_y, 9)  # Turn on the LED
            sleep(500)  # Wait
            display.set_pixel(sprite_x, sprite_y, 0)  # Turn off the LED

            # Decide the direction to move based on the current side
            if current_side == 0:  # First side: move right
                sprite_x += 1
            elif current_side == 1:  # Second side: move down
                sprite_y += 1
            elif current_side == 2:  # Third side: move left
                sprite_x -= 1
            elif current_side == 3:  # Fourth side: move up
                sprite_y -= 1

            step_in_side += 1  # Move to the next step in the side

        current_side += 1  # Move to the next side of the square

    # Show a happy face after completing the square
    display.show(Image.HAPPY)

# Main loop to wait for button press
while True:
    # Start the LED movement when button A is pressed
    if button_a.was_pressed():
        move_led_in_square()
