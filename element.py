class Element:
    individualism_to_color = {
        "Organisation": "White",
        "Curiosity": "Blue",
        "Self-concern": "Black",
        "Emotion": "Red",
        "Instinct": "Green",
    }

    def __init__(self, individualism, color, associated_roles, associated_skills):
        self.individualism = individualism
        self.color = self.individualism_to_color[individualism]
        self.associated_roles = associated_roles
        self.associated_skills = associated_skills

    def __str__(self):
        return self.individualism

    def get_color(self):
        return self.color

    def has_role(self, role):
        return role in self.associated_roles

    def has_skill(self, skill):
        return skill in self.associated_skills

    def get_associated_roles(self):
        return self.associated_roles

    def get_associated_skills(self):
        return self.associated_skills
