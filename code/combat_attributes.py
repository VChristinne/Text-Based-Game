import life_attributes as life


class CombatAttributes(life):
    def __init__(self, health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana, damage, defense):
        super().__init__(self, health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.damage = damage
        self.defense = defense

    ### Attack ###
    def attack(self, target):
        target.take_damage(self.damage)

    def get_damage(self):
        return self.damage

    ### Defense ###
    def defense(self, target):
        target.take_damage(self.defense)

    def get_defense(self):
        return self.defense
