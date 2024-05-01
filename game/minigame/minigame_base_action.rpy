label minigame_base_action:

    $ narrator("Как мне поступить?", interact=False)
    $ next_action = renpy.display_menu([ 
        to_tuple("block"), 
        to_tuple("dodge"), 
        to_tuple("hard_hit"), 
        to_tuple("jab"), 
        to_tuple("parry"), 
        to_tuple("pressure_hit"), 
        to_tuple("short_hit"), 
    ])
    $ renpy.jump("minigame_before_action")

    