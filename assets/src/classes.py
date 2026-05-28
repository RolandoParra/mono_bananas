import random
import pygame

pygame.init()

puntaje = 0
vidas = 3


class banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, 800)
        self.y = 0
        self.sp_banana = pygame.image.load('assets/images/banana.jpg')
    
    def move(self):
        self.y += 5
    
    def delete(self):
        global vidas
        vidas -= 1
        self.kill()


class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 550
        self.sp_player = pygame.image.load('assets/images/mono.png')
        self.image = self.sp_player
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x)
    
    def move(self, direction):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= 5
        elif keys[pygame.K_d] and self.x < 750:
            self.x += 5
    
    def comer(self, banana):
        if self.sprite.collide_rect(self, banana):
            global puntaje
            puntaje += 1
            banana.kill()
            pygame.mixer.Sound('assets/sounds/coin.mp3').play()

