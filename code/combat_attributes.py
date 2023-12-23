class CombatAttributes():
    def __init__(self, damage, defense):
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
