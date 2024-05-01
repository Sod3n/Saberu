label minigame_parry_action:

    $ player_char.action = "parry"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ narrator("Как мне поступить?", interact=False)
    $ next_action = renpy.display_menu(filter_actions([ 
        to_tuple("jab"), 
        to_tuple("pressure_hit"), 
        to_tuple("short_hit"), 
    ], player_char))
    $ renpy.jump("minigame_before_action")

    