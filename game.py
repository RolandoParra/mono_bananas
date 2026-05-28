import pygame
import random
from assets.src.classes import banana, player, puntaje, vidas

pygame.init()

lost = pygame.mixer.Sound("assets/sounds/lost.wav")
coin = pygame.mixer.Sound("assets/sounds/coin.mp3")
bg = pygame.image.load("assets/images/BG.png")
screen = pygame.display.set_mode((1024, 800))
blanco = (255, 255, 255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    bg = pygame.image.load("assets/images/BG.png")
    screen = pygame.display.set_mode((1024, 800))
    screen.blit(bg, (0, 0))

    screen.blit(banana.sp_banana, (banana.x, banana.y))
    screen.blit(player.sp_player, (player.x, 700))
    fuente = pygame.font.SysFont("comic sans ms", 35, 1, 1)
    texto = fuente.render(str(puntaje), 1, blanco)
    screen.blit(texto, (0, 50))

    if player.rect.colliderect(banana.rect):
        coin.play()
        puntaje.score += 1
        banana.rect.x = random.randint(0, 750)
        banana.rect.y = random.randint(0, 550)

    if player.rect.colliderect(vidas.rect):
        lost.play()
        vidas.lives -= 1
        vidas.rect.x = random.randint(0, 750)
        vidas.rect.y = random.randint(0, 550)

    if vidas.lives <= 0:
        lost.play()
        print("Game Over")
        pygame.quit()
        exit()

    pygame.display.update()