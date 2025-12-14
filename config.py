MAP_W = 20
MAP_H = 20

TILE_W = 64
TILE_H = 32

AVATARS_PER_MAP = 6
ANIMALS_PER_MAP = 3

SPECIES = {
    "toumai": "Toumaï",
    "australopitheque": "Australopithèque",
    "habilis": "Homo habilis",
    "erectus": "Homo erectus",
    "neandertal": "Néandertal",
    "sapiens": "Homo sapiens"
}

ANIMALS = {
    "mammouth": "Mammouth",
    "bison": "Bison",
    "cerf": "Cerf"
}

TOOLS = {
    "galet": {"name": "Galet aménagé", "fixed": True},
    "biface": {"name": "Biface", "fixed": True},
    "javelot": {"name": "Javelot", "fixed": False},
}

TIMELINE = [
    {
        "date": "–7 à –6 millions d'années",
        "description": "Premiers homininés connus.",
        "species": ["toumai"],
        "animals": [],
		"tools": [],
        "fire": False,
    },
    {
        "date": "–4,2 à –2 millions d'années",
        "description": "Bipédie affirmée.",
        "species": ["toumai", "australopitheque"],
        "animals": ["cerf"],
		"tools": [],
        "fire": False
    },
    {
        "date": "–2,4 à –1,6 millions d'années",
        "description": "Premiers outils.",
        "species": ["australopitheque", "habilis"],
        "animals": ["cerf"],
		"tools": ["galet"],
        "fire": False
    },
    {
        "date": "–1,9 à –300 000 ans",
        "description": "Maîtrise du feu.",
        "species": ["habilis", "erectus"],
        "animals": ["bison"],
		"tools": ["galet", "biface"],
        "fire": True,
    },
    {
        "date": "–400 000 à –40 000 ans",
        "description": "Culture et chasse.",
        "species": ["erectus", "neandertal", "sapiens"],
        "animals": ["mammouth", "bison"],
		"tools": ["biface", "javelot"],
        "fire": True
    },
    {
        "date": "–300 000 ans à aujourd’hui",
        "description": "Sociétés complexes.",
        "species": ["sapiens"],
        "animals": ["cerf", "bison"],
		"tools": ["javelot"],
        "fire": True
    }
]

BIOME_COLOR = (110, 180, 110)
FIRE_COLOR = (220, 120, 40)
ROCK_COLOR = (120, 120, 120)
