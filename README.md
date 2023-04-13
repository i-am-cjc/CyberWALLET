# CyberWALLET
![Alt text](logo.jpg?raw=true "Title")
Inspired by the USB Rubber Ducky / BadUSB, but in a different formfactor that I might actually carry and use.

## Hardware
The current iteration of the CyberWALLET is a Raspberry Pi Pico, and an SSD1306 0.9inch 128x32 screen. There are two buttons on the front that will be used for menu navigation as well as interaction in scripts.

![Alt text](photo.jpg?raw=true "Title")

Multiple scripts can be loaded and then selected upon boot using the buttons on the device.

## Scripting Language
The CyberWALLET uses a pretty simple scripting language, again inspired mostly by the Hak5 USB Rubber Ducky, but with some other stuff based around the buttons on the front of the device.

* TYPE <string> - Types out the string, but doesn't press enter
* RTYPE <string> - Types out the string and presses enter (ps RType is a great game)
* SLEEP <float> - Sleeps for the float number of seconds
* DELAY <float> - Sets the default sleep time between commands (default: 0.1)
* RETURN - Presses Return
* MOD4 - Presses the MOD4 / Windows key
* MOUSE <co-ords> - Moves the Mouse by x,y
* CLICK - Clicks the left mouse
* SET <variable> - Sets a variable to true
* LABEL <string> - A label in code to jump to
* JUMP <LABEL> - Jumps to a specific label
* VJUMP <variable> <label> - Jumps to label is variable is set, otherwise carries on down the script
* BJUMP <target> - waits for a button press. If the left button is pressed, JUMP to target, otherwise carry on down the script.
* REM <string> - A comment
* SCREEN <string> - Writes the string to the internal screen, great for debugging / amusement.

### Hello World!

Here is an example script that will open up notepad on a windows computer, and write hello world.

```
DELAY 1
MOD4
RTYPE notepad
TYPE Hello World
```

