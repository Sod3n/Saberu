label minigame_pressure_hit_action:

    $ player_char.action = "pressure_hit"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ renpy.jump("minigame_action_menu")

    