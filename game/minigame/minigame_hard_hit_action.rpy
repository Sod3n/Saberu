label minigame_hard_hit_action:

    $ player_char.action = "hard_hit"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ narrator("Как мне поступить?", interact=False)
    $ next_action = renpy.display_menu(filter_actions(get_actions_after_action(player_char.action), 
        player_char), screen = "horizontal_choice")
    $ renpy.jump("minigame_before_action")

    