import pygame
import avatars
from config import SPECIES, ANIMALS, TOOLS

def draw_ui(surface, map_data):
    font = pygame.font.SysFont(None, 22)
    era = map_data["era"]

    date = font.render(era["date"], True, (240,240,240))

    surface.blit(date, (surface.get_width()-460, 10))


    species = ", ".join(SPECIES[s] for s in era["species"])
    sp = font.render("Humains : " + species, True, (240,240,240))
    surface.blit(sp, (10, surface.get_height()-100))

    if era["animals"]:
        animals = ", ".join(ANIMALS[a] for a in era["animals"])
        an = font.render("Animaux : " + animals, True, (220,220,220))
        surface.blit(an, (10, surface.get_height()-75))

    y = surface.get_height() - 50
    for tool in era["tools"]:
        img = avatars.get_item(tool)
        name = TOOLS[tool]["name"]
        surface.blit(img, (10, y))
        surface.blit(font.render(name, True, (230,230,230)), (10, y))
        y += 25
