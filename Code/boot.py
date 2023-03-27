import storage
import board, digitalio
import usb_cdc

# If not pressed, the key will be at +V (due to the pull-up).
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#circuitpy-mass-storage-device-3096583-4

left_button = digitalio.DigitalInOut(board.GP12)
left_button.switch_to_input(pull=digitalio.Pull.DOWN)

# Disable devices only if button is not pressed.
if not left_button.value:
    print(f"boot: button not pressed, disabling drive")
    storage.disable_usb_drive()
    usb_cdc.disable() 
