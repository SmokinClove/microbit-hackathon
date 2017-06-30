# The code for the microbit that borrows stuff (eg umbrella)
from microbit import *
import radio

# Set up variables
cost = 10 # Cost to borrow one umbrella
balance = 100 # Current balance
DEBUGGING = True # we will print stuff during development
borrowing = 0 # indicate whether the current holder is borrowing anything

# The logic
while True:
    # Press a to borrow, press b to return
    if button_a.was_pressed():
        radio.on()
        # indicate borrow an umbrella
        # TODO: set up the handshake
        radio.send('Borrow')

        # and deduct account only if balance has enough
        if balance > 0:
            balance = balance - cost
            borrowing = borrowing + 1
        # for us to know we have just sent a notice
        if DEBUGGING:
            display.show('Borrow')
            display.show(str(balance))
        # TODO: unlock umbrella

    if button_b.was_pressed(): # return
        if borrowing > 0:
            balance = balance + cost
            borrowing = borrowing - 1
        if DEBUGGING:
            display.show('Return')
            display.show(str(balance))