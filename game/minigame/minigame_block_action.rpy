label minigame_block_action:

    $ player_char.action = "block"
    if do_action:
        $ perform_action_in_order(player_char, enemy_char)
    $ do_action = True

    $ narrator("Как мне поступить?", interact=False)
    $ next_action = renpy.display_menu(filter_actions([ 
        to_tuple("hard_hit"), 
        to_tuple("jab"), 
        to_tuple("parry"), 
    ], player_char))
    $ renpy.jump("minigame_before_action")