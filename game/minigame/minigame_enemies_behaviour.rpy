init -10 python:

    import random

    minigame_enemy_behaviour = 2

    minigame_used_pressure_hit_sequencly = 0

    minigame_enemy_def_success = False

    def get_enemy_action(e, p):
        print(store.minigame_used_pressure_hit_sequencly)
        if store.minigame_enemy_behaviour == 0:
            if p.distance_to(e) > 1 and e.is_in_balance:
                return "short_hit"

            rand_action = random.randint(0, 5)

            if rand_action != 5 and e.is_in_balance:
                return "hard_hit"
            else:
                return "block"

        if store.minigame_enemy_behaviour == 1:
            if store.minigame_used_pressure_hit_sequencly < 2 and e.is_in_balance:
                store.minigame_used_pressure_hit_sequencly += 1
                return "pressure_hit"

            store.minigame_used_pressure_hit_sequencly = 0
            if p.distance_to(e) > 1:
                return "parry"
            elif not e.is_in_danger:
                return "jab"

        if store.minigame_enemy_behaviour == 2:
            if store.minigame_enemy_def_success and e.is_in_balance:
                store.minigame_enemy_def_success = False
                return "shoot"

            if p.distance_to(e) > 1:
                return "parry"
            elif not e.is_in_danger:
                return "dodge"