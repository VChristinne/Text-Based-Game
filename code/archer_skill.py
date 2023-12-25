from card_attributes import Card


class ArcherSkill(Card):
    def __init__(self, name, description, stamina_cost, mana_cost, damage, critic):
        super().__init__(name, description, damage, stamina_cost, mana_cost)
        self.critic = critic
