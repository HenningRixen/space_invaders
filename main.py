import pygame
import random

# intialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

# title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Enemy
enemy_img = pygame.image.load("monster.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(50, 150)
enemy_x_change = 0

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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.3
        
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

    # Player load 
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # always need that !!
    pygame.display.update()

