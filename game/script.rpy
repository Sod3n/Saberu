
label start:
    $ minigame_win_scene = "win"
    $ minigame_lose_scene = "lose"
    menu:
        "Дерись"

        "Сильный шиш":
            $ store.minigame_enemy_behaviour = 0
            $ enemy = Character("Сильный шиш")
            jump minigame_start

        "Быстрый шиш":
            $ store.minigame_enemy_behaviour = 1
            $ enemy = Character("Быстрый шиш")
            jump minigame_start
        
        "Хитрый шиш":
            $ store.minigame_enemy_behaviour = 2
            $ enemy = Character("Хитрый шиш")
            jump minigame_start

        "Безобидный шиш":
            $ store.minigame_enemy_behaviour = 3
            $ enemy = Character("Безобидный шиш")
            jump minigame_start

        "Шиш Дартаньян":
            $ store.minigame_enemy_behaviour = 4
            $ enemy = Character("Шиш Дартаньян")
            jump minigame_start

        "Паладин шиш":
            $ store.minigame_enemy_behaviour = 5
            $ enemy = Character("Паладин шиш")
            jump minigame_start

        "Дальник шиш":
            $ store.minigame_enemy_behaviour = 6
            $ enemy = Character("Дальник шиш")
            jump minigame_start

        "Крапива шиш":
            $ store.minigame_enemy_behaviour = 7
            $ enemy = Character("Крапива шиш")
            jump minigame_start