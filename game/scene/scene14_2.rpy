label scene14_2:

    scene mount1
    show SamuraiIdle at left
    show SamuraiNPCFight at right
    n "Стой, демон. Назовись!"
    hide SamuraiIdle
    show SanuraiBow at left
    io "Я не демон. Меня зовут Иошинори. Я иду из столицы в Судзу."
    hide SamuraiNPCFight
    show SamuraiNPC at right
    n "Прошу прощения. Самурай не должен терять хладнокровия. Больше такого не повторится."

    n "Приятно познакомиться, Иошинори. Меня зовут Норайо. Я понимаю, что оказанный мной прием не был теплым, но могу ли я попросить тебя о помощи?"

    n "Взамен я могу предложить тебе еду и ночлег. Согласен на такие условия?"
    hide SanuraiBow
    show SamuraiIdle at left
    io "Да."

    n "Пройдем тогда в мой дом."
    
    jump scene15_2
    
    return