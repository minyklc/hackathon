if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    x, y = screen_to_grid(*pygame.mouse.get_pos(), screen.get_width())
    add_character_to_map(maps[current_map_index], x, y)
