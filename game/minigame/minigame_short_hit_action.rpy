label minigame_short_hit_action:

    $ player_char.action = "short_hit"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ narrator("Как мне поступить?", interact=False)
    $ next_action = renpy.display_menu(filter_actions([ 
        to_tuple("block"), 
        to_tuple("dodge"), 
        to_tuple("jab"), 
    ], player_char))
    $ renpy.jump("minigame_before_action")

    