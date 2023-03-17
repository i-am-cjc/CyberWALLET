import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import time

# Set up the keyboard and mouse objects
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
mouse = Mouse(usb_hid.devices)

# Read the list of commands from a text file
with open('JIGGLE.cy', 'r') as file:
    commands = file.read().splitlines()

# Initialize the program counter to zero
program_counter = 0

# Iterate through each command in the list
while program_counter < len(commands):
    command = commands[program_counter]
    if command.startswith('TYPE'):
        # Extract the text to type from the command and type it using the keyboard
        text = command[5:]
        keyboard_layout.write(text)
    elif command.startswith('SLEEP'):
        # Extract the sleep duration from the command and sleep for that amount of time
        duration = float(command[6:])
        time.sleep(duration)
    elif command == 'RETURN':
        # Press the return key using the keyboard
        keyboard.send(Keycode.ENTER)
    elif command == 'MOD4':
        # Press the windows key using the keyboard
        keyboard.press(Keycode.WINDOWS)
        keyboard.release(Keycode.WINDOWS)
    elif command.startswith('MOUSE'):
        # Extract the X and Y coordinates from the command and move the mouse cursor to that position
        x, y = command[6:].split(',')
        mouse.move(int(x), int(y))
    elif command.startswith('JUMP'):
        # Extract the line number to jump to from the command and update the program counter
        line_number = int(command[5:])
        program_counter = line_number
        continue
    elif command.startswith('REM'):
        # Do nothing for a comment
        pass

    # Increment the program counter
    program_counter += 1
