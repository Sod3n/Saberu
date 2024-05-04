
init python:
    dictionary_statement = []

    is_dictionary_new_word = False
    last_word_added = 6.0
    is_dictionary_showed = False

    def show_dictionary():
        if store.is_dictionary_showed:
            store.is_dictionary_showed = False
            Show("dictionary_screen")
        else:
            store.is_dictionary_showed = True
            Hide("dictionary_screen")

    def add_to_dictionary(statement):
        store.dictionary_statement.append(statement)
        store.is_dictionary_new_word = True
    
    def dictionary_notification_function(trans, st, at):
        if store.is_dictionary_new_word:
            store.last_word_added = st
            store.is_dictionary_new_word = False

        delay = st - store.last_word_added
        print(delay)
        if delay <= 0.5:
            xpos = (1920) - int(200 * delay / 0.5)
        elif delay <= 3:
            xpos = (1920 - 200)
        elif delay <= 4:
            xpos = (1920 - 200) + int(200 * (delay - 3) / 1)
        else:
            xpos = 1920

        trans.xalign = 0.0
        trans.xpos = xpos
        return 0
    
    dictionary_notification = Transform(Image("dictionary_notification.png"), function = dictionary_notification_function)
    orange = Solid("#FAC898")


screen dictionary_screen:
    tag menu
    key "dismiss" action NullAction()
    frame:
        background orange
        ysize 980
        xsize 1820
        xalign 0.5
        yalign 0.5
        viewport id "vp":
            draggable True
            mousewheel True
            vbox:
                for i in store.dictionary_statement:
                    text i

        vbar value YScrollValue("vp"):
            xalign 1.0

        
