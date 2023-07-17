from gasp import *
begin_graphics()
c = Circle((5, 5), 5)

def move_player():
    ball_x = 5
    ball_y = 5
    while ball_x <= 635:
        ball_x = ball_x + 4
        ball_y = ball_y + 3
        move_to(c, (ball_x, ball_y))
        sleep(0.02)

move_player()
    