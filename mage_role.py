from life_attributes import LifeAttributes
from skill_roles import MageSkill


class Mage(LifeAttributes):
    """
    1. Soulbind: binds the soul of an enemy.
    2. Dante's Inferno: deals massive fire damage to all enemies.
    3. Quantum Surge: deals variable quantum damage to an enemy.
    4. Void Shatter: instantly kills an enemy without shield with 25 health.
    """
    def __init__(self, health=60, max_health=60, shield=0, max_shield=0, stamina=0, max_stamina=0, mana=80, max_mana=80):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = [
            MageSkill("Soulbind with the Astral Chains",
                      "Tece correntes astrais entre o mago e o inimigo, vinculando suas vidas por dois turnos. Durante esse tempo, o dano infligido ao inimigo é refletido no mago como uma forma de vínculo espiritual.",
                      0,
                      0,
                      0,
                      False),
            MageSkill("Dante's Inferno",
                      "Invoca as chamas do próprio inferno, causando uma explosão de fogo que consome tudo em seu caminho. O dano massivo é compensado pelo fato de que o mago também sofre um preço pela manipulação do fogo infernal.",
                      0,
                      0,
                      0,
                      False),
            MageSkill("Quantum Surge of Chaotic Essence",
                      "Libera uma explosão de partículas quânticas imprevisíveis, criando uma cascata de caos. O dano variável torna esta habilidade uma manifestação imprevisível da essência caótica.",
                      0,
                      0,
                      0,
                      False),
            MageSkill("Void Shatter of Cosmic Annihilation",
                      "Manipula a energia do vazio para criar uma explosão desintegradora. Este poder cósmico aniquila instantaneamente inimigos sem escudo com 25 de vida, desencadeando uma onda de energia cósmica devastadora.",
                      0,
                      0,
                      0,
                      False)
        ]
        self.current_ability = None
