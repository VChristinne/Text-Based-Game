from colorama import Fore


class Element:
    individualism_to_color = {
        "Organisation": Fore.YELLOW,
        "Curiosity": Fore.BLUE,
        "Self-concern": Fore.BLACK,
        "Emotion": Fore.RED,
        "Instinct": Fore.GREEN,
    }

    def __init__(self, individualism, associated_roles, associated_skills):
        self.individualism = individualism
        self.colour = self.individualism_to_color[individualism]
        self.associated_roles = associated_roles
        self.associated_skills = associated_skills

    def __str__(self):
        return f"{self.colour}{self.individualism}{Fore.RESET}"

    def get_color(self):
        return self.colour

    def has_role(self, role):
        return role in self.associated_roles

    def has_skill(self, skill):
        return skill in self.associated_skills

    def get_associated_roles(self):
        return self.associated_roles

    def get_associated_skills(self):
        return self.associated_skills
