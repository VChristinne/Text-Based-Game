from colorama import Fore


class LifeAttributes:
    def __init__(self, health=100, max_health=100, shield=100, max_shield=100, stamina=100, max_stamina=100, mana=100, max_mana=100):
        self.health: int = health
        self.max_health: int = max_health
        self.shield: int = shield
        self.max_shield: int = max_shield
        self.stamina: int = stamina
        self.max_stamina: int = max_stamina
        self.mana: int = mana
        self.max_mana: int = max_mana

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
        if self.stamina > 0:
            self.stamina -= amount
            print(Fore.WHITE + f"| {amount} stamina used       |" + Fore.RESET)
        else:
            print("Not enough stamina!")

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
