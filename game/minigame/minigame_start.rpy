define player = Character("Игрок")
define enemy = Character("Враг")
define config.menu_include_disabled = True

init python:
    import random
    
    random_first_aciton = random.choice(minigame_actions_tuple)[1]
    player_char = GCharacter((1920, 1080), "sprite.png", 3, "sprite2.png", "sprite3.png", 0.2)
    enemy_char = GCharacter((1920, 1080), "enemy.jpg", 6, "enemy2.jpg", "enemy3.jpg", 0.2)
    do_action = False

    next_action = "parry"

    cell_positions = {
        1: (540, 150),
        2: (660, 150),
        3: (780, 150),
        4: (900, 150),
        5: (1020, 150),
        6: (1140, 150),
        7: (1260, 150),
        8: (1380, 150)
    }
    minigame_saved_rollback_limit = 0

    defence_positions = []

    def defence_fade_function(trans, st, at, cpos):
        a = 0.0

        if cpos in defence_positions:
            a = 1

        trans.alpha = a
        return 0.1

    defence_cells = []

    def_func = renpy.curry(defence_fade_function)
    for i in range(1, 9):
        defence_cells.append(Transform(Image("defence_cell.png"), function = def_func(cpos = i))) 


    damaged_positions = []

    def damage_fade_function(trans, st, at, cpos):
        a = 0.0

        if cpos in damaged_positions:
            a = 1.0

        trans.alpha = a
        return 0.1
    
    damage_cells = []
    dmg_func = renpy.curry(damage_fade_function)
    for i in range(1, 9):
        damage_cells.append(Transform(Image("damage_cell.png"), function = dmg_func(cpos = i))) 

screen minigame:
    add player_char
    add enemy_char
    for idi, i in enumerate(store.cell_positions):
        if idi == 0:
            add "left_cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.22
        elif idi == 7:
            add "right_cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.22
        elif idi < 2 or idi > 5:
            add "edge_cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.22
        else:
            add "cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.22


        add store.damage_cells[idi]:
            xpos store.cell_positions[i][0] 
            ypos store.cell_positions[i][1] - 55
            yanchor 1
            xanchor 0.5
            zoom 0.22

        add store.defence_cells[idi]:
            xpos store.cell_positions[i][0] 
            ypos store.cell_positions[i][1] - 35
            yanchor 1
            xanchor 0.5
            zoom 0.2

label minigame_start:
    $ player_char = GCharacter((1920, 1080), "sprite.png", 3, "sprite2.png", "sprite3.png", 0.2)
    $ enemy_char = GCharacter((1920, 1080), "enemy.jpg", 6, "enemy2.jpg", "enemy3.jpg", 0.2)
    $ store.minigame_used_pressure_hit_sequencly = 0
    $ store.minigame_enemy_def_success = False
    $ store.minigame_enemy_last_health = 0
    $ store.minigame_enemy_prepared_to_heal = False
    $ defence_positions.clear()
    $ damaged_positions.clear()
    $ do_action = False
    $ next_action = "parry"
    $ config.rollback_enabled = False
    $ store.minigame_saved_rollback_limit = config.hard_rollback_limit
    $ config.hard_rollback_limit = 0 
    show screen minigame
    $ player_char.look_at(enemy_char)
    $ enemy_char.look_at(player_char)
    $ renpy.redraw(player_char, 0)
    $ renpy.redraw(enemy_char, 0)

    $ renpy.jump("minigame_before_action")

    return