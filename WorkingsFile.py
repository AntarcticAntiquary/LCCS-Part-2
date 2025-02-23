# Author='Daniel Lewis'
# Telos='Homework'
# Topic='Pygame'
# Identifier='Midterm Work'
# Date=23-02-25

import pygame as p

p.init() # Set up screen and game
screen=p.display.set_mode((400,400))
ticker=p.time.Clock()
running=True
dt=0

position=p.Vector2(200,200)

BLACK=(0,0,0) # Initialise colours
WHITE=(255,255,255)
RED=(255,0,0)

while running:
    
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
    
    screen.fill(BLACK)
    
    p.draw.circle(screen,RED,position,15)
    
    keys=p.key.get_pressed()
    if keys[p.K_w]:
        position.y-=50*dt
    if keys[p.K_s]:
        position.y+=50*dt
    if keys[p.K_a]:
        position.x-=50*dt
    if keys[p.K_d]:
        position.x+=50*dt
            
    p.display.flip() # Load changes to screen

    dt=ticker.tick(30)/1000 # 1 tick per 10 seconds (slow is easier to debug)
    
p.quit()