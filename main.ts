/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Gavin Gallant
 * Created on: nov 2024
 * This program moves led in a circle
*/


// variables
let sprite: game.LedSprite = null
let loopCounterbox = 0
let loopCounterside = 0

// setup
basic.pause(500)
basic.clearScreen()
basic.showIcon(IconNames.Happy)


// when "A" is pressed, the pixels move in a squaire  
input.onButtonPressed(Button.A, function () {
    // setup
    basic.clearScreen()
    loopCounterbox = 0
    loopCounterside = 0
    sprite = game.createSprite(0, 0)
    sprite.set(LedSpriteProperty.X, loopCounterside)
    // loop to move the sprite around
    while (loopCounterbox <= 3) {
        while (loopCounterside <= 5) {
            sprite.move(1)
            loopCounterside++
            basic.pause(500)
        }
        sprite.turn(Direction.Right, 90)
        loopCounterside = 0
        loopCounterbox++
    }
    //reset 
    sprite.delete()
    basic.showIcon(IconNames.Happy)
})