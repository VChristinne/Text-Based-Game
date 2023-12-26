from life_attributes import LifeAttributes
from skill_roles import ArcherSkill


class Archer(LifeAttributes):
    """
    1. Piercing Shot: pierce an enemy's shield.
    2. Arcane Arrow: deals arcane damage to an enemy.
    3. Arrow of Silence: silence magic abilities of an enemy.
    4. Solar Flare Shot: deals massive fire damage to an enemy.
    """
    def __init__(self, health=40, max_health=40, shield=20, max_shield=20, stamina=30, max_stamina=30, mana=40, max_mana=40):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = [
            ArcherSkill("Piercing Shot", "", 10, 0, 10, 0),
        ]
        self.current_ability = None
