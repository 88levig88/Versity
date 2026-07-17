print("starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
keyboard.extensions.append(MediaKeys())


# configure pins

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D6, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Configure LEDs

rgb = RGB(
    pixel_pin = board.D10, 
    num_pixels = 12, # number of LEDs
    animation_mode = AnimationModes.RAINBOW
)
keyboard.extensions.append(rgb)


# Configure Rotary Encoder
# Format: ((Pin_A, Pin_B, Click_Pin),)

encoder_handler.pins = ((board.D8, board.D9),)



# Configure Keymap

keyboard.keymap = [
    # Standard Layer
    [
        KC.N1,   KC.N2,   KC.N3,
        KC.N4,   KC.N5,   KC.N6,
        KC.N7,   KC.N8,   KC.N9,
    ]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),)
]


# STarts KMK

if __name__ == '__main__':
    keyboard.go()


# OLED Screen (SSD1306) is wired to I2C pins (SCL/SDA). 
# Display code and Adafruit libraries will be added locally once hardware arrives.
# I'll also change some key functionalities after I have the screen working
