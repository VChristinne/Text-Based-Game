class Role:
    def __init__(self, name, skills, health, mana, stamina):
        self.name = name
        self.skills = skills
        self.health = max(0, health)
        self.mana = max(0, mana)
        self.stamina = max(0, stamina)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)

    def has_skill(self, skill):
        return skill in self.skills

    def get_skill(self, index):
        if 0 <= index < len(self.skills):
            return self.skills[index]
        else:
            return None
