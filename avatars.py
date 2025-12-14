import pygame

# Dictionnaire d'avatars
# clé = nom
# valeur = image pygame
AVATARS = {}

def load_avatars():
    AVATARS["sapiens"] = pygame.image.load("assets/avatars/sapiens.png").convert_alpha()
    AVATARS["erectus"] = pygame.image.load("assets/avatars/erectus.png").convert_alpha()
    AVATARS["habilis"] = pygame.image.load("assets/avatars/habilis.png").convert_alpha()
    AVATARS["neandertal"] = pygame.image.load("assets/avatars/neandertal.png").convert_alpha()
    AVATARS["australopitheque"] = pygame.image.load("assets/avatars/australopitheque.png").convert_alpha()
    AVATARS["toumai"] = pygame.image.load("assets/avatars/toumai.png").convert_alpha()

def get_avatar(name):
    return AVATARS.get(name)