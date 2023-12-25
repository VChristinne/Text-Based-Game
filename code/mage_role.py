from life_attributes import LifeAttributes


class Mage(LifeAttributes):
    """
    1. Soulbind: binds the soul of an enemy.
    2. Dante's Inferno: deals massive fire damage to all enemies.
    3. Quantum Surge: deals variable quantum damage to an enemy.
    4. Void Shatter: instantly kills an enemy without shield with 25 health.
    """
    def __init__(self, health=60, max_health=60, shield=0, max_shield=0, stamina=0, max_stamina=0, mana=80, max_mana=80):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = ["Soulbind", "Dante's Inferno", "Quantum Surge", "Void Shatter"]
        self.current_ability = None
