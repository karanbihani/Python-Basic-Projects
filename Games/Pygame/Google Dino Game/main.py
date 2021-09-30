import pygame
import sys
import random as ran

from pygame.constants import K_SPACE, MOUSEBUTTONDOWN, MOUSEMOTION
from pygame.event import event_name
pygame.init()

WIDTH, HEIGHT = 800, 450
FPS = 60

def displayScore():
    global scoreSurface
    tickCounter = (pygame.time.get_ticks()-scoreReseter)//1000
    scoreSurface = scoreFont.render('Score : '+str(tickCounter), False, 'Black')
    scoreRect = scoreSurface.get_rect(center=(400, 100))
    pygame.draw.rect(screen, 'Pink', scoreRect, 10)  # args : surface to draw on, color, rectangle we want to draw
    pygame.draw.rect(screen, 'Pink', scoreRect)
    screen.blit(scoreSurface, scoreRect)
    oldCounter = tickCounter

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Tutorial')

gameActive = 1
scoreReseter = 0

testSurface = pygame.Surface((100, 200))
testSurface.fill((255, 255, 255))

# easier and fater for pygame to work with
skySurface = pygame.image.load('graphics/Sky.png').convert()
groundSurface = pygame.image.load('graphics/ground.png').convert()

# convert_alpha only converts alpha values instead of the white and black outside main part of the image
snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snailRect = snailSurface.get_rect(bottomleft=(600, 300))

playerGravity = 0
playeSurface = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()

# creatign a rectangle, there are different ways to do this
'''
1.playerRect = pygame.rect()#args are left,top,width,height
2. playerRect = 
1. is not used generally as we want soething very close to the size of the image so we use the second method
'''

playerRect = playeSurface.get_rect(midbottom=(80, 300))

scoreFont = pygame.font.Font('font/Pixeltype.ttf', 50)

resetSurface = scoreFont.render('DO you want to restart?',False,'Black')
resetRect = resetSurface.get_rect(center = (WIDTH//2,HEIGHT//2))

'''
testFont = pygame.font.Font('font/Pixeltype.ttf', 50)# args are font type and size
textSurface = testFont.render('The text',False,'Black') #Args are : Text, Anti alisaing, color
'''


def main(snailRect = snailRect, playerRect = playerRect, playerGravity = playerGravity , gameActive = gameActive ):
    global scoreReseter

    clock = pygame.time.Clock()
    run = True
    speed = ran.randint(4,8)
    oldCounter = 0
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            '''
            if event.type == MOUSEBUTTONDOWN:
                if resetRect.collidepoint(event.pos):
                    gameActive = True
            '''
            if event.type == MOUSEBUTTONDOWN:
                if playerRect.collidepoint(event.pos):
                    playerGravity = -20 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerRect.bottom >= 300 and gameActive == True: 
                    if gameActive:
                        playerGravity = -20
                
                elif event.key == pygame.K_SPACE : 
                    gameActive = True

            if event.type == pygame.KEYUP:
                print('Key up')

            #mouse input using event loop
            '''
            if event.type == pygame.MOUSEMOTION:
                if playerRect.collidepoint(event.pos):
                    print('.Collision')
            '''
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse Down')
            if event.type == pygame.MOUSEBUTTONUP:
                print('Mouse Up')
            '''

        if gameActive:

            screen.blit(skySurface, (0, 0))
            screen.blit(groundSurface, (0, 300))
            # screen.blit(testSurface,(0,0))

            '''
            screen.blit(textSurface,(325,50))
            '''
                        # Using pygame.draw
            '''
            pygame.draw.line(screen,'gold',(WIDTH//2,0),(WIDTH//2,HEIGHT),5)
            pygame.draw.line(screen,'gold',(WIDTH//2,0),pygame.mouse.get_pos(),5)

            pygame.draw.ellipse(screen, 'brown', pygame.Rect(WIDTH//2,HEIGHT//2, 100, 100))
            '''

            if snailRect.left < -100:
                snailRect.left = 800
                speed = ran.randint(4,9)

            snailRect.left-=speed

            screen.blit(snailSurface, snailRect)

            displayScore()

            # Getting keyboard input pygame.key

            '''
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                print('Jump')
            '''

            #player
            
            playerGravity += 1
            playerRect.bottom +=playerGravity

            if playerRect.bottom > 300:
                playerRect.bottom = 300
                playerGravity =0

            screen.blit(playeSurface, playerRect)

            # collision checker
            '''
            if playerRect.colliderect(snailRect):# returns 0 or 1 ie true or false
                print('Collided')
            '''

            # collision with mouse
            '''
            mousePOS = pygame.mouse.get_pos()
            mousePOSPressed = pygame.mouse.get_pressed()
            if playerRect.collidepoint((mousePOS)):
                print(mousePOSPressed)
            '''

            if snailRect.colliderect(playerRect):
                snailRect.left = 800
                scoreReseter = pygame.time.get_ticks()
                gameActive = 0
            
        else:
            screen.fill('Yellow')
            pygame.draw.rect(screen,'Pink',resetRect,10)
            pygame.draw.rect(screen,'Pink',resetRect)
            screen.blit(resetSurface,resetRect)
            scoreSurfaceRect2 = scoreSurface.get_rect(center = (400,350))
            screen.blit(scoreSurface,scoreSurfaceRect2)
        pygame.display.update()


main()

# Notes

'''
# For Creating Text
1. Create a font (text size and style)
2. Write text on a surface
3. Blit text surface
'''
# 1.Basic Animation

'''
We are nto drawign a satitic image
if we updated image we would see animation
so keep updating
'''

# 2. Rectangles

'''
1. Precise positioning of surfaces
    We can place surface s based ont heir bottom or top faces instead of left corner
    |->Genrally While placing some thing on the screen we have 2 steps 
        1. Sutrface for imege information  
        2. Placement cia rectangles
            these toether are SPRITES class
2. Basic Colliisions

'''

# 3. Collisions

'''
Very easy with rectangles

SYNTAX:
1. rect1.colliderect(rect2)
2. rect1.collidepoint((x,y)) --> check pts collision
'''

# 4. Mouse Input

'''
Pygane has 2 methods

1. Pygame.mouse
    Guves mouse position, clicks, buttons, visibility etc
2. event loop
    Gives mouse motition, clicks, buttons, visibility etc
    basically the same just 2 different ways to achive it

'''

# 5. Drawing With Rectangles

'''
pygame.draw is very useful for drawign stuff 
we can draw circles, lines, pointes, ellipses
'''

# 6. Colors
'''
There are 2 ways to do this:
1. Prdefined color
2. User defined -This is done in 2 ways:
    1. rgb
    2. hexadecimal

''' 

# 7. Player Charecter
'''
1. Keyboard input
    1. pygame.key
    2. event loop

2. Jump + gravity
3. creating a floor
'''

# 8. Game States

'''
use if statements like

if gameState:
    run game
else:
    end game
'''

# 9. Time in pygame
'''
Done using

pygame.time.get_ticks() --> milli seconds since the game started
'''
