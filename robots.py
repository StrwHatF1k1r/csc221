from gasp import *
from random import *

def place_player( ):
    global px, py
    px = randint(0,63)
    py = randint(0,47)

    print("Here I am!")

def place_robot():
    global rx,ry, roboshape
    rx = randint(0,63)
    ry = randint(0,47)
    roboshape = Box((10 * rx, 10 * ry), 10, 10, filled=False, color=color.BLACK, thickness=1)

def move_player(px, py):
    key_press = (update_when('key_pressed'))

    while key_press == 'f':
     remove_from_screen(player_shape)
     safely_place()
     key_press = (update_when('key_pressed'))

    if key_press == 'w':
        py += 1

    if key_press == 'q':
        px -= 1
        py += 1

    if key_press == 'e':
        px += 1
        py += 1
        
    elif key_press == 'a':
        px -= 1
        
    
    elif key_press == 's':
        py -= 1
    
    
    elif key_press == 'd':
        px += 1
    
    sleep(.5)
    move_to(player_shape, (10 * px + 5, 10 * py + 5))
    return px, py


def move_robot(rx,ry):
    
    if rx > px and ry > py:
        rx -= 1
        ry -= 1
       
   
    elif rx < px and ry < py:
        rx += 1
        ry += 1
       
   
    elif rx > px and ry < py:
        rx -= 1
        ry += 1
       
    
    elif rx < px and ry > py:
        rx += 1
        ry -= 1
       
   
    elif rx > px and ry == py:
        rx -= 1
        
   
    elif rx < px and ry == py:
        rx += 1
        
   
    elif ry > py and rx == px:
        ry -= 1
        
   
    elif ry < py and rx == px:
        ry += 1
        

    sleep(.5)
    move_to(roboshape, (10 * rx, 10 * ry))
    return rx, ry

def check_collsions():
    if ry == py and rx == px:
        Text("You've been caught!")
        sleep(3)
        return True
    
def collided():
    if ry == py and rx == px:

        return True

def safely_place(): 
    global player_shape
    place_player()
    while collided():
        place_player()
    player_shape = Circle((10 * px + 5, 10 * py + 5), 5, filled=True)

begin_graphics()

place_robot()
safely_place()
while True:
    px, py = move_player(px,py)
    rx, ry = move_robot(rx, ry)
    collided = check_collsions()
    if collided == True:
        break

end_graphics()