init -100 python:

    import random

    minigame_win_scene = "start"
    minigame_lose_scene = "start"

    minigame_actions = {
        "block": "Принять защитную стойку",
        "dodge": "Увернуться",
        "hard_hit": "Ударить в полную силу",
        "jab": "Отступить колющим ударом",
        "parry": "Сделать шаг вперёд, парируя",
        "pressure_hit": "Броситься впёред",
        "short_hit": "Свершить атаку",
        "wait": "Ожидать лучшей возможности",
        "shoot": "Нанести гига атаку",
        "dash": "Сделать рывок вперёд",
        "heal_rebound": "Отступает и начинает произносить заклинание",
        "counter_attack": "Нанести ответный удар",
        "heal_prepare": "Готовится произнести восстанавливающие заклинание",
        "heal": "Восстанавливает здоровья",
        "throw": "Выполнить бросок"
    }

    minigame_actions_past = {
        "block": "Принял защитную стойку.",
        "dodge": "Увернулся.",
        "hard_hit": "Ударил в полную силу.",
        "jab": "Отступил пронзая колющим ударом.",
        "parry": "Сделал шаг вперёд, парируя.",
        "pressure_hit": "Бросился впёред.",
        "short_hit": "Свершил атаку.",
        "wait": "Ожидает лучшей возможности.",
        "shoot": "Использовал до чёртикво нечестную атаку.",
        "dash": "Сделал рывок вперёд.",
        "heal_rebound": "Отступает и начинает произносить заклинание.",
        "rebound": "Тактически отскакивает.",
        "counter_attack": "Наносит ответный удар.",
        "heal_prepare": "Готовится произнести восстанавливающие заклинание.",
        "heal": "Восстанавливает свои силы и готов атаковать вновь.",
        "throw": "Быстро отскакивает и использует дальнию атаку."
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

        last_p_in_danger = p.is_in_danger
        last_e_in_danger = e.is_in_danger

        p.last_stable_position = p.position
        e.last_stable_position = e.position

        p.is_last_was_crit = False
        e.is_last_was_crit = False

        if p.make_move_action(e):
            player(minigame_actions_past[p.action])

        if e.make_move_action(p):
            enemy(minigame_actions_past[e.action])

        p.move_to_next_pos(e)
        if e.move_to_blocked_pos(p):
            renpy.say(narrator, "Бдышь!")

        e.move_to_next_pos(p)
        if p.move_to_blocked_pos(e):
            renpy.say(narrator, "Фшьюх!!!")

        p.move_to_next_pos(e) # if enemy push player

        if p.is_in_danger and not last_p_in_danger:
            player("Ещё шаг назад и я труп. Надо быть осторожнее.")

        if e.is_in_danger and not last_e_in_danger:
            player("Враг прижат к стенке. Ещё чуть-чуть...")

        if p.make_def_action(e):
            player(minigame_actions_past[p.action])

        if e.make_def_action(p):
            enemy(minigame_actions_past[e.action])

        if p.make_attack_action(e):
            player(minigame_actions_past[p.action])

        if e.is_last_was_crit:
            narrator("Удар оказался сокрушительным.")

        print(store.damaged_positions)
        damaged_positions.clear()

        if e.health <= 0:
            renpy.hide_screen("minigame")
            config.rollback_enabled = True
            config.hard_rollback_limit = store.minigame_saved_rollback_limit
            renpy.block_rollback()
            renpy.jump(minigame_win_scene)
            return
            
        
        if not p.is_in_balance:
            store.minigame_enemy_def_success = True
            player("Меня выбили из равновесия. Защита - единственный оставшийся вариант.")

        if e.make_attack_action(p):
            enemy(minigame_actions_past[e.action])

        if p.is_last_was_crit:
            narrator("Удар оказался сокрушительным.")
        
        if not e.is_in_balance:
            player("Кажется, враг потерял боевой потенциал. Нельзя останавливаться на этом.")

        print(store.damaged_positions)
        damaged_positions.clear()
        
        defence_positions.clear()

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
            renpy.block_rollback()
            renpy.jump(minigame_lose_scene)
            return

        if e.health <= 0:
            renpy.hide_screen("minigame")
            config.rollback_enabled = True
            config.hard_rollback_limit = store.minigame_saved_rollback_limit
            renpy.block_rollback()
            renpy.jump(minigame_win_scene)
            return


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

    