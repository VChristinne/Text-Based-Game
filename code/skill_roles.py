from card_attributes import Card


class ArcherSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, critic):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.critic = critic


class AssassinSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, critic, speed):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.critic = critic
        self.speed = speed


class KnightSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, defense):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.defense = defense


class MageSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, bind):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.bind = bind
