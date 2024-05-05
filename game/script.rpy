define io = Character("Иошинори", color='#3E072C')
define t = Character("Торговец", color='#3E072C')
define raz = Character("Разбойник", color='#3E072C')
define ts = Character("Цурубэ-отоси", color='#3E072C')
define n = Character("Норайо", color='#3E072C')
define roc = Character("Рокеро", color='#3E072C')
define ch = Character("Чиаса", color='#3E072C')

define audio.bgmus1 = "audio/bgmus1.mp3"
define audio.bgmus2 = "audio/bgmus2.mp3"
define audio.bgmus2_2 = "audio/bgmus2_2.mp3"
define audio.bgmus3 = "audio/bgmus3.mp3"

image Bandit = "Bandit.png"
image Merchant = "Merchant.png"
image Merchant2 = "Merchant2.png"
image Merchantflip = "Merchantflip.png"
image SamuraiAngry = "SamuraiAngry.png"
image SamuraiDrinking = "SamuraiDrinking.png"
image SamuraiEat = "SamuraiEat.png"
image SamuraiIdle = "SamuraiIdle.png"
image SamuraiNPC = "SamuraiNPC.png"
image SanuraiBow = "SanuraiBow.png"

style say_label:
    bold True

screen notif_screen:
    add dictionary_notification:
        ypos 0
        yanchor 0

label start:
    jump scene1
    show screen notif_screen
    $ add_to_dictionary("Фраза 1 - это определенно фраза")
    "Фраза 1"
    $ add_to_dictionary("Фраза 2 - это определенно фраза")
    "Фраза 2"

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