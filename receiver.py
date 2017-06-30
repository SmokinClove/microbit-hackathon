# The receiver code
from microbit import *
import radio

while True:
    radio.on()
    if radio.receive('Borrow'):
        display('Received')
    
