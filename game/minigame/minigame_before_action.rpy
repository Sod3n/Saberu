label minigame_before_action:
    if do_action:
        $ enemy_char.action = get_enemy_action(enemy_char, player_char)
    $ renpy.jump("minigame_" + next_action + "_action")

    