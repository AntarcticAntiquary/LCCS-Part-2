# Author='Daniel Lewis'
# Telos='Homework'
# Topic='Pygame'
# Identifier='Midterm Work'
# Date=23-02-25

impot pygame as p

p.init() # Set up screen and game
screen=p.display.set_mode((400,400))
ticker=p.time.Clock()
running=True

BLACK=(0,0,0) # Initialise colours
WHITE=(255,255,255)

while running:
    
    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
    
    x=0 # Initial coordinates
    y=0
    
    for i in range(8): # This loop governs a column
        for j in range(4): # This loop governs a row
            p.draw.rect(screen,WHITE,p.Rect(x,y,50,50))
            x+=100 # MOves the squares horizontally
        #print(i,x,y)
        y+=50 # Moves squares vertically
        if i%2==0: # Conditionals govern offset of squares
            x=50
        elif i%2==1:
            x=0
            
    p.display.flip() # Load changes to screen

    ticker.tick(0.1) # 1 tick per 10 seconds (slow is easier to debug)
    
p.quit()