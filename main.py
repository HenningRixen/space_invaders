import pygame

# intialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

# title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB - Red, Green, Blue
    screen.fill((39, 45,  87))
    # always need that !!
    pygame.display.update()

