from config import TILE_W, TILE_H

def iso_coords(x, y, screen_width):
    screen_x = (x - y) * TILE_W // 2 + screen_width // 2
    screen_y = (x + y) * TILE_H // 2 + 80
    return screen_x, screen_y
