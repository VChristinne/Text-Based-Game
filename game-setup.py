from skill import Skill
from role import Role

"""
KNIGHT SKILLS
1. Charge: charges towards an enemy, dealing damage.
2. Riposte: defensive with counter attack.
3. Tactical Retreat: retreats from battle, restoring stamina.
4. Berserker Rage: increases damage, but decreases defense.
"""
charge_of_the_valiant = Skill("Charge of the Valiant",
                              "Investe corajosamente em direção a um inimigo, empunhando a energia dos antigos heróis. O Guerreiro, como um raio de batalha, atravessa a linha inimiga, causando dano e deixando seus oponentes atordoados pela aura guerreira.",
                              20,
                              0,
                              10,
                              0)

riposte_shieldwall = Skill("Riposte Shieldwall",
                           "Adota uma postura defensiva impenetrável, onde cada golpe inimigo é respondido com uma parede de escudos encantados. A counter-attack não é apenas física, mas também desencadeia uma onda de energia que enfraquece os inimigos atacantes.",
                           30,
                           0,
                           10,
                           0)

tactical_retreat_of_the_enclave = Skill("Tactical Retreat of the Enclave",
                                        "Desaparece habilmente do campo de batalha por um turno, buscando refúgio nas sombras da ancestral Enclave da Sobrevivência. Durante esse tempo, a energia ancestral se manifesta, curando feridas e revigorando a estamina do Guerreiro.",
                                        0,
                                        0,
                                        15,
                                        0)

berserkers_fury_unleashed = Skill("Berserker's Fury Unleashed",
                                  "Em um frenesi selvagem, o Guerreiro canaliza a ira ancestral dos Berserkers. Seus ataques tornam-se devastadores, enquanto sua própria resistência física parece ignorar a dor. No entanto, essa fúria desenfreada torna-o mais vulnerável a retaliações.",
                                  45,
                                  0,
                                  30,
                                  0)

knight_skills = [charge_of_the_valiant, riposte_shieldwall, tactical_retreat_of_the_enclave, berserkers_fury_unleashed]


"""
ARCHER SKILLS
1. Piercing Shot: pierce an enemy's shield.
2. Arcane Arrow: deals arcane damage to an enemy.
3. Arrow of Silence: silence magic abilities of an enemy.
4. Solar Flare: deals massive fire damage to an enemy.
"""
piercing_shot = Skill("Piercing Shot of Ethereal Precision",
                      "Dispara uma flecha etérea que transcende as leis da física, perfurando armaduras e ignorando as defesas físicas do inimigo.",
                      25,
                      0,
                      10,
                      0)

arcane_arrow = Skill("Arcane Arrow of Astral Mastery",
                     "Imbui uma flecha com a essência da magia arcana, tornando-a um projétil místico que causa não apenas dano físico, mas também dano mágico adicional.",
                     30,
                     0,
                     15,
                     0)

arrow_of_silence = Skill("Arrow of Silence from the Whispering Grove",
                         "Dispara uma flecha enfeitiçada que silencia a magia do inimigo, impedindo-o de conjurar feitiços por um curto período de tempo.",
                         0,
                         0,
                         20,
                         0)

solar_flare = Skill("Solar Flare Arrow from the Celestial Forge",
                         "Cria uma flecha carregada com a energia ardente do sol, que, ao atingir o alvo, irradia uma explosão de chamas solares, causando dano de fogo e cegando o inimigo por dois turnos.",
                         40,
                         0,
                         25,
                         0)

roles = {
    "Knight": Role("Knight", knight_skills, 20, 40, 0, 100),
    "Archer": Role("Archer", archer_skills, 40, 30, 40, 20)
}

knight = roles["Knight"]
archer = roles["Archer"]
