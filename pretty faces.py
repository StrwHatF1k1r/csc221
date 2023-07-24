from gasp import *

def draw_face(x, y):
    Circle((x, y), 40)
    Circle((x-15, y+10), 5)
    Circle((x+15, y+10), 5)
    Line((x, y+10), (x-10, y-10))
    Line((x-10, y-10), (x+10, y-10))
    Arc((x, y-20), 15, -180, 10)

def draw_smiley_faces():
    x = 50  
    y = 50
    spacing = 100 

    begin_graphics()
    while y < 650:  
        draw_face(x, y)
        x += spacing  

        if x >= 650:  
            x = 50
            y += spacing

    update_when('key_pressed')
    end_graphics()

draw_smiley_faces()
