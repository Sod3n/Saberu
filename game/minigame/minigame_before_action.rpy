label minigame_before_action:
    $ enemy_char.action = random_action(enemy_char)
    $ renpy.jump("minigame_" + next_action + "_action")

    