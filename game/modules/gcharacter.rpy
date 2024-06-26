init -5 python:

    from enum import Enum
    import math
    import random

    class GCharacter(renpy.Displayable):

        class LookDirection(Enum):
            RIGHT = 0
            LEFT = 1

        look_direction = LookDirection.RIGHT

        health = 5

        next_position = 3
        blocked_position = 3
        last_position = 3
        last_stable_position = 3
        position = 3

        off_balance_position = 0

        is_in_balance = True
        is_in_danger = False
        is_invincible_to_common_damage = False
        is_invincible_to_damage = False

        last_time = 0.0
        delta = 0.0
        timer = 1.0
        last_health = 5
        action = None
        
        is_last_was_crit = False
        crit_chance = 5
        is_reversed = False


        def __init__(self, size, character, position, lose_balance_character, in_danger_character, is_reversed, zoom = 1.0, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(GCharacter, self).__init__(**kwargs)

            self.character = renpy.displayable(character)
            self.health_image = renpy.displayable(self.get_hp_image(health = self.health))
            self.width, self.height = size
            self.position = position
            self.next_position = position
            self.blocked_position = position
            self.last_stable_position = position
            self.zoom = zoom
            self.lose_balance_character = renpy.displayable(lose_balance_character)
            self.in_danger_character = renpy.displayable(in_danger_character)
            self.is_reversed = is_reversed

            self.char_width, self.char_height = renpy.image_size(character)

        def render(self, width, height, st, at):
            if self.position < 1:
                self.position = 1

            if self.position > 8:
                self.position = 8

            # The health_image.
            self.health_image = renpy.displayable(self.get_hp_image(health = self.health))

            self.lerp_current_position()

            ht = Transform(child=self.health_image, function = GCharacter.trigger_redraw)

            ht.zoom = self.zoom

            # Create a render from the health_image.
            health_image_render = renpy.render(ht, width, height, st, at)
        
            lbt = Transform(child=self.lose_balance_character)

            if self.is_in_danger:
                ct = Transform(child=self.in_danger_character)
            else:
                ct = Transform(child=self.character)
            
            lbt.zoom = self.zoom
            ct.zoom = self.zoom

            if((self.look_direction == GCharacter.LookDirection.LEFT and not self.is_reversed) or (self.look_direction == GCharacter.LookDirection.RIGHT and self.is_reversed)):
                ct.xzoom = -1.0

            character_render = renpy.render(ct, width, height, st, at)
            balance_render = renpy.render(lbt, width, height, st, at)

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            x, y = self.current_position
            x -= self.char_width / 2 * self.zoom
            y -= self.char_height / 2 * self.zoom
            # Blit (draw) the health_image's render to our render.
            render.blit(health_image_render, (x + 50 * self.zoom, y - 120 * self.zoom))

            
            # Blit (draw) the health_image's render to our render.
            render.blit(character_render, (x, y))

            if not self.is_in_balance:
                render.blit(balance_render, (x, y + 200 * self.zoom))
            
            # Return the render.
            return render

        def event(self, ev, x, y, st):
            # self.delta = st - self.last_time
            # self.timer -= self.delta
            # if self.timer < 0: 
            #     self.timer = 1.0
            #     self.health -= 1
            #     renpy.redraw(self, 0)

            # self.last_time = st

            return None

        def visit(self):
            return [ self.health_image, self.character ]

        def get_hp_image(self, health):
            if health <= 0:
                return "0_hp.png"
            if health ==  1:
                return "1_hp.png"
            if health ==  2:
                return "2_hp.png"
            if health ==  3:
                return "3_hp.png"
            if health ==  4:
                return "4_hp.png"
            if health >=  5:
                return "5_hp.png"
        
        current_position = (0, 0)

        def lerp_current_position(self):
            cx, cy = self.current_position
            x, y = cell_positions[self.position]
            lx, ly = cell_positions[self.last_position]
            
            if self.position != self.current_position:
                dx = x - cx
                dy = y - cy
                cx = cx + dx * 0.1
                cy = cy + dy * 0.1
                self.current_position = (cx, cy)
            else:
                self.current_position = cell_positions[self.position]
                self.last_position = self.position

        def trigger_redraw(trans, st, at):
            return 0

        def look_at(self, character):
            if self.position < character.position:
                self.look_direction = GCharacter.LookDirection.RIGHT
            else:
                self.look_direction = GCharacter.LookDirection.LEFT

        def move(self, move_value, e):
            in_danger_before = self.is_on_danger_position()

            self.position += move_value

            is_in_danger = self.is_on_danger_position()

            if not in_danger_before and is_in_danger:
                self.is_in_balance = False
            
            self.is_in_danger = is_in_danger

            return False

        def is_on_danger_position(self):
            return self.position == 1 or self.position == 2 or self.position == 7 or self.position == 8

        def move_and_push(self, move_value, char_to_push):
            self.move(move_value, char_to_push)
            if char_to_push.next_position == self.position:
                if char_to_push.next_position == 8 or char_to_push.next_position == 1:
                    move_value = move_value * -1
                char_to_push.blocked_position = char_to_push.next_position
                char_to_push.next_position += math.copysign(1, move_value)
                return True
            return False    

        def move_and_push_forward(self, move_value, char_to_push):
            self.move_and_push(move_value * self.forward(), char_to_push)

        was_pushed = False

        def move_to_next_pos(self, e):
            if self.next_position - self.position != 0:
                if self.move_and_push(self.next_position - self.position, e):
                    e.was_pushed = True
                self.next_position = self.position
                self.blocked_position = self.position

        def move_to_blocked_pos(self, e):
            if self.blocked_position != self.next_position:
                self.move(self.blocked_position - self.position, e)
                return True
            return False
        
        def set_next_position(self, value):
            if value > 8:
                value = 8
            if value < 1:
                value = 1
            self.next_position = value
            self.blocked_position = value

        def forward(self):
            if self.look_direction == GCharacter.LookDirection.LEFT:
                return -1
            return 1

        def take_damage(self, value, is_common, e):
            if self.is_invincible_to_damage:
                    return False

            crit_rand = random.randint(0, 100)

            if crit_rand >= 100 - e.crit_chance:
                self.health -= value
                self.is_last_was_crit = True

            if self.is_invincible_to_common_damage and is_common:
                value -= 1

            self.health -= value

            return True

        def set_crit_chance(self, value):
            self.crit_chance = value

        def take_damage_at_position(self, value, position, is_common, e):
            store.damaged_positions.append(position)
            if self.position == position:
                return self.take_damage(value, is_common, e)
            return False

        def common_invincible(self):
            self.is_invincible_to_common_damage = True

        def hard_invincible(self):
            self.is_invincible_to_damage = True

        def reset_invincible(self):
            self.is_invincible_to_damage = False
            self.is_invincible_to_common_damage = False

        def make_move_action(self, e):
            if self.action == "dodge":
                self.set_next_position(self.next_position + -1 * self.forward())

            if self.action == "parry":
                self.set_next_position(self.next_position + 1 * self.forward())

            if self.action == "jab":
                self.set_next_position(self.next_position + -1 * self.forward())

            if self.action == "pressure_hit":
                self.set_next_position(self.next_position + 2 * self.forward())

            if self.action == "short_hit":
                self.set_next_position(self.next_position + 1 * self.forward())

            if self.action == "dash":
                self.set_next_position(self.next_position + 2 * self.forward())
            
            if self.action == "heal_rebound":
                self.set_next_position(self.next_position + -2 * self.forward())
                return True

            if self.action == "rebound":
                self.set_next_position(self.next_position + -2 * self.forward())
                return True

            if self.action == "counter_attack":
                self.set_next_position(self.next_position + 1 * self.forward())

            if self.action == "throw":
                self.set_next_position(self.next_position + -1 * self.forward())
                
            return False

        def make_def_action(self, e):
            if self.action == "block":
                self.common_invincible()
                return True

            if self.action == "nettle_wait":
                self.common_invincible()
                return True

            if self.action == "heal_prepare":
                return True

            if self.action == "dodge":
                self.off_balance_position = self.position + 1 * self.forward()
                defence_positions.append(self.off_balance_position)
                return True

            if self.action == "parry":
                self.hard_invincible()
                self.off_balance_position = self.position
                defence_positions.append(self.off_balance_position)
                return True

            if self.action == "dash":
                self.off_balance_position = self.last_stable_position
                defence_positions.append(self.off_balance_position)
                return True

            if self.action == "counter_attack":
                self.off_balance_position = self.last_stable_position
                defence_positions.append(self.off_balance_position)

            return False

        def make_attack_action(self, e):
            if self.action == "hard_hit":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(2, dmg_position, False, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                return True

            if self.action == "short_hit":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True

            if self.action == "nettle_attack":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True

            if self.action == "pressure_hit":
                damage_maked = False

                for i in range(int(self.last_stable_position), int(self.position), self.forward()):
                    dmg_position = i
                    if e.take_damage_at_position(1, dmg_position, True, self):
                        damage_maked = True
                    if e.off_balance_position == dmg_position:
                        self.is_in_balance = False
                
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                
                return True

            if self.action == "jab":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                dmg_position = self.position + 2 * self.forward()
                e.take_damage_at_position(1, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True

            if self.action == "shoot":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(3, dmg_position, False, self)
                dmg_position = self.position + 2 * self.forward()
                e.take_damage_at_position(3, dmg_position, False, self)
                dmg_position = self.position + 3 * self.forward()
                e.take_damage_at_position(3, dmg_position, False, self)
                return True

            if self.action == "counter_attack":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True
            
            if self.action == "heal" and e.health == store.minigame_enemy_last_health:
                self.health += 2
                return True

            if self.action == "throw":
                d = random.randint(1, 2)
                dmg_position = self.position + 3 * self.forward()
                e.take_damage_at_position(d, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                dmg_position = self.position + 4 * self.forward()
                e.take_damage_at_position(d, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                dmg_position = self.position + 5 * self.forward()
                e.take_damage_at_position(d, dmg_position, True, self)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True

            if self.action == "wait_with_sake":
                minus_cr_ch = random.randint(0, 100)
                if minus_cr_ch >= 100 - 25:
                    self.is_last_was_crit = True
                    self.health -= 4

                self.health -=1
                return True

            return False
                
        def can_perform_action(self, action, e):
            if action in ("hard_hit", "short_hit", "pressure_hit", "jab"):
                if not self.is_in_balance:
                    return False

            if action in ("jab", "dodge"):
                if self.is_in_danger:
                    return False

            if action in ("parry") and self.distance_to(e) == 1:
                return False
            
            return True

        def distance_to(self, e):
            return abs(e.position - self.position)