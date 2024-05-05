label minigame_wait_with_sake_action:

    $ player_char.action = "wait_with_sake"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ renpy.jump("minigame_action_menu")

    