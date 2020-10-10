import pygame
from pygame.display import set_icon
# from Player import Player
from Npcs import Npc
from Bullet import Bullet
import math
import random
import sys

pygame.init()

screen = pygame.display.set_mode((1000,600))

background = pygame.image.load('background.jpg')

## Set icons for games ##
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
set_icon(icon)

''' set player options '''
player_img = pygame.image.load('spaceship.png')
playerX = 500 # x position
playerY = 500 # y position
player1 = Npc(playerImg=player_img)
player_valx = 0
player_valy = 0

enemy_img = pygame.image.load('ufo.png')
enemy = Npc(playerImg = enemy_img)
enemyX = 500
enemyY = 50
enemy_valx = 0.3
enemy_valy = 30

bullet_img = pygame.image.load('bullet.png')
bullet = Bullet(Img = bullet_img)
# bullet2  = Bullet(Img= bullet_img)
bulletX = 500
bulletY = 500
bullet_valx = 0
bullet_valy = 0.2

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
## Game play ##
conn = True
# ready = True
score = 0
while conn and score < 10:

    screen.fill((0,0,0))

    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            conn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_valx = -0.4  
            if event.key == pygame.K_RIGHT:
                player_valx = 0.4
            if event.key == pygame.K_SPACE:
                if bullet.bullet_state == False:
                    bulletX = playerX
                    bullet.fire(screen,x = bulletX,y = bulletY)
                else:
                    pass
                
    playerX += player_valx
    enemyX += enemy_valx
    # playerY += player_valy
    if playerX <= 0:
        playerX = 0
     
    elif playerX >= 964:
        playerX = 964
    
    if enemyX <= 0:
        enemyX = 0
        enemy_valx = 0.3
        enemyY += enemy_valy

    elif enemyX >= 964:
        enemyX = 964
        enemy_valx = -0.3
        enemyY += enemy_valy
    if enemyY >=400:
        print("You has lost the game")
        sys.exit()
    
    if bulletY <= 0:
        bulletY = 500
        bullet.bullet_state = False

    if bullet.bullet_state:
        bullet.display(screen,x = bulletX, y = bulletY)
        bulletY -=1

    ## collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 500
        bullet.bullet_state = False
        score += 1
        print(f"Score {score}")
        enemyX = random.randint(0,900)
        enemyY = random.randint(50,150)


    player1.play(screen=screen, x = playerX, y = playerY)
    enemy.play(screen=screen , x = enemyX, y = enemyY)
    # bullet.play(screen=screen , x = bulletX , y = bulletY)
    pygame.display.update() 

print("congratulation !!! You have won the game")