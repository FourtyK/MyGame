from pygame import *
import pygame
from sys import *
from random import *
init()
# mixer.init()
i = 0
clock = pygame.time.Clock()
condition = False
game = True
delay = 5
playerYSpeed = 0
playerX = 260
playerY = 430
enemyYSpeed = 0
enemyX = 900
enemyY = 430
picFormat = '.dat'
playerHealth = 100
enemyHealth  = 100
# mixer.music.load('music.mp3')
backgroundPNG = 'background'+str(randint(1,1))+picFormat
playerCharPNG = 'player'+picFormat
pausePNG = 'pause'+picFormat
enemyPNG = 'enemy' +picFormat
bulletPNG = 'bullet' +picFormat
gameWindow = display.set_mode([1280,720])
display.set_caption("Stick Kombat")
background = image.load(backgroundPNG)
playerChar = image.load(playerCharPNG)
enemyChar = image.load(enemyPNG)
backgroundwin = image.load('backgroundwin.dat')
bullet = image.load(bulletPNG)
pause = image.load(pausePNG)
# mixer.music.set_volume(0.05)
# mixer.music.play(-1)
display.flip()
bulletLife = 0
timeEnemy = 12
moveRandomResult = 2
randomResult = 0
enemyCurrent = 2
enemyStanding = 1
enemyRunning = 2
enemyJumping = 3

def enemyMovement():
    global enemyYSpeed
    global moveRandomResult
    global randomResult
    global timeEnemy
    global enemyCurrent
    global enemyX
    global enemyY
    if timeEnemy <= 0:
        randomResult = randint(1,100)
        if   1  <= randomResult <= 15:
            enemyCurrent = enemyStanding
        elif 16 <= randomResult <= 45:
            enemyCurrent = enemyRunning
        elif 46 <= randomResult <= 100:
            enemyCurrent = enemyJumping

        if enemyCurrent == enemyStanding:
            moveRandomResult = 0
        if enemyCurrent == enemyRunning:
            moveRandomResult = randint(1,2)
        if enemyCurrent == enemyJumping:
            moveRandomResult = randint(0,4)
        timeEnemy = 12
    if moveRandomResult in [1,3]:
        enemyX -= 7
    elif moveRandomResult in [2,4]:
        enemyX += 7
    enemyYSpeed += 1
    if enemyY >= 430:
        enemyYSpeed = 0
    if enemyCurrent == enemyJumping:
        if enemyY == 430 and enemyYSpeed == 0:
            enemyYSpeed -= 20
    enemyY += enemyYSpeed
    if enemyX > 1180:
        enemyX = 1180
    elif enemyX < 840:
        enemyX = 840
    if enemyY > 430:
        enemyY = 430

def drowing():
    gameWindow.blit(background,[0,0])
    gameWindow.blit(enemyHealthBar,[776,70])
    gameWindow.blit(enemyChar,[enemyX,enemyY])
    gameWindow.blit(playerChar,[playerX,playerY])
    # gameWindow.blit(playerHealthBar,[120,70])
    if bulletLife == 1:
        gameWindow.blit(bullet,[bulletX,bulletY])
    global i
    global clock
    i += 10 * clock.tick() / 1000
    display.update()

while True:
    while game == True:
        timeEnemy -= 1
        # playerHealthPNG = 'health'+str(playerHealth)+picFormat
        enemyHealthPNG  = 'health'+str(enemyHealth)+picFormat
        # playerHealthBar = image.load(playerHealthPNG)
        enemyHealthBar  = image.load(enemyHealthPNG)
        drowing()
        i = 0
        for act in event.get():
            if act.type == QUIT:
                quit()
                exit()
            if act.type == KEYDOWN:
                if act.key == K_ESCAPE:
                    gameWindow.blit(pause,[440,260])
                    display.update()
                    game = False
                if act.key == K_f and bulletLife == 0:
                    bulletX = playerX+50
                    bulletY = playerY+15
                    bulletLife = 1
        keys = key.get_pressed()
        if keys[K_LEFT] or keys[K_a]:
            playerX -= 7
        if keys[K_RIGHT] or keys[K_d]:
            playerX += 7
        if playerX <0:
            playerX = 0
        elif playerX > 540:
            playerX = 540
        playerYSpeed += 1
        if playerY >= 430:
            playerYSpeed = 0
        if keys[K_UP] and playerYSpeed == 0 and playerY == 430:
            playerYSpeed -= 23
        if keys[K_w] and playerYSpeed == 0 and playerY == 430:
            playerYSpeed -= 23        
        playerY += playerYSpeed
        if bulletLife ==1:
            bulletX += 35
            if bulletX > 1280-34:
                bulletLife = 0
            if bulletX+34 >= enemyX and bulletX+17 <= enemyX+100:
                if bulletY >= enemyY+60 and bulletY-12 <= enemyY+150:
                    bulletLife = 0
                    bulletX = playerX+50
                    bulletY = playerY+15
                elif bulletY+12 >= enemyY and bulletY <= enemyY+60:
                    if bulletX+34 >= enemyX+30 and bulletX+17 <= enemyX+80:
                        bulletLife = 0
                        bulletX = playerX+50
                        bulletY = playerY+15
                if bulletLife == 0:
                    enemyHealth -= 5
                    if enemyHealth <= 0:
                        enemyHealth = 0
                        condition = True
                        break

        enemyMovement()
        
        time.delay(delay)
        
    while game == False:
        if condition == True:
            break
        for act in event.get():
            if act.type == QUIT:
                quit()
                exit()
            if act.type == KEYDOWN:
                if act.key == K_ESCAPE:
                    game = True

    if condition == True:
        game = None
        gameWindow.blit(backgroundwin,[0,0])
        display.update()
        for act in event.get():
            if act.type == QUIT:
                quit()
            if act.type == KEYDOWN:
                if act.key == K_ESCAPE:
                    quit()
