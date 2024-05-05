init:
    $ blod = ImageDissolve(im.Tile("blod.png"), 3.0, 30, reverse=False)
init:
    image smert = Solid("#980002", zorder = 10)

label lose:

    scene smert with blod:
        time 1.5
    $ renpy.pause(3.0, hard=True)

    "Вы умерли от кринжа...?"

    return