import pygame
import random

# intialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))



# backround
backround = pygame.image.load("backround1.png")

# title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# laser bullet
laser_img = pygame.image.load("laser.png")
laser_x = 0
laser_y = 480
laser_x_change = 0
laser_y_change = 10
laser_state = "ready"

def fire_laser(x,y):
    global laser_state
    laser_state = "fire"
    screen.blit(laser_img, (x + 16, y + 10))

# Enemy
enemy_img = pygame.image.load("monster.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 3
enemy_y_change = 30

def enemy(x, y):
    screen.blit(enemy_img, (x, y))


# Player
player_img = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0

def player(x, y):
    screen.blit(player_img, (x, y))

# game loop
running = True
while running:
    
    # RGB - Red, Green, Blue
    screen.fill((39, 45,  87))
    # backround
    screen.blit(backround, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if laser_state == "ready":
                    laser_x = player_x
                    fire_laser(laser_x, laser_y)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    #player movement
    player_x += player_x_change
    
    # boarders
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # enemy movement
    enemy_x += enemy_x_change
    
    # boarders
    if enemy_x <= 0:
        enemy_x_change = 3
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -3
        enemy_y += enemy_y_change
    
    #bullet movement
    if laser_y <= 0:
        laser_y = 480
        laser_state = "ready"

    if laser_state == "fire":
        fire_laser(laser_x, laser_y)
        laser_y -= laser_y_change
        
    


    # Player load 
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # always need that !!
    pygame.display.update()

