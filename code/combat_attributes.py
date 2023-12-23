import life_attributes as life


class CombatAttributes(life):
    def __init__(self, health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana, damage):
        super().__init__(self, health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.damage = damage

    def attack(self, target):
        target.take_damage(self.damage)

    def get_damage(self):
        return self.damage
