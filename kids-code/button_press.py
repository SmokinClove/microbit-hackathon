place_values = [0,0,0]
current_place = 0 

def press_A():
    global current_place
    current_place = current_place + 1
    if current_place > 2:
        current_place = 0 
        
def press_B(): 
    global place_values
    place_values[current_place] = place_values[current_place] + 1
    if place_values[current_place] > 9:
        place_values[current_place] = 0
