define player = Character("Игрок")
define enemy = Character("Враг")
define config.menu_include_disabled = True

init python:
    import random
    
    random_first_aciton = random.choice(minigame_actions_tuple)[1]
    player_char = GCharacter((1920, 1080), "sprite.png", 3, "sprite2.png", "sprite3.png", 0.2)
    enemy_char = GCharacter((1920, 1080), "sprite.png", 6, "sprite2.png", "sprite3.png", 0.2)
    do_action = False

    next_action = random_first_aciton

screen minigame:
    add player_char
    add enemy_char

label minigame_start:
    show screen minigame

    $ player_char.look_at(enemy_char)
    $ enemy_char.look_at(player_char)
    $ renpy.redraw(player_char, 0)
    $ renpy.redraw(enemy_char, 0)

    $ renpy.jump("minigame_before_action")

    return