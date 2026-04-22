import pygame, sys, random

class Button1:
    def __init__(self,text,width,height,pos):
        self.pressed = False

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (200,200,200)
        self.text_surf = game_font.render(text,True,(20,20,20))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        global difficulty
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (120,120,120)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    difficulty = 10
                    game()
                    self.pressed = False
        else:
            self.top_color = (200,200,200)

class Button2:
    def __init__(self,text,width,height,pos):
        self.pressed = False

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (200,200,200)
        self.text_surf = game_font.render(text,True,(20,20,20))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        global difficulty
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (120,120,120)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    difficulty = 15
                    game()
                    self.pressed = False
        else:
            self.top_color = (200,200,200)

class Button3:
    def __init__(self,text,width,height,pos):
        self.pressed = False

        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (200,200,200)
        self.text_surf = game_font.render(text,True,(20,20,20))
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        global difficulty
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (120,120,120)
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    difficulty = 20
                    game()
                    self.pressed = False
        else:
            self.top_color = (200,200,200)

def ball_animation():
    global running, ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <= 0:
        ball_restart()
        player_score += 1
        if player_score > 10:
            running = False

    if ball.right >= screen_width:
        ball_restart()
        opponent_score += 1
        if opponent_score > 10:
            running = False

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    global player_speed
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

def draw_score():
    score_text = str(opponent_score) + str("  :  ") + str(player_score)
    score_surface = game_font.render(score_text,True,(200,200,200))
    score_x = int(screen_width/2)
    score_y = int(60)
    score_rect = score_surface.get_rect(center = (score_x,score_y))
    screen.blit(score_surface,score_rect)

def game():
    global player_speed, running
    running = True
    setting_up()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += difficulty
                if event.key == pygame.K_UP:
                    player_speed -= difficulty
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= difficulty
                if event.key == pygame.K_UP:
                    player_speed += difficulty
        
        screen.fill(bg_color)

        ball_animation()
        player_animation()
        opponent_ai()
        draw_score()

        pygame.draw.rect(screen,light_grey, player)
        pygame.draw.rect(screen,light_grey, opponent)
        pygame.draw.ellipse(screen,light_grey, ball)
        
        pygame.display.flip()
        clock.tick(60)

def setting_up():
    global difficulty, ball, player, opponent, bg_color, light_grey, ball_speed_x, ball_speed_y, player_speed, opponent_speed, player_score, opponent_score

    ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
    player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
    opponent = pygame.Rect(10, screen_height/2 - 70,10,140)

    bg_color = (20,20,20)
    light_grey = (200,200,200)

    ball_speed_x = difficulty * random.choice((1,-1))
    ball_speed_y = difficulty * random.choice((1,-1))
    player_speed = 0
    opponent_speed = difficulty

    player_score = 0
    opponent_score = 0

def main_menu():
    while True:
        screen.fill((20,20,20))

        title_text = str('PONG')
        title_surface = title_font.render(title_text,True,(200,200,200))
        title_x = int(screen_width/2)
        title_y = int(200)
        title_rect = title_surface.get_rect(center = (title_x,title_y))
        screen.blit(title_surface,title_rect)

        title_text = str('Choose difficulty:')
        title_surface = game_font.render(title_text,True,(200,200,200))
        title_x = int(screen_width/2)
        title_y = int(400)
        title_rect = title_surface.get_rect(center = (title_x,title_y))
        screen.blit(title_surface,title_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        button_1.draw()
        button_2.draw()
        button_3.draw()

        pygame.display.update()
        clock.tick(60)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')
game_font = pygame.font.Font(None,100)
title_font = pygame.font.Font(None,200)

button_1 = Button1('NORMAL',screen_width/2,100,(screen_width/4,500))
button_2 = Button2('HARD',screen_width/2,100,(screen_width/4,650))
button_3 = Button3('IMPOSSIBLE',screen_width/2,100,(screen_width/4,800))

main_menu()