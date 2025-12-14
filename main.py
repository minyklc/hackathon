import pygame
import avatars
from world import create_map, update_characters
from render import draw_map
from ui import draw_ui

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

avatars.load_avatars()

maps = [create_map(i) for i in range(6)]
current = 0

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and current < len(maps)-1:
                current += 1
            if e.key == pygame.K_DOWN and current > 0:
                current -= 1

    update_characters(maps[current])
    draw_map(screen, maps[current], screen.get_width())
    draw_ui(screen, maps[current])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
