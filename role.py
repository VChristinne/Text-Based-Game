class Role:
    def __init__(self, name, skills, health, stamina, mana, shield):
        self.name = name
        self.skills = skills
        self.health = max(0, health)
        self.stamina = max(0, stamina)
        self.mana = max(0, mana)
        self.shield = max(0, shield)

    def has_skill(self, skill):
        return skill in self.skills

    def get_skill(self, index):
        if 0 <= index < len(self.skills):
            return self.skills[index]
        else:
            return None
