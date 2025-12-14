import pygame
from config import SPECIES, ANIMALS

def draw_ui(surface, map_data):
    font = pygame.font.SysFont(None, 22)
    era = map_data["era"]

    date = font.render(era["date"], True, (240,240,240))
    desc = font.render(era["description"], True, (200,200,200))

    surface.blit(date, (surface.get_width()-460, 10))
    surface.blit(desc, (surface.get_width()-460, 35))

    species = ", ".join(SPECIES[s] for s in era["species"])
    sp = font.render("Humains : " + species, True, (240,240,240))
    surface.blit(sp, (10, surface.get_height()-50))

    if era["animals"]:
        animals = ", ".join(ANIMALS[a] for a in era["animals"])
        an = font.render("Animaux : " + animals, True, (220,220,220))
        surface.blit(an, (10, surface.get_height()-25))
