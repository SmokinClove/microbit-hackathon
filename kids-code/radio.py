from microbit import *
import radio
balance = 1000
send_amt = 0
place_values = [0,0,0,0]
current_place = 0
ROW_WIDTH = 5


def convert_place_values_to_send_amt():
    global place_values
    send_amt = place_values[0] * 1000
    send_amt = place_values[1] * 100 + send_amt
    send_amt = place_values[2] * 10 + send_amt
    send_amt = place_values[3] * 1 + send_amt

# Function convert displays the amount in the wallet on the microbit screen
def convert_balance_to_place_value():
    global place_values
    global balance
    while len(bal_string) < 4:
        bal_string = '0' + bal_string
    place_values[0] = balance[0]
    place_values[1] = balance[1]
    place_values[2] = balance[2]
    place_values[3] = balance[3]

def show_balance():
    # Set the amount displayed on the microbit to the amount I have
    # in the wallet
    convert_balance_to_place_value()
    image = display_first_row(current_place) + display_rest(place_values)
    display.show(Image(image))

def start():
    convert_balance_to_place_value()
    radio.config(channel=28) # Make microbit talk and listen on channel 28
    radio.on()

def press_A():
    global current_place
    current_place = current_place + 1
    if current_place > 3:
        current_place = 0 
        
def press_B(): 
    global place_values
    place_values[current_place] = place_values[current_place] + 1
    if place_values[current_place] > 9:
        place_values[current_place] = 0

numbers = ['00000', '09000', '09900', 
           '09990', '09999', '90000',
           '99000', '99900', '99990',
           '99999'
           ]

# TODO
''' TODO: This algorithm must be run through again '''
def display_first_row(current_place):
    str = ''
    global ROW_WIDTH
    for i in range(ROW_WIDTH):
        if i == current_place:
            str = str + '9'
        else:
            str = str + '0'
    str = str + ':' # Add colon because it's the end of the line
    return(str)
    
def display_rest(values):
    str = ''
    for i in range(4):
        str = str + numbers[values[i]]
        str = str + ':' # Add colon because it's the end of the line
    str = str[:-1] # remove the last colon from the string
    return(str)

start()
image = display_first_row(current_place) + display_rest(place_values)
display.show(Image(image))


while True:
    received = radio.receive()
    if received is not None:
        balance = balance + int(received)
        show_balance()
        sleep(1000)
    else:
        pass # Do nothing if we receive nothing
    # When A and B are pressed, send money
    if button_a.is_pressed() and button_b.is_pressed():
        convert_place_values_to_send_amt();
        if send_amt <= balance:
            radio.send(str(send_amt))
            balance = balance - send_amt
            show_balance()
            sleep(1000)    
        else:
            pass # Do nothing if we try to send more than we have
    elif button_a.is_pressed():
        press_A()
        image = display_first_row(current_place) + display_rest(place_values)
        display.show(Image(image))
        sleep(500)
    elif button_b.is_pressed():
        press_B()
        image = display_first_row(current_place) + display_rest(place_values)
        display.show(Image(image))
        sleep(500)
    else:
        pass
