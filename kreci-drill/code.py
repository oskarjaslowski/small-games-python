import pygame,sys,time
from settings import *
from sprites import BG, Ground, Kret, Pipe

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Kreci Drill')
        pygame.display.set_icon(pygame.image.load('graphics/kret0.png').convert_alpha())
        self.clock = pygame.time.Clock()
        self.active = False

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        bg_height = pygame.image.load('graphics/background.png').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height
        BG(self.all_sprites,self.scale_factor)
        Ground([self.all_sprites,self.collision_sprites],self.scale_factor)

        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        self.font = pygame.font.Font('font/pixel.ttf',40)
        self.fonts = pygame.font.Font('font/pixel.ttf',30)
        self.score = 0
        self.start_offset = 0

        self.menu_surf = pygame.image.load('graphics/menu.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

    def collisions(self):
        if pygame.sprite.spritecollide(self.kret,self.collision_sprites,False,pygame.sprite.collide_mask):
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'pipe':
                    sprite.kill()
            self.active = False
            self.kret.kill()
            
    def display_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
            y = WINDOW_HEIGHT/8
        else:
            y = WINDOW_HEIGHT/2 + 100 + self.menu_rect.height
            score_surf = self.font.render('Kreci Drill',False,'white')
            score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH/2,WINDOW_HEIGHT/4))
            self.display_surface.blit(score_surf,score_rect)
            start_surf = self.fonts.render('To Start',False,'white')
            start_rect = start_surf.get_rect(midtop = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2 + 75))
            self.display_surface.blit(start_surf,start_rect)
        score_surf = self.font.render(str(self.score),False,'white')
        score_rect = score_surf.get_rect(midtop = (WINDOW_WIDTH/2,y))
        self.display_surface.blit(score_surf,score_rect)

    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.active:
                        self.kret.jump()
                    else:
                        self.kret = Kret(self.all_sprites,self.scale_factor / 1.6)
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()

                if event.type == self.obstacle_timer and self.active == True:
                    Pipe([self.all_sprites,self.collision_sprites],self.scale_factor)

            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.active:
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf,self.menu_rect)

            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()