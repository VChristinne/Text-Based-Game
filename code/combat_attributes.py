class CombatAttributes:
    def __init__(self, damage):
        self.damage = damage

    ### Attack ###
    def attack(self, target):
        target.take_damage(self.damage)

    def get_damage(self):
        return self.damage
