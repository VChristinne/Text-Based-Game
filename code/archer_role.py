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
            ArcherSkill("Piercing Shot",
                        "Dispara uma flecha etérea que transcende as leis da física, perfurando armaduras e ignorando as defesas físicas do inimigo.",
                        0,
                        0,
                        0,
                        0),
            ArcherSkill("Arcane Arrow",
                        "Imbui uma flecha com a essência da magia arcana, tornando-a um projétil místico que causa não apenas dano físico, mas também dano mágico adicional.",
                        0,
                        0,
                        0,
                        0),
            ArcherSkill("Arrow of Silence",
                        "Forja uma flecha com madeira dos antigos bosques, envolvendo-a em um silêncio profundo. Ao atingir o alvo, a flecha silencia a magia inimiga, interrompendo habilidades mágicas por dois turnos.",
                        0,
                        0,
                        0,
                        0),
            ArcherSkill("Solar Flare Shot",
                        "Cria uma flecha carregada com a energia ardente do sol, que, ao atingir o alvo, irradia uma explosão de chamas solares, causando dano de fogo e cegando o inimigo por dois turnos.",
                        0,
                        0,
                        0,
                        0)
        ]
        self.current_ability = None
