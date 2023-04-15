import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse
import time

import board
import digitalio

import displayio
import terminalio
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

import os

displayio.release_displays()

i2c = busio.I2C(scl=board.GP27, sda=board.GP26)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context


splash = displayio.Group()
display.show(splash)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False


left_button = digitalio.DigitalInOut(board.GP12)
left_button.switch_to_input(pull=digitalio.Pull.DOWN)

right_button = digitalio.DigitalInOut(board.GP13)
right_button.switch_to_input(pull=digitalio.Pull.DOWN)

# Set up the keyboard and mouse objects
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
mouse = Mouse(usb_hid.devices)



# Initialize the program counter to zero
program_counter = 0

# 0 = MENU, 1 = RUNNING
STATE = 0
FILENAME = ""

DELAY = 0.1

VARS = {}

while True:
    VARS = {}
    if STATE == 0:
        files = []
        for f in os.listdir("./scripts"):
            if f.endswith('.cy'):
                files.append(f)
        files.sort()
        index = 0
        FILENAME = files[index]
        
        while STATE == 0:
            splash = displayio.Group()
            
            text_area_top = label.Label(
                terminalio.FONT, text=FILENAME[:-3], color=0xFFFFFF, x=4, y=HEIGHT // 2 - 1
            )
            splash.append(text_area_top)
            
            display.show(splash)
            display.refresh()
            if (right_button.value):
                STATE = 1
            elif (left_button.value):
                index += 1
                if index >= len(files):
                    index = 0
                FILENAME = files[index]
                    
            time.sleep(0.1)
    elif STATE == 1:
        # Read the list of commands from a text file
        with open("./scripts/" + FILENAME, 'r') as file:
            commands = file.read().splitlines()
        top_text = ""

        program_counter = 0
        while program_counter < len(commands):
            command = commands[program_counter]
            splash = displayio.Group()
            
            # Make the display context
            text_area = label.Label(
                terminalio.FONT, text=str(program_counter) + " " + command, color=0xFFFFFF, x=4, y=HEIGHT-6
            )
            splash.append(text_area)
            
            text_area_top = label.Label(
                terminalio.FONT, text=top_text, color=0xFFFFFF, x=4, y=4
            )
            splash.append(text_area_top)
            
            display.show(splash)
            display.refresh()
            if command.startswith('TYPE'):
                # Extract the text to type from the command and type it using the keyboard
                text = command[5:]
                keyboard_layout.write(text)
            elif command.startswith('SLEEP'):
                # Extract the sleep duration from the command and sleep for that amount of time
                duration = float(command[6:])
                time.sleep(duration)
            elif command.startswith("DELAY"):
                DELAY = float(command[6:])
            elif command.startswith("RTYPE"):
                text = command[6:]
                keyboard_layout.write(text)
                time.sleep(0.1)
                keyboard.send(Keycode.ENTER)
            elif command == 'RETURN':
                # Press the return key using the keyboard
                keyboard.send(Keycode.ENTER)
            elif command == "TAB":
                keyboard.send(Keycode.TAB)
            elif command.startswith('MOD4'):
                # Press the windows key using the keyboard
                keyboard.press(Keycode.WINDOWS)
                if len(command) > 4:
                    k = command[5:6]
                    keyboard_layout.write(k)
                keyboard.release(Keycode.WINDOWS)
            elif command.startswith('CTRL'):
                keyboard.press(Keycode.CONTROL)
                if len(command) > 4:
                    k = command[5:6]
                    keyboard_layout.write(k)
                keyboard.release(Keycode.CONTROL)
            elif command.startswith('MOUSE'):
                # Extract the X and Y coordinates from the command and move the mouse cursor to that position
                x, y = command[6:].split(',')
                mouse.move(int(x), int(y))
            elif command.startswith('CLICK'):
                mouse.click(Mouse.LEFT_BUTTON)
            elif command.startswith('JUMP'):
                # Extract the line number to jump to from the command and update the program counter
                jump_target = command[5:]
                target = 0
                for line in commands:
                    if line == "LABEL " + jump_target:
                        program_counter = target
                    target += 1
                continue
            elif command.startswith("SET"):
                var = command[4:]
                VARS[var] = True
            elif command.startswith("UNSET"):
                var = command[6:]
                if var in VARS:
                    del VARS[var]
            elif command.startswith("VJUMP"):
                var, jump_target = command[6:].split(" ")
                if var in VARS:
                    target = 0
                    for line in commands:
                        if line == "LABEL " + jump_target:
                            program_counter = target
                        target += 1
                else:
                    program_counter += 1
                continue
            elif command.startswith("BJUMP"):
                # Jump if left button is pressed, usually proceeded with a SCREEN command
                l = True
                jump_target =command[6:]
                while l == True:
                    if left_button.value:
                        target = 0
                        for line in commands:
                            if line == "LABEL " + jump_target:
                                program_counter = target
                            target += 1
                        l = False
                        continue
                    elif right_button.value:
                        program_counter += 1
                        l = False
                    time.sleep(0.1)
                continue
            elif command.startswith('REM'):
                # Do nothing for a comment
                pass
            elif command.startswith("LED"):
                led.value = not led.value
            elif command.startswith("SCREEN"):
                top_text = command[7:]

            program_counter += 1
            time.sleep(DELAY)
        STATE = 0

