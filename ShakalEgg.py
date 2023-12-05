import pygame
import random
import math
from pygame import mixer

# initialise pygame
pygame.init()
pygame.display.set_caption('Shakal egg')
pygame.display.set_icon(pygame.image.load('shakal.png'))

# create screen
backgroundColor = (0,0,0)
(width, height) = (679,600)
screen = pygame.display.set_mode((width,height))
eggBack = pygame.image.load('eggBack.png')
eggBack = pygame.transform.scale(eggBack, (width, height))

# music
mixer.music.load('star.wav')
mixer.music.play(-1)

# shakal
shakalImg = pygame.image.load('shakal.png')
shakalSize = 50
shakalImg = pygame.transform.scale(shakalImg, (shakalSize,shakalSize))
shaX = 375
shaY = 275
def isCollision(px, py, egx, egy):
    distance = math.sqrt(math.pow(px - egx, 2) + math.pow(py - egy,2))
    radius = 25
    if (distance <= radius):
        radius += 5
        return True
    else:
        return False

    
def shakal(x, y, size):
    screen.blit(pygame.transform.scale(shakalImg, (size,size)), (shaX, shaY))
# egg
eggImg = pygame.image.load('egg.png')
eggNum = 10
eggX = []
eggY = []
eggChangeY = []
eggChangeX = []
eggImg = pygame.transform.scale(eggImg, (25, 35))
for i in range(eggNum):
    eggY.append(0)
    eggX.append(random.randint(0, 775))
    eggChangeY.append(random.uniform(1.5, 4.0))
    if eggX[i] <= shaX:
        eggChangeX.append(random.uniform(1.5, 4.0))
    else:
        eggChangeX.append(random.uniform(-4.0, -1.5))
def egg(x,y):
    screen.blit(eggImg, (x, y))
ticks = pygame.time.get_ticks()
# Game loop
running = True
while running:
    screen.fill(backgroundColor)
    screen.blit(eggBack, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # egg movement
    for i in range(eggNum):
        eggY[i] += eggChangeY[i]
        eggX[i] += eggChangeX[i]
        egg(eggX[i], eggY[i])
        if eggY[i] >= height or eggX[i] >= width or eggX[i] <= 0:
            eggY[i] = -12
            eggX[i] = random.randint(0,775)
        # collision
        collision = isCollision(shaX + shakalSize/2, shaY + shakalSize/2, eggX[i], eggY[i])
        if collision:
            shakalSize += 5
            eggY[i] = -12
            eggX[i] = random.randint(0,775)
        
    # player movement
    keys = pygame.key.get_pressed()
    shaY += 5*(keys[pygame.K_DOWN]) - 5*(keys[pygame.K_UP])
    shaX += 5*(keys[pygame.K_RIGHT]) - 5*(keys[pygame.K_LEFT])
    # Boundaries
    shaX = -10*(shaX <= -10) + (width - shakalSize + 10)*(shaX >= width - shakalSize + 10) + shaX*((shaX > -10) and (shaX < width - shakalSize + 10))
    shaY = (shaY <= 0) + (height - shakalSize)*(shaY >= height - shakalSize) + shaY*((shaY > 0) and (shaY < height - shakalSize))
    shakal(shaX, shaY, shakalSize)
    pygame.display.update()