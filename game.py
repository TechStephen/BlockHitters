import pygame

""" Variables """

# array of tuples x and y associated w/ individual blocks
pos = []

# boolean is done playing
done = False

# counters
cntr = 0
cntr2 = 0
cntr3 = 0

# player x and y
x = 350
y = 550
lead_x = 0

# ball x and y
bx = 400
by = 420

# block default setter x and y 
blx = 250
bly = 100

""" Methods """

# creates block objects
def createBlocks():
    i = 0
    count = 0
    count2 = 0
    while(i < 90):
        pygame.draw.rect(screen, magenta, [blx + count, bly + count2, 20, 20])
        setBlockPos(blx + count, bly + count2)
        i += 1
        count += 20
        if(count % 300 == 0):
            count = 0
            count2 += 20

# removes block by not having it drawn in loop
def removeBlock():
    print("")
    # checks if ball xy equal to tuple blocks xy

# sets block to an x and y tuple stored in pos
def setBlockPos(x, y):
    pos.append(tuple((x,y)))


""" Screen """

# initializing
pygame.init()

# RGB values for colors were using
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
skyblue = (135,206,235)
magenta = (175, 0, 175)

# screen
screen = pygame.display.set_mode((800, 600))

# caption
pygame.display.set_caption('Block Hitters')

# clock element
clock = pygame.time.Clock()

""" Game Loop """

# run program
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 11 

            if event.key == pygame.K_RIGHT:
                lead_x += 11

    """ Collision Logic """

    # player wall collision
    x += lead_x
    if(x>650):
        x = 650
    elif(x<0):
        x = 0

    # ball to player obj collision
    if((bx - x) <= 145 and (bx - x) >= -20 and by >= y): # hits obj
        cntr = cntr + 1
    elif((bx - x) > 145 and by >= y) or ((bx - x) < 20 and by >= y): # miss so lose
        print("Lose!")
        pygame.quit()

    # ball to wall collision
    if(bx >= 800): # hits right wall
        cntr2 = cntr2 + 1
    elif(bx <= 0): # hits left wall
        cntr2 = 0
    if (by > 600): # hits floor
        print("")
    elif (by < 0): # hits ceiling
        cntr = 0
        cntr3 = cntr3 + 1
    
    # ball to block collision logic
    if(by == bly and bx == blx):
        print("hit")

    """ Ball Movement Logic """

    # ball movement logic
    if(cntr == 0 and cntr2 == 0 and cntr3 == 0): # start goes down
        by += 10
    elif(cntr > 0 and cntr2 == 0): # hits player obj goes up right
        by -= 8
        bx += 8
    elif(cntr > 0 and cntr2 > 0): # hits right wall goes up left
        by -= 8
        bx -= 8
    elif(cntr == 0 and cntr2 > 0): # hits ceiling goes down left
        by += 8
        bx -= 8
    elif(cntr3 > 0 and cntr == 0 and cntr2 == 0): # hits left wall goes down right 
        bx += 10
        by += 10
    elif(cntr3 > 0 and cntr == 0 and cntr2 > 0): # hits player obj goes up right
        bx -= 10
        by += 10
 
    # repopulates screen
    screen.fill(skyblue)
    pygame.draw.rect(screen, red, [bx, by, 10, 10])
    pygame.draw.rect(screen, black, [x, y, 150, 10])
    createBlocks()
    print(str(x) + " " + str(y) + " " + str(bx) + " " + str(by)) # displays coordinates

    # you win/lose display
        # insert code here

    # updates window
    pygame.display.update()

    # clock ticks
    clock.tick(40)

    