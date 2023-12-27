from card_attributes import Card


class ArcherSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, critic):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.critic = critic

    def __str__(self):
        return f"{self.name}: {self.description}"


class AssassinSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, critic, speed):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.critic = critic
        self.speed = speed

    def __str__(self):
        return f"{self.name}: {self.description}"


class KnightSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, defense):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.defense = defense

    def __str__(self):
        return f"{self.name}: {self.description}"


class MageSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, bind):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.bind = bind

    def __str__(self):
        return f"{self.name}: {self.description}"
