class Element:
    def __init__(self, name, individualisms, associated_roles, associated_skills):
        self.name = name
        self.individualisms = individualisms
        self.associated_roles = associated_roles
        self.associated_skills = associated_skills

    def __str__(self):
        return self.name

    def has_role(self, role):
        return role in self.associated_roles

    def has_skill(self, skill):
        return skill in self.associated_skills

    def get_individualisms(self):
        return self.individualisms

    def get_associated_roles(self):
        return self.associated_roles

    def get_associated_skills(self):
        return self.associated_skills
