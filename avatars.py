import pygame

HUMANS = {}
ANIMALS = {}
FIRE = {}
ITEM = {}

def load_avatars():
    for name in [
        "toumai", "australopitheque", "habilis",
        "erectus", "neandertal", "sapiens"
    ]:
        HUMANS[name] = pygame.image.load(
            f"assets/avatars/{name}.png"
        ).convert_alpha()

    for name in ["bison", "cerf", "mammouth", "ver", "renne"]:
        ANIMALS[name] = pygame.image.load(
            f"assets/animals/{name}.png"
        ).convert_alpha()
    
    for name in ["feu"]:
        FIRE[name] = pygame.image.load(
            f"assets/items/{name}.png"
        ).convert_alpha()

    for name in ["biface", "galet", "javelot", "pomme", "baie", "propulseur", "epieux", "harpon", "grattoir", "charognards"]:
        ITEM[name] = pygame.image.load(
            f"assets/items/{name}.png"
        ).convert_alpha()

def get_item(name):
    return ITEM.get(name)

def get_human(name):
    return HUMANS.get(name)

def get_animal(name):
    return ANIMALS.get(name)

def get_fire(name):
    return FIRE.get(name)


