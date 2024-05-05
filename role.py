class Role:
    def __init__(self, name, skills, health, stamina, mana, shield):
        self.name = name
        self.skills = skills
        self.health = max(0, health)
        self.stamina = max(0, stamina)
        self.mana = max(0, mana)
        self.shield = max(0, shield)

    def __str__(self):
        return self.name

    def has_skill(self, skill):
        return skill in self.skills
