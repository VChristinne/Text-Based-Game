from life_attributes import LifeAttributes


class Archer(LifeAttributes):
    """
    1. Piercing Shot: pierce an enemy's shield.
    2. Arcane Arrow: deals arcane damage to an enemy.
    3. Arrow of Silence: silence magic abilities of an enemy.
    4. Solar Flare Shot: deals massive fire damage to an enemy.
    """
    def __init__(self, health=40, max_health=40, shield=20, max_shield=20, stamina=30, max_stamina=30, mana=40, max_mana=40):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = ["Piercing Shot", "Arcane Arrow", "Arrow of Silence", "Solar Flare Shot"]
        self.ability_damage = [0, 0, 0, 0]
        self.ability_stamina_cost = [0, 0, 0, 0]
        self.ability_mana_cost = [0, 0, 0, 0]
        self.current_ability = None
