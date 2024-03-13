import pygame
import random
import math

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

#score 

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

text_x = 10
text_y = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

#clock
clock = pygame.time.Clock()

#game win
win_font = pygame.font.Font("freesansbold.ttf", 32)

def game_win_text():
    win_text = win_font.render("WINNER WINNER CHICKEN DINNER", True, (255,255,255))
    screen.blit(win_text, (150, 250))

#game over
over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

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

def isCollision(enemy_x, enemy_y, laser_x, laser_y):
    distance = math.sqrt(((enemy_x - laser_x)**2) + ((enemy_y - laser_y)**2))
    if distance < 27:
        return True
    else:
        return False

#Boss enemy
dragon_img = pygame.image.load("final-boss.png")
dragon_x = 330
dragon_y = 45
dragon_x_change = 2

def dragon(x,y):
    screen.blit(dragon_img, (x,y))

def is_Collision_Dragon(enemy_x, enemy_y, laser_x, laser_y):
    distance = math.sqrt(((enemy_x - laser_x)**2) + ((enemy_y - laser_y)**2))
    if distance < 70:
        return True
    else:
        return False

# Boss shots fire 
fire_img = pygame.image.load("fire.png")
fire_x = 330
fire_y = 45
fire_x_change = 0
fire_y_change = 5
fireball_cooldown = 50
fireball_timer = fireball_cooldown

def fireball(x,y):
    screen.blit(fire_img, (x + 16, y + 10))

def colission_dragon_fire(player_x, player_y, fire_x, fire_y):
    dead = math.sqrt(((player_x - fire_x)**2) + ((player_y - fire_y)**2))
    if dead < 70:
        return True
    else:
        return False

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 4

for i in range(num_of_enemy):
    enemy_img.append(pygame.image.load("monster.png")) 
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(2)
    enemy_y_change.append(30)

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


# Player
player_img = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0
player_health = 10

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
    for i in range(num_of_enemy):

        # game over 
        if enemy_y[i] == 440:
            for j in range(num_of_enemy):
                enemy_y[j] = 2000
            game_over_text()
            break

        #dragon
        if score_value >= 50:
            for j in range(num_of_enemy):
                enemy_y[j] = 2000
                
               
                # call dragon
                dragon(dragon_x, dragon_y)
                
                
                #hit by fire
                

                hit = colission_dragon_fire(player_x, player_y, fire_x, fire_y)
                if hit:
                    player_health -=10
                    
                    
                if player_health <= 0:
                    dragon_x = 2000
                    game_over_text()
                    break
                

                # dragon fire movement
                
                
                fire_x = dragon_x
                fireball(fire_x, fire_y)
                # dragon countdown fireball
                
                fireball_timer -= 2
                if fireball_timer <= 0:
                    fire_y += fire_y_change
                    fireball_timer = fireball_cooldown
                
                if fire_y >= 600:
                    fire_y = 45
                
                # dragon colission with laser 
                colission = is_Collision_Dragon(dragon_x, dragon_y, laser_x, laser_y)
                if colission:
                    laser_y = 480
                    laser_state = "ready"
                    score_value += 25
         
                
                #game win

                if score_value >= 150:
                    dragon_x = 2000 
                    fire_x = 2000
                    game_win_text()
                    break
        
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -2
            enemy_y[i] += enemy_y_change[i]
        
        # colission
        colission = isCollision(enemy_x[i], enemy_y[i], laser_x, laser_y)
        if colission:
            laser_y = 480
            laser_state = "ready"
            score_value += 10
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)


    # dragon movement
    
    dragon_x += dragon_x_change
    if dragon_x <= 0:
        dragon_x_change = 2
        
    elif dragon_x >= 690:
        dragon_x_change = -2
                

    #laser movement
    if laser_y <= 0:
        laser_y = 480
        laser_state = "ready"

    if laser_state == "fire":
        fire_laser(laser_x, laser_y)
        laser_y -= laser_y_change
    

    # Player load 
    player(player_x, player_y)
    show_score(text_x, text_y)
    

    #frame rate
    clock.tick(120)
    # always need that !!
    pygame.display.update()



