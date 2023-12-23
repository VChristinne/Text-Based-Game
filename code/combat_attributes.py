class CombatAttributes:
    def __init__(self, damage):
        self.damage = damage

    def stamina_cost(self):
        if 10 <= self.damage <= 20:
            return 5
        elif 20 < self.damage <= 30:
            return 10
        elif 30 < self.damage <= 40:
            return 15
        elif 40 < self.damage <= 50:
            return 25
        elif 50 < self.damage <= 60:
            return 30
        else:
            return 0

    ### Attack ###
    def attack(self, target):
        target.take_damage(self.damage)

    def get_damage(self):
        return self.damage
