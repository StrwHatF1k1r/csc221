from gasp import *          # So that you can draw things
import random
player_x = random.randint(0, 63)
player_y = random.randint(0, 47)
c = Circle((5, 5), 5)

def place_player():
    print("Here I am!")
    

def move_player():
    ball_x = 5
    ball_y = 5
    while ball_x <= 635:
        ball_x = ball_x + 4
        ball_y = ball_y + 3
        move_to(c, (ball_x, ball_y))
        sleep(0.02)

begin_graphics()            # Create a graphics window
finished = False


place_player()

while not finished:
    move_player()

end_graphics()              # Finished!