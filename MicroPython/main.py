"""
Gavin Gallant
Created on: nov 2024
This program moves led in a circle
"""
from microbit import *

# Initial setup
sleep(500)
display.clear()
display.show(Image.HAPPY)

def move_led_in_square():
    display.clear()
    sprite_x = 0
    sprite_y = 0

    loop_counter_box = 0
    while loop_counter_box < 4:  # Loop for each side of the square
        loop_counter_side = 0
        while loop_counter_side < 5:  # Loop for moving along a side
            display.set_pixel(sprite_x, sprite_y, 9)  # Turn on LED
            sleep(500)
            display.set_pixel(sprite_x, sprite_y, 0)  # Turn off LED

            # Move the sprite in the current direction
            if loop_counter_box == 0:  # Move right
                sprite_x += 1
            elif loop_counter_box == 1:  # Move down
                sprite_y += 1
            elif loop_counter_box == 2:  # Move left
                sprite_x -= 1
            elif loop_counter_box == 3:  # Move up
                sprite_y -= 1

            loop_counter_side += 1
        loop_counter_box += 1

    display.show(Image.HAPPY)  # Show happy face after the loop

# Event loop
while True:
    if button_a.was_pressed():
        move_led_in_square()
