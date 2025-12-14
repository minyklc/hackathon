MAP_W = 20
MAP_H = 20

TILE_W = 64
TILE_H = 32

AVATARS_PER_MAP = 6
ANIMALS_PER_MAP = 3
TOOLS_PER_MAP = 4

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
    "cerf": "Cerf",
	"ver": "Ver",
	"renne": "Renne"
}

TOOLS = {
   "galet": {"name": "Galet aménagé", "fixed": True},
    "biface": {"name": "Biface", "fixed": True},
    "javelot": {"name": "Javelot", "fixed": True},
	"pomme": {"name": "pomme", "fixed": True},
	"baie": {"name": "baie", "fixed": True},
	"propulseur": {"name": "propulseur", "fixed": True},
	"epieux": {"name": "epieux", "fixed": True},
	"harpon": {"name": "harpon", "fixed": True},
	"grattoir": {"name": "grattoir", "fixed": True},
   "charognards": {"name": "charognards", "fixed": True}
	
}

TIMELINE = [
    {
        "date": "–7 à –6 millions d'années",
        "species": ["toumai"],
        "animals": [],
		"tools": [],
        "fire": False,
    },
    {
        "date": "–4,2 à –2 millions d'années",
        "species": ["toumai", "australopitheque"],
        "animals": ["ver"],
		"tools": ["charognards", "pomme", "baie"],
        "fire": False
    },
    {
        "date": "–2,4 à –1,6 millions d'années",
        "species": ["australopitheque", "habilis"],
        "animals": [],
		"tools": ["charognards", "galet"],
        "fire": False
    },
    {
        "date": "–1,9 à –300 000 ans",
        "species": ["habilis", "erectus"],
        "animals": ["bison", "renne"],
		"tools": ["galet", "biface", "epieux", "grattoir"],
        "fire": True,
    },
    {
        "date": "–400 000 à –40 000 ans",
        "species": ["erectus", "neandertal", "sapiens"],
        "animals": ["mammouth", "bison", "renne"],
		"tools": ["epieux", "grattoir", "biface", "javelot"],
        "fire": True
    },
    {
        "date": "–300 000 ans à aujourd’hui",
        "species": ["sapiens"],
        "animals": ["cerf", "bison", "renne"],
		"tools": ["javelot", "harpon", "propulseur"],
        "fire": True
    }
]

BIOME_COLOR = (110, 180, 110)
FIRE_COLOR = (220, 120, 40)
ROCK_COLOR = (120, 120, 120)
