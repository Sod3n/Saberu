label scene4_5:
    
    scene three1
    show SamuraiIdle at left
    "Сверху начинают падать фрагменты доспехов. Подняв голову вверх можно увидеть…"
    hide SamuraiIdle
    show SamuraiAngry at left
    io  "Цурубэ-отоси…"
    show head at right
    ts  "Да, да, звали, господин самурай? Как замечательно, что вы здесь идете. Почаще бы здесь ходили люди. Было бы просто замечательно, вы не находите? Я ведь сижу совсем один в чаще леса, мне даже не с кем поговорить! Скука смертная."

    io  "Нет. Все знают, для чего тебе нужны люди."

    ts  "Что вы, я просто хочу поговорить, как говорю сейчас с вами. Ну, иногда хочу есть, а кто не хочет? Мне нравится звук, который издают люди, когда я их ем. Люди такие аппетитные и беззащитные."

    ts  "Просто падаешь и наслаждаешься их кампанией. Жаль только на последнем издыхании никто не говорит…"

    ts  "Недавно вот проходили люди. Друг с другом говорили, а увидели меня - вмиг разбежались. Ну и бросили своего товарища. Разжился он многим перед встречей со мной, а потому и мне теперь есть что предоставить вам!"

    "С дерева летит еще один фрагмент доспехов и ножи."

    io  "Но ты же можешь питаться чем-то другим, кроме людей."

    ts  "Люди вкуснее всего! Нет ничего лучше человеческой плоти."

    ts  "Какая жалость. Живой человек за столь долгое время, а мне уже наскучил этот разговор. Да кто ты такой, чтобы поучать меня? Думаю, ты будешь вкуснее, чем твои предшественники."
    
    menu:
        "Атаковать":
            $ minigame_win_scene = "scene5_5"
            $ minigame_lose_scene = "lose"
            $ store.minigame_enemy_behaviour = random.randint(1, 7)
            $ enemy_char = GCharacter((1920, 1080), "head.png", 6, "not_in_balance.png", "head.png", True, 0.35)
            $ enemy = ts
            $ minigame_back = "three1.png"
            $ io(minigame_enemy_behaviour_reaction[store.minigame_enemy_behaviour])
            jump minigame_start
        "Бежать":
            "К сожалению, побег от данного ёкая - плохая идея. Дух настигает, а Иошинори не был готов к бою."
            "Теперь он пища для ёкая."
            jump lose
            
    return