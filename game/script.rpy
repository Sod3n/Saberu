define io = Character("Иошинори", color='#990066')
define t = Character("Торговец", color='#990066')
define raz = Character("Разбойник", color='#990066')
define ts = Character("Цурубэ-отоси", color='#990066')
define n = Character("Норайо", color='#990066')
define roc = Character("Рокеро", color='#990066')
define ch = Character("Чиаса", color='#990066')

define audio.bgmus1 = "audio/bgmus1.mp3"
define audio.bgmus2 = "audio/bgmus2.mp3"
define audio.bgmus2_2 = "audio/bgmus2_2.mp3"
define audio.bgmus3 = "audio/bgmus3.mp3"

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