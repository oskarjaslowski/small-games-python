import pygame, sys, random

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = game_font.render(f'Score: {current_time}', False, (17, 48, 92))
    score_rect = score_surf.get_rect(center = (400,100))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(bollard_surf,obstacle_rect)
            else: screen.blit(sign_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()

clock = pygame.time.Clock()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
icon = pygame.image.load('assets/graphics/icon.png').convert_alpha()
game_font = pygame.font.Font('assets/fonts/game_font.ttf', 50)
sky_surf = pygame.image.load('assets/graphics/sky.png').convert_alpha()
ground_surf = pygame.image.load('assets/graphics/ground.png').convert_alpha()
bollard_surf = pygame.image.load('assets/graphics/bollard.png').convert_alpha()
sign_surf = pygame.image.load('assets/graphics/sign.png').convert_alpha()
obstacle_rect_list = []
player_walk1 = pygame.image.load('assets/graphics/player/walk1.png').convert_alpha()
player_walk2 = pygame.image.load('assets/graphics/player/walk2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('assets/graphics/player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
score = 0
title_screen = pygame.image.load('assets/graphics/player/title_screen.png').convert_alpha()
title_screen = pygame.transform.rotozoom(title_screen,0,2)
title_screen_rect = title_screen.get_rect(center = (400,200))
jump_sound = pygame.mixer.Sound('assets/sounds/he.wav')
jump_sound.set_volume(0.6)
game_active = False
start_time = 0
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)
pygame.display.set_caption('Ball Runner')
pygame.display.set_icon(icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    jump_sound.play()    
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if random.randint(0,2):
                obstacle_rect_list.append(bollard_surf.get_rect(bottomright = (random.randint(900,1100),300)))
            else:
                obstacle_rect_list.append(sign_surf.get_rect(topright = (random.randint(900,1100),0)))

    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf,(0,300))
        score = display_score()

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        
        player_animation()
        screen.blit(player_surf, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(title_screen,title_screen_rect)
        title_surf = game_font.render('Ball Runner', False, (17, 48, 92))
        title_rect = title_surf.get_rect(center = (400,50))
        screen.blit(title_surf,title_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        
        if score == 0:
            inst_surf = game_font.render('Tap SPACE to Play', False, (17, 48, 92))
            inst_rect = inst_surf.get_rect(center = (400,350))
            screen.blit(inst_surf,inst_rect)
        else:
            score_message = game_font.render(f'Your Last Score: {score}', False, (17, 48, 92))
            score_message_rect = score_message.get_rect(center = (400, 350))
            screen.blit(score_message,score_message_rect)
    
    pygame.display.update()
    clock.tick(60)