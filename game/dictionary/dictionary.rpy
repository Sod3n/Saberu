
init python:
    dictionary_statement = []

    is_dictionary_new_word = False
    last_word_added = -10000.0

    def add_to_dictionary(statement):
        if statement in store.dictionary_statement:
            return

        store.dictionary_statement.append(statement)
        store.is_dictionary_new_word = True
    
    def dictionary_notification_function(trans, st, at):
        if store.is_dictionary_new_word:
            store.last_word_added = st
            store.is_dictionary_new_word = False

        delay = st - store.last_word_added
        
        if delay <= 0.5:
            xpos = (1920) - int(400 * delay / 0.5)
        elif delay <= 3:
            xpos = (1920 - 400)
        elif delay <= 4:
            xpos = (1920 - 400) + int(400 * (delay - 3) / 1)
        else:
            xpos = 1920

        trans.xalign = 0.0
        trans.xpos = xpos
        return 0
    
    dictionary_notification = Transform(Image("dictionary_notification.png"), function = dictionary_notification_function)
    orange = Solid("#FAC898")


screen dictionary_screen:
    tag menu
    zorder 10
    dismiss action Hide("dictionary_screen", Dissolve(0.3))
    add "dictionart_background.png"
    window id "dictionary_window":
        background None
        modal True
        ysize 650
        xsize 1500 - 100
        xalign 0.5
        yalign 0.5
        vbox:
            text "{color=#1B1212}{size=64}{font=ofont.ru_ChinaCyr.ttf}Словарь{/font}{/size}{/color}":
                xalign 0.5
            viewport id "vp":
                draggable True
                mousewheel True
                vbox:
                    for i in store.dictionary_statement:
                        text "{color=#1B1212}{size=32}{font=Neucha-Regular.ttf}"+i+"{/font}{/size}{/color}"
                        fixed:
                            ymaximum 20

        
