label minigame_dodge_action:

    $ player_char.action = "dodge"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ renpy.jump("minigame_action_menu")

    