
label start:
    $ minigame_win_scene = "win"
    $ minigame_lose_scene = "lose"
    menu:
        "Дерись"

        "Сильный шиш":
            $ store.minigame_enemy_behaviour = 0
            jump minigame_start

        "Быстрый шиш":
            $ store.minigame_enemy_behaviour = 1
            jump minigame_start
        
        "Хитрый шиш":
            $ store.minigame_enemy_behaviour = 2
            jump minigame_start

        "Безобидный шиш":
            $ store.minigame_enemy_behaviour = 3
            jump minigame_start

        "Шиш Дартаньян":
            $ store.minigame_enemy_behaviour = 4
            jump minigame_start

        "Паладин шиш":
            $ store.minigame_enemy_behaviour = 5
            jump minigame_start

        "Дальник шиш":
            $ store.minigame_enemy_behaviour = 6
            jump minigame_start