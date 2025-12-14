import pygame

HUMANS = {}
ANIMALS = {}

def load_avatars():
    for name in [
        "toumai", "australopitheque", "habilis",
        "erectus", "neandertal", "sapiens"
    ]:
        HUMANS[name] = pygame.image.load(
            f"assets/avatars/{name}.png"
        ).convert_alpha()

    for name in ["bison", "cerf", "mammouth"]:
        ANIMALS[name] = pygame.image.load(
            f"assets/animals/{name}.png"
        ).convert_alpha()


def get_human(name):
    return HUMANS.get(name)

def get_animal(name):
    return ANIMALS.get(name)
