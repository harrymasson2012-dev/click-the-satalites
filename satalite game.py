import pgzrun

import random

WIDTH=700
HEIGHT=500

TITLE = "connect the satalites"

lines = []
satalites = []
next_satalite = 0

number_of_satalites = 7

for i in range(number_of_satalites):
    satalite = Actor("satalite")

    satalite.x = random.randint(0,WIDTH)
    satalite.y = random.randint(0,HEIGHT)
    satalites.append(satalite)

def draw():
    screen.blit("space",(0,0))
    number = 1
    for satalite in satalites:
        satalite.draw()
        screen.draw.text(str(number),(satalite.pos[0],satalite.pos[1]+18),color="light green")
        number += 1
    for i in lines:
        screen.draw.line(i[0],i[1],color = "white")
    
def on_mouse_down(pos):
    global next_satalite, lines
    if next_satalite<number_of_satalites:
        if satalites[next_satalite].collidepoint(pos):
            if next_satalite:
                lines.append((satalites[next_satalite-1].pos,satalites[next_satalite].pos))
            next_satalite +=1
        else:
            next_satalite = 0
            lines = []






pgzrun.go()
