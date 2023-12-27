from life_attributes import LifeAttributes
from skill_roles import AssassinSkill


class Assassin(LifeAttributes):
    """
    1. Mutilate: deals critic damage to an enemy.
    2. Assassinate: instantly kills an enemy without shield with 25 health.
    3. Rapid Concealment: dodge an enemy quick attack.
    4. Death's Embrace: increases drastically damage, but loses health.
    """
    def __init__(self, health=100, max_health=100, shield=100, max_shield=100, stamina=100, max_stamina=100, mana=0, max_mana=0):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = [
            AssassinSkill("Mutilate Dance of Shadows",
                          "Dança habilmente entre as sombras, desferindo uma série rápida de ataques precisos. Cada golpe é um elo na dança mortal, culminando em um ataque crítico que deixa os inimigos desorientados.",
                          0,
                          0,
                          0,
                          0,
                          False),
            AssassinSkill("Rapid Concealment of the Phantom",
                          "Desaparece nas sombras instantaneamente, tornando-se uma sombra fugaz que escapa da visão inimiga. O retorno repentino confunde os inimigos, permitindo ao Assassino desviar dos ataques.",
                          0,
                          0,
                          0,
                          0,
                          False),
            AssassinSkill("Death’s Embrace Eternal Night",
                          "Aceita a morte como uma aliada temporária, mergulhando em uma escuridão profunda. Durante esse abraço mortal, cada golpe desferido pelo Assassino é imbuido com o poder da própria morte, infligindo dano significativo. No entanto, esse pacto sombrio cobra um preço, consumindo a própria vida do Assassino.",
                          0,
                          0,
                          0,
                          0,
                          False),
            AssassinSkill("Assassinate's Veil",
                          "Envolve a lâmina em uma aura nefasta antes de desferir um golpe letal certeiro. A lâmina, envolta na própria escuridão, corta através da resistência, eliminando instantaneamente inimigos desprotegidos com 25 de vida.",
                          30,
                          30,
                          100,
                          100,
                          False)
        ]
        self.current_ability = None
