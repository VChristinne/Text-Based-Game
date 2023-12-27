from life_attributes import LifeAttributes
from skill_roles import ArcherSkill


class Archer(LifeAttributes):
    """
    1. Piercing Shot: pierce an enemy's shield.
    2. Arcane Arrow: deals arcane damage to an enemy.
    3. Arrow of Silence: silence magic abilities of an enemy.
    4. Solar Flare Shot: deals massive fire damage to an enemy.
    """
    def __init__(self, health=100, max_health=100, shield=100, max_shield=100, stamina=50, max_stamina=50, mana=50, max_mana=50):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = [
            ArcherSkill("Piercing Shot of Ethereal Precision",
                        "Dispara uma flecha etérea que transcende as leis da física, perfurando armaduras e ignorando as defesas físicas do inimigo.",
                        50,
                        10,
                        0,
                        0),
            ArcherSkill("Arcane Arrow of Astral Mastery",
                        "Imbui uma flecha com a essência da magia arcana, tornando-a um projétil místico que causa não apenas dano físico, mas também dano mágico adicional.",
                        20,
                        20,
                        40,
                        10),
            ArcherSkill("Arrow of Silence from the Whispering Grove",
                        "Forja uma flecha com madeira dos antigos bosques, envolvendo-a em um silêncio profundo. Ao atingir o alvo, a flecha silencia a magia inimiga, interrompendo habilidades mágicas por dois turnos.",
                        10,
                        10,
                        20,
                        0),
            ArcherSkill("Solar Flare Arrow from the Celestial Forge",
                        "Cria uma flecha carregada com a energia ardente do sol, que, ao atingir o alvo, irradia uma explosão de chamas solares, causando dano de fogo e cegando o inimigo por dois turnos.",
                        30,
                        30,
                        60,
                        10)
        ]
        self.current_ability = None
