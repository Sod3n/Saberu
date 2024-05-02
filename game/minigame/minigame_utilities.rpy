init -100 python:

    import random

    minigame_win_scene = "start"
    minigame_lose_scene = "start"

    minigame_actions = {
        "block": "Выставить меч перед собой",
        "dodge": "Отступить",
        "hard_hit": "Ударить в полную силу",
        "jab": "Нанести колющий удар",
        "parry": "Сделать шаг вперёд, парируя",
        "pressure_hit": "Броситься впёред",
        "short_hit": "Совершить атаку",
        "wait": "Ожидать лучшей возможности",
        "shoot": "Нанести гига атаку"
    }

    def to_tuple(action):
        return (minigame_actions[action], action)

    minigame_actions_tuple = [ 
        to_tuple("block"), 
        to_tuple("dodge"), 
        to_tuple("hard_hit"), 
        to_tuple("jab"), 
        to_tuple("parry"), 
        to_tuple("pressure_hit"), 
        to_tuple("short_hit"), 
    ]

    def perform_action_in_order(p, e):
        p.is_in_balance = True
        e.is_in_balance = True

        if p.make_move_action(e):
            player(minigame_actions[p.action])

        if e.make_move_action(p):
            enemy(minigame_actions[e.action])

        p.move_to_next_pos(e)
        if e.move_to_blocked_pos(p):
            renpy.say(narrator, "Бдышь!")

        e.move_to_next_pos(p)
        if p.move_to_blocked_pos(e):
            renpy.say(narrator, "Фшьюх!!!")

        p.move_to_next_pos(e) # if enemy push player

        if p.make_def_action(e):
            player(minigame_actions[p.action])

        if e.make_def_action(p):
            enemy(minigame_actions[e.action])

        if p.make_attack_action(e):
            player(minigame_actions[p.action])

        if not p.is_in_balance:
            store.minigame_enemy_def_success = True

        if e.make_attack_action(p):
            enemy(minigame_actions[e.action])

        p.look_at(e)
        e.look_at(p)

        p.reset_invincible()
        e.reset_invincible()
        p.off_balance_position = 0
        e.off_balance_position = 0
        p.was_pushed = False
        e.was_pushed = False

        if p.health <= 0:
            renpy.hide_screen("minigame")
            config.rollback_enabled = True
            config.hard_rollback_limit = store.minigame_saved_rollback_limit
            renpy.jump(minigame_lose_scene)

        if e.health <= 0:
            renpy.hide_screen("minigame")
            config.rollback_enabled = True
            config.hard_rollback_limit = store.minigame_saved_rollback_limit
            renpy.jump(minigame_win_scene)


    def random_action(p, e):
        return random.choice(filter_actions(minigame_actions_tuple, p, e))[1]

    def filter_actions(actions, character, e):
        filtered_actions = []
        for action_tuple in actions:
            if character.can_perform_action(action_tuple[1], e):
                filtered_actions.append(action_tuple)

        if len(filtered_actions) == 0:
            filtered_actions.append(to_tuple("wait"))

        return filtered_actions
    
    is_show_next_actions = False

    def show_next_actions(action):
        print("HOVERED")
        if store.is_show_next_actions == False:
            store.is_show_next_actions = True
    
    def hide_next_actions(action):
        print("UNHOVERED")
        if store.is_show_next_actions == True:
            store.is_show_next_actions = False


    def get_actions_after_action(action):
        if action == "short_hit":
            return [ 
                to_tuple("block"), 
                to_tuple("dodge"), 
                to_tuple("jab"), 
            ]

        if action == "parry":
            return [ 
                to_tuple("jab"), 
                to_tuple("pressure_hit"), 
                to_tuple("short_hit"),
            ]
        
        if action == "pressure_hit":
            return [ 
                to_tuple("dodge"), 
                to_tuple("parry"), 
                to_tuple("short_hit"), 
            ]

        if action == "jab":
            return [ 
                to_tuple("parry"), 
                to_tuple("pressure_hit"), 
                to_tuple("short_hit"), 
            ]

        if action == "hard_hit":
            return [ 
                to_tuple("block"), 
                to_tuple("jab"), 
                to_tuple("parry"), 
            ]

        if action == "dodge":
            return [ 
                to_tuple("block"), 
                to_tuple("jab"), 
                to_tuple("pressure_hit"), 
            ]
        
        if action == "block":
            return [ 
                to_tuple("hard_hit"), 
                to_tuple("jab"), 
                to_tuple("parry"), 
            ]

        if action == "wait":
            return [ 
                to_tuple("block"), 
                to_tuple("pressure_hit"), 
                to_tuple("short_hit"), 
            ]

    