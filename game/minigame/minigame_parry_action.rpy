label minigame_parry_action:

    $ player_char.action = "parry"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ renpy.jump("minigame_action_menu")

    