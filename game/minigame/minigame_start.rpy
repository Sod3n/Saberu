define player = Character("Игрок")
define enemy = Character("Враг")
define config.menu_include_disabled = True

init python:
    import random
    
    random_first_aciton = random.choice(minigame_actions_tuple)[1]
    do_action = False

    next_action = "parry"

    cell_positions = {
        1: (201, 300),
        2: (418, 300),
        3: (635, 300),
        4: (852, 300),
        5: (1069, 300),
        6: (1286, 300),
        7: (1503, 300),
        8: (1720, 300)
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

    minigame_back = Solid("#000")

screen minigame:

    transform:
        image minigame_back
        matrixcolor BrightnessMatrix(-0.15)
        blur 30.0
        
    add player_char
    add enemy_char
    for idi, i in enumerate(store.cell_positions):
        if idi == 0:
            add "left_cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.43
        elif idi == 7:
            add "right_cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.43
        elif idi < 2 or idi > 5:
            add "edge_cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.43
        else:
            add "cell.png":
                xpos store.cell_positions[i][0] 
                ypos store.cell_positions[i][1] - 45
                yanchor 1
                xanchor 0.5
                zoom 0.43


        add store.damage_cells[idi]:
            xpos store.cell_positions[i][0] 
            ypos store.cell_positions[i][1] - 55
            yanchor 1
            xanchor 0.5
            zoom 0.43

        add store.defence_cells[idi]:
            xpos store.cell_positions[i][0] 
            ypos store.cell_positions[i][1] - 35
            yanchor 1
            xanchor 0.5
            zoom 0.43

label minigame_start:
    play music bgmus2_2
    $ player_char = GCharacter((1920, 1080), "SamuraiDrinking.png", 3, "not_in_balance.png", "SamuraiDrinking.png", False, 0.35)
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