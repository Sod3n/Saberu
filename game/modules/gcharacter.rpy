init -5 python:

    from enum import Enum
    import math

    class GCharacter(renpy.Displayable):

        class LookDirection(Enum):
            RIGHT = 0
            LEFT = 1

        look_direction = LookDirection.RIGHT

        health = 5

        last_position = 3
        position = 3

        off_balance_position = 0

        is_in_balance = True
        is_in_danger = False
        is_invincible_to_common_damage = False
        is_invincible_to_damage = False


        def __init__(self, size, character, position, lose_balance_character, in_danger_character, zoom = 1.0, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(GCharacter, self).__init__(**kwargs)

            self.character = renpy.displayable(character)
            self.health_image = renpy.displayable(self.get_hp_image(health = self.health))
            self.width, self.height = size
            self.position = position
            self.zoom = zoom
            self.lose_balance_character = renpy.displayable(lose_balance_character)
            self.in_danger_character = renpy.displayable(in_danger_character)

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
            ht.xanchor = 0.5
            ht.yanchor = 0.5

            # Create a render from the health_image.
            health_image_render = renpy.render(ht, width, height, st, at)

            # Get the size of the health_image.
            self.width, self.height = health_image_render.get_size()

            if not self.is_in_balance:
                ct = Transform(child=self.lose_balance_character)
            elif self.is_in_danger:
                ct = Transform(child=self.in_danger_character)
            else:
                ct = Transform(child=self.character)
            
            ct.zoom = self.zoom
            ct.xanchor = 0.5
            ct.yanchor = 0.5

            if(self.look_direction == GCharacter.LookDirection.LEFT):
                ct.xzoom = -1.0

            character_render = renpy.render(ct, width, height, st, at)

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the health_image's render to our render.
            render.blit(health_image_render, self.current_position)

            x, y = self.current_position
            # Blit (draw) the health_image's render to our render.
            render.blit(character_render, (x - 100 * self.zoom, y + 70 * self.zoom))
            
            # Return the render.
            return render
        
        last_time = 0.0
        delta = 0.0
        timer = 1.0
        last_health = 5

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
            x, y = positions[self.position]
            lx, ly = positions[self.last_position]
            
            if self.position != self.current_position:
                dx = x - cx
                dy = y - cy
                cx = cx + dx * 0.1
                cy = cy + dy * 0.1
                self.current_position = (cx, cy)
            else:
                self.current_position = positions[self.position]
                self.last_position = self.position

        def trigger_redraw(trans, st, at):
            return 0

        def look_at(self, character):
            if self.position < character.position:
                self.look_direction = GCharacter.LookDirection.RIGHT
            else:
                self.look_direction = GCharacter.LookDirection.LEFT

        def move(self, move_value, e):
            self.position += move_value

            if self.position == 1 or self.position == 2 or self.position == 7 or self.position == 8:
                self.is_in_danger = True
            else:
                self.is_in_danger = False
            return False

        def move_and_push(self, move_value, char_to_push):
            self.move(move_value, char_to_push)
            if char_to_push.position == self.position:
                if char_to_push.position == 8 or char_to_push.position == 1:
                    move_value = move_value * -1
                char_to_push.position += math.copysign(1, move_value)
                return True
            return False

        def move_and_push_forward(self, move_value, char_to_push):
            self.move_and_push(move_value * self.forward(), char_to_push)

        def forward(self):
            if self.look_direction == GCharacter.LookDirection.LEFT:
                return -1
            return 1

        def take_damage(self, value, is_common = True):
            if (self.is_invincible_to_common_damage and is_common) or self.is_invincible_to_damage:
                    return False
            self.health -= value
            return True

        def take_damage_at_position(self, value, position, is_common = True):
            if self.position == position:
                return self.take_damage(value)
            return False

        def common_invincible(self):
            self.is_invincible_to_common_damage = True

        def hard_invincible(self):
            self.is_invincible_to_damage = True

        def reset_invincible(self):
            self.is_invincible_to_damage = False
            self.is_invincible_to_common_damage = False

        action = None

        def make_def_action(self, e):
            if self.action == "block":
                self.common_invincible()
                return True

            if self.action == "dodge":
                self.off_balance_position = self.position
                self.move_and_push_forward(-1, e)
                return True

            if self.action == "parry":
                self.hard_invincible()
                self.move_and_push_forward(1, e)
                self.off_balance_position = self.position
                return True

            if self.action == "jab":
                self.move_and_push_forward(-1, e)
            return False
        
        def make_attack_action(self, e):
            if self.action == "hard_hit":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(2, dmg_position, False)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                return True

            if self.action == "short_hit":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True

            if self.action == "pressure_hit":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                dmg_position = self.position + 2 * self.forward()
                e.take_damage_at_position(1, dmg_position)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False

                self.move_and_push_forward(2, e)
                return True

            if self.action == "jab":
                dmg_position = self.position + 1 * self.forward()
                e.take_damage_at_position(1, dmg_position)
                if e.off_balance_position == dmg_position:
                    self.is_in_balance = False
                return True
            return False
                
        def can_perform_action(self, action):
            if action in ("hard_hit", "short_hit", "pressure_hit", "jab"):
                if not self.is_in_balance:
                    return False

            if action in ("jab", "dodge"):
                if self.is_in_danger:
                    return False
                    
            return True