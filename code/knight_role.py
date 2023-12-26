from life_attributes import LifeAttributes
from skill_roles import KnightSkill


class Knight(LifeAttributes):
    """
    1. Charge: charges towards an enemy, dealing damage.
    2. Riposte: defensive with counter attack.
    3. Tactical Retreat: retreats from battle, restoring stamina.
    4. Berserker Rage: increases damage, but decreases defense.
    """
    def __init__(self, health=20, max_health=20, shield=100, max_shield=100, stamina=40, max_stamina=40, mana=0, max_mana=0):
        super().__init__(health, max_health, shield, max_shield, stamina, max_stamina, mana, max_mana)
        self.abilities = [
            KnightSkill("Charge of the Valiant",
                        "Investe corajosamente em direção a um inimigo, empunhando a energia dos antigos heróis. O Guerreiro, como um raio de batalha, atravessa a linha inimiga, causando dano e deixando seus oponentes atordoados pela aura guerreira.",
                        0,
                        0,
                        0,
                        False),
            KnightSkill("Riposte Shieldwall",
                        "Adota uma postura defensiva impenetrável, onde cada golpe inimigo é respondido com uma parede de escudos encantados. A counter-attack não é apenas física, mas também desencadeia uma onda de energia que enfraquece os inimigos atacantes.",
                        0,
                        0,
                        0,
                        False),
            KnightSkill("Tactical Retreat of the Enclave",
                        "Desaparece habilmente do campo de batalha por um turno, buscando refúgio nas sombras da ancestral Enclave da Sobrevivência. Durante esse tempo, a energia ancestral se manifesta, curando feridas e revigorando a estamina do Guerreiro.",
                        0,
                        0,
                        0,
                        False),
            KnightSkill("Berserker's Fury Unleashed",
                        "Em um frenesi selvagem, o Guerreiro canaliza a ira ancestral dos Berserkers. Seus ataques tornam-se devastadores, enquanto sua própria resistência física parece ignorar a dor. No entanto, essa fúria desenfreada torna-o mais vulnerável a retaliações.",
                        0,
                        0,
                        0,
                        False)
        ]
        self.current_ability = None
