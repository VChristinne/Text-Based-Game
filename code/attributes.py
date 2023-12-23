class Attributes:
    def __init__(self, health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana):
        self.health = health
        self.max_health = max_health
        self.shield = shield
        self.max_shield = max_shield
        self.stamina = stamina
        self.max_stamina = max_stamina
        self.mana = mana
        self.max_mana = max_mana

    ### Health ###
    def take_damage(self, damage):
        if self.shield > 0:
            self.shield -= damage
            if self.shield < 0:
                self.health += self.shield
                self.shield = 0
        else:
            self.health -= damage

    def heal(self, amount):
        self.health += amount

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.max_health

    ### Shield ###
    def restore_shield(self, amount):
        self.shield += amount

    def get_shield(self):
        return self.shield

    def get_max_shield(self):
        return self.max_shield

    ### Stamina ###
    def use_stamina(self, amount):
        self.stamina -= amount

    def restore_stamina(self, amount):
        self.stamina += amount

    def get_stamina(self):
        return self.stamina

    def get_max_stamina(self):
        return self.max_stamina

    ### Mana ###
    def use_mana(self, amount):
        self.mana -= amount

    def restore_mana(self, amount):
        self.mana += amount

    def get_mana(self):
        return self.mana

    def get_max_mana(self):
        return self.max_mana

    ### Status ###
    def is_alive(self):
        return self.health > 0

    def is_exhausted(self):
        return self.stamina <= 0

    def is_dead(self):
        return self.health <= 0

    def is_out_of_mana(self):
        return self.mana <= 0
