import pygame
from config import MAP_W, MAP_H, BIOME_COLOR, FIRE_COLOR, ROCK_COLOR
from isometric import iso_coords
import avatars

def draw_tile(x, y, color, surface, screen_width):
    px, py = iso_coords(x, y, screen_width)
    points = [
        (px, py),
        (px+32, py+16),
        (px, py+32),
        (px-32, py+16)
    ]
    pygame.draw.polygon(surface, color, points)
    pygame.draw.polygon(surface, (40,40,40), points, 1)


def draw_map(surface, map_data, screen_width):
    surface.fill((25,25,25))

    for x in range(MAP_W):
        for y in range(MAP_H):
            draw_tile(x, y, BIOME_COLOR, surface, screen_width)

    for x, y in map_data["rocks"]:
        draw_tile(x, y, ROCK_COLOR, surface, screen_width)

    for x, y in map_data["fires"]:
        px, py = iso_coords(x, y, screen_width)
        draw_tile(x, y, FIRE_COLOR, surface, screen_width)
        img = avatars.get_fire("feu")
        if img:
            surface.blit(img, img.get_rect(center=(px, py + 16)))

    for a in map_data["animals"]:
        px, py = iso_coords(a["x"], a["y"], screen_width)
        img = avatars.get_animal(a["type"])
        if img:
            surface.blit(img, img.get_rect(center=(px, py)))

    for c in map_data["characters"]:
        px, py = iso_coords(c["x"], c["y"], screen_width)
        img = avatars.get_human(c["avatar"])
        if img:
            surface.blit(img, img.get_rect(center=(px, py)))
