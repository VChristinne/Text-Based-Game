from code.life_attributes import LifeAttributes


class Assassin(LifeAttributes):
    """
    1. Mutilate: deals critic damage to an enemy.
    2. Assassinate: instantly kills an enemy without shield with 25 health.
    3. Rapid Concealment: dodge an enemy quick attack.
    4. Death's Embrace: increases drastically damage, but loses health.
    """
    def __init__(self, health=70, max_health=70, shield=0, max_shield=0, stamina=60, max_stamina=60, mana=0, max_mana=0):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = ["Mutilate", "Assassinate", "Rapid Concealment", "Death's Embrace"]
        self.current_ability = None
