class Skill:
    def __init__(self, name, description, damage, health_cost, stamina_cost, mana_cost):
        self.name = name
        self.description = description
        self.damage = max(0, damage)
        self.health_cost = max(0, health_cost)
        self.stamina_cost = max(0, stamina_cost)
        self.mana_cost = max(0, mana_cost)

    def __str__(self):
        return self.name