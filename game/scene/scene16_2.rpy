label scene16_2:
    
    scene village1
    show SamuraiAngry at left
    show SamuraiNPC at right
    show Servant
    roc "Господин, это здесь."

    n "Она не могла далеко уйти. Мы с Иошинори пойдем вверх по улице, а вы ищите ниже!"

    roc "Есть!"
    hide Servant
    n "Что ж, если нас и вправду ведет судьба, то именно нам и суждено встретить проклятого духа."

    io "Кто это?"
    show rokuidle
    ch "Господин, что вы здесь делаете?"

    ch "Ах, простите мне мои манеры. Я Чиаса, наша семья изготавливает прекрасные ткани, в том числе для господина Норайо."

    n "Чиаса, убирайся с улицы! Здесь бродит мононокэ, который изводит жителей. Быстрее в дом!"

    io "Подожди… Посмотри на ее шею."

    n "Что? Что ты имеешь ввиду?"

    io "Пусть покажет свою шею."

    ch "Господин, негоже так. Я не могу показывать лицо незнакомцам."

    n "Чиаса права. Иди домой."

    ch "Не беспокойтесь, господин. Я могу о себе позаботиться."

    n "Эта тварь убила человека, мы избавимся от нее."

    ch "Убила? Кого убила? Я никого не убивала."
    hide SamuraiNPC
    show SamuraiNPCFight at right
    hide rokuidle
    show rokuevil
    n "Что? Ты… Монстр! Ты поплатишься за то, что сделала!"

    ch "Ах, какой же вы наивный. Неужели вы думаете, что сможете меня остановить?"

    $ minigame_win_scene = "scene18_1"
    $ minigame_lose_scene = "lose"
    $ store.minigame_enemy_behaviour = random.randint(1, 7)
    $ enemy_char = GCharacter((1920, 1080), "rokuevil.png", 6, "not_in_balance.png", "rokuevil.png", True, 0.35)
    $ enemy = ch
    $ minigame_back = "village1.png"
    $ io(minigame_enemy_behaviour_reaction[store.minigame_enemy_behaviour])
    jump minigame_start
    
    return