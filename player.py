class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_health(self):
        return self.role.health

    def get_mana(self):
        return self.role.mana

    def get_stamina(self):
        return self.role.stamina

    def get_shield(self):
        return self.role.shield
