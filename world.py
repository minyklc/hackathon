import random
from config import MAP_W, MAP_H, TIMELINE, AVATARS_PER_MAP, ANIMALS_PER_MAP, TOOLS

def create_map(index):
    era = TIMELINE[index]

    map_data = {
        "era": era,
        "characters": [],
        "animals": [],
        "fires": [],
        "rocks": [],
        "items": []
    }

    if era["fire"]:
        map_data["fires"].append((MAP_W//2, MAP_H//2))

    for _ in range(10):
        map_data["rocks"].append((
            random.randint(0, MAP_W-1),
            random.randint(0, MAP_H-1)
        ))

    for _ in range(AVATARS_PER_MAP):
        map_data["characters"].append({
            "x": random.randint(5, MAP_W-5),
            "y": random.randint(5, MAP_H-5),
            "avatar": random.choice(era["species"]),
            "timer": random.randint(60, 180)
        })

    for _ in range(ANIMALS_PER_MAP):
        if era["animals"]:
            map_data["animals"].append({
                "x": random.randint(0, MAP_W-1),
                "y": random.randint(0, MAP_H-1),
                "type": random.choice(era["animals"]),
                "timer": random.randint(120, 240)
            })

    for tool in era["tools"]:
        info = TOOLS[tool]
        if info["fixed"]:
            zone = random.choice(map_data["rocks"])
            x, y = zone
        else:
            x = random.randint(0, MAP_W-1)
            y = random.randint(0, MAP_H-1)

        map_data["items"].append({
            "type": tool,
            "x": x,
            "y": y
        })

    return map_data


def update_characters(map_data):
    fires = map_data["fires"]

    for c in map_data["characters"]:
        c["timer"] -= 1
        if c["timer"] <= 0:
            if fires and random.random() < 0.4:
                fx, fy = fires[0]
                dx = 1 if fx > c["x"] else -1 if fx < c["x"] else 0
                dy = 1 if fy > c["y"] else -1 if fy < c["y"] else 0
            else:
                dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])

            nx, ny = c["x"] + dx, c["y"] + dy
            if 0 <= nx < MAP_W and 0 <= ny < MAP_H:
                c["x"], c["y"] = nx, ny
            c["timer"] = random.randint(90, 240)

    for a in map_data["animals"]:
        a["timer"] -= 1
        if a["timer"] <= 0:
            dx, dy = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
            nx, ny = a["x"] + dx, a["y"] + dy
            if 0 <= nx < MAP_W and 0 <= ny < MAP_H:
                a["x"], a["y"] = nx, ny
            a["timer"] = random.randint(120, 300)
