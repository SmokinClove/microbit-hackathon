from microbit import *
import radio
balance = 1000
send_amt = 5
place_values = [0,0,0,0]
current_place = 0
ROW_WIDTH = 5

def convert():
    global place_values
    global balance
    place_values[0] = balance // 1000
    place_values[1] = (balance % 1000) // 100
    place_values[2] = ((balance % 1000) % 100) // 10
    place_values[3] = balance % 10

def show_balance():
    convert()
    image = display_first_row(current_place) + display_rest(place_values)
    display.show(Image(image))
def start():
    convert()
    radio.config(channel=28)
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

def display_first_row(current_place):
    str = ''
    global ROW_WIDTH
    for i in range(ROW_WIDTH):
        if i == current_place:
            str = str + '9'
        else:
            str = str + '0'
    str = str + ':'
    return(str)
    
def display_rest(values):
    str = ''
    for i in range(4):
        str = str + numbers[values[i]]
        str = str + ':'
    str = str[:-1] # remove the last colon from the string
    return(str)

image = display_first_row(current_place) + display_rest(place_values)
display.show(Image(image))

start()
image = display_first_row(current_place) + display_rest(place_values)
display.show(Image(image))
while True:
    received = radio.receive()
    if received is not None:
        balance = balance + int(received)
        show_balance()
        sleep(1000)
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send(str(send_amt))
        balance = balance - send_amt
        show_balance()
        sleep(1000)     
    elif button_a.is_pressed():
        press_A()
        print(place_values, current_place)
        image = display_first_row(current_place) + display_rest(place_values)
        display.show(Image(image))
        sleep(500)
    elif button_b.is_pressed():
        press_B()
        print(place_values, current_place)
        image = display_first_row(current_place) + display_rest(place_values)
        display.show(Image(image))
        sleep(500)
    else:
        pass
