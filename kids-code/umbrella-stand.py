from microbit import *
import radio

balance = 0
send_amt = 400

while True:
    received = radio.receive() #constantly checks if there's a message
    if received is not None:
        balance = balance + int(received)
        #TODO: Unlock servo
        sleep(1000)
    else:
        pass # Do nothing if we receive nothing
    # When A and B are pressed, return some money back
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(str(send_amt))
        balance = balance - send_amt
        # TODO: Lock servo
        sleep(1000)    
    else:
        pass
