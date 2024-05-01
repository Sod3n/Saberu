init -100 python:

    import random

    minigame_actions = {
        "block": "Выставить меч перед собой",
        "dodge": "Отступить",
        "hard_hit": "Ударить в полную силу",
        "jab": "Нанести колющий удар",
        "parry": "Сделать шаг вперёд, парируя",
        "pressure_hit": "Броситься впёред",
        "short_hit": "Совершить атаку"
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

        if p.make_def_action(e):
            player(minigame_actions[p.action])

        p.look_at(e)
        e.look_at(p)

        if e.make_def_action(p):
            enemy(minigame_actions[e.action])

        p.look_at(e)
        e.look_at(p)
        
        if p.make_attack_action(e):
            player(minigame_actions[p.action])

        if e.make_attack_action(p):
            enemy(minigame_actions[e.action])

        p.look_at(e)
        e.look_at(p)

        p.reset_invincible()
        e.reset_invincible()
        p.off_balance_position = 0
        e.off_balance_position = 0

    def random_action(e):
        return random.choice(filter_actions(minigame_actions_tuple, e))[1]

    def filter_actions(actions, character):
        filtered_actions = []
        for action_tuple in actions:
            if character.can_perform_action(action_tuple[1]):
                filtered_actions.append(action_tuple)

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

    