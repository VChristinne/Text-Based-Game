from life_attributes import LifeAttributes


class Knight(LifeAttributes):
    """
    1. Charge: charges towards an enemy, dealing damage.
    2. Riposte: defensive with counter attack.
    3. Tactical Retreat: retreats from battle, restoring stamina.
    4. Berserker Rage: increases damage, but decreases defense.
    """
    def __init__(self, health=20, max_health=20, shield=100, max_shield=100, stamina=40, max_stamina=40, mana=0, max_mana=0):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = ["Charge", "Riposte", "Tactical Retreat", "Berserker Rage"]
        self.ability_damage = [30, 20, 0, 50]
        self.ability_stamina_cost = [10, 20, 30, 40]
        self.current_ability = None
