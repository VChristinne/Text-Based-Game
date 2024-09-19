class Role:
    def __init__(self, name, element, skills, health, stamina, mana, shield):
        self.name = name
        self.element = element
        self.skills = skills
        self.health = max(0, health)
        self.stamina = max(0, stamina)
        self.mana = max(0, mana)
        self.shield = max(0, shield)

    def __str__(self):
        return f"Role: {self.name}, Element: {self.element}, Health: {self.health}, Stamina: {self.stamina}, Mana: {self.mana}, Shield: {self.shield}"

    def has_skill(self, skill):
        return skill in self.skills
