label scene2:
    
    scene les1
    show Bandit at right
    show Merchantflip at left
    raz "А неплохо так ты, старик, разжился. Делиться не учили? А то, знаешь ли, моим ребятам сейчас тяжко приходится."
    raz "Всякая нечисть в лесу еще, а ты тут ходишь, провоцируешь."
    t "Зарабатывать надо честным трудом."
    raz "А, честным трудом говоришь? Ну так мы это, точно, защищаем вас. В любой момент ведь могут напасть варвары, или того хуже - мононокэ явится."
    raz "Вот что вы, слабаки, будете делать без нас? Думаешь, самураям из столицы есть дело до таких как ты?"
    
    menu:
        "Помочь":
            hide Merchantflip
            show SamuraiAngry at left
            io "Неужели ты обвиняешь сёгуна в бездействии своим грязным языком?"
            raz "Что? А ты еще кто?.."
            io "Как самурай я должен пресечь подобное поведение. Вы либо глупцы, либо уверены в своей победе. Что ж, поплатись за свою беспечность."
            "Разбойник начинает убегать. Он седлает своего коня и скрывается в лесной чаще."
            jump scene3_1
        "Пройти мимо":
            raz "Ну, чего ты уставился на меня? Мои ребята погибают защищая тебя, а ты не можешь просто поделиться?"
            raz "Нам тут вот, видишь ли, плохо платят. Да, да, и ты оттуда же. Да это все равно что испортить урожай риса!"
            jump scene3_2
    return