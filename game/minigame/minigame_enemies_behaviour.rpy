init -10 python:

    import random

    minigame_enemy_behaviour = 2

    minigame_used_pressure_hit_sequencly = 0
    

    minigame_enemy_def_success = False

    minigame_enemy_last_health = 0
    minigame_enemy_prepared_to_heal = False
    

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
            elif not e.is_in_danger and e.is_in_balance:
                return "jab"

        if store.minigame_enemy_behaviour == 2:
            if store.minigame_enemy_def_success and e.is_in_balance:
                store.minigame_enemy_def_success = False
                return "shoot"

            if p.distance_to(e) > 1:
                return "parry"
            elif not e.is_in_danger:
                return "dodge"

        if store.minigame_enemy_behaviour == 3:
            
            if not e.is_in_danger and p.distance_to(e) == 1:
                a = random.choice(("dodge", "dash"))
                return a

            if not e.is_in_danger and p.distance_to(e) > 1:
                return "dodge"

            return "dash"

        if store.minigame_enemy_behaviour == 4:

            e.set_crit_chance(5)

            if not e.is_in_danger and p.distance_to(e) == 1:
                e.set_crit_chance(70)
                a = random.choice(("dodge", "jab"))
                return a

            if not e.is_in_danger and p.distance_to(e) == 2:
                e.set_crit_chance(70)
                return "jab"
            
            if minigame_used_pressure_hit_sequencly < 1:
                return "pressure_hit"

            return "wait"

        if store.minigame_enemy_behaviour == 5:
            if store.minigame_enemy_prepared_to_heal and e.health == store.minigame_enemy_last_health:
                store.minigame_enemy_prepared_to_heal = False
                return "heal"

            store.minigame_enemy_prepared_to_heal = False

            if not e.is_in_danger and e.health < 3:
                store.minigame_enemy_prepared_to_heal = True
                store.minigame_enemy_last_health = e.health
                return "heal_rebound"
            
            if e.is_in_balance:
                return "counter_attack"
            elif not e.is_in_danger:
                return "heal_rebound"

            return "wait"

        if store.minigame_enemy_behaviour == 6:
            e.set_crit_chance(5)
            if e.is_in_balance:
                e.set_crit_chance(100)
                print(e.crit_chance)

            if not e.is_in_danger and p.distance_to(e) < 3:
                return "rebound"

            if (e.is_in_danger and p.distance_to(e) < 3) or p.distance_to(e) == 1:
                return "dash"

            if p.distance_to(e) >= 3:
                return "throw"

            return "wait"
            
        