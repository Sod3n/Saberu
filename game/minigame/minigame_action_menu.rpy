label minigame_action_menu:

    $ narrator("Как мне поступить?", interact=False)
    $ next_action = renpy.display_menu(filter_actions(get_actions_after_action(player_char.action), 
        player_char, enemy_char), screen = "horizontal_choice")
    $ renpy.jump("minigame_before_action")