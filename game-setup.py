from skill import Skill
from role import Role

charge_of_the_valiant = Skill("Charge of the Valiant", "Investe corajosamente em direção a um inimigo, empunhando a energia dos antigos heróis. O Guerreiro, como um raio de batalha, atravessa a linha inimiga, causando dano e deixando seus oponentes atordoados pela aura guerreira.")
riposte_shieldwall = Skill("Riposte Shieldwall", "Adota uma postura defensiva impenetrável, onde cada golpe inimigo é respondido com uma parede de escudos encantados. A counter-attack não é apenas física, mas também desencadeia uma onda de energia que enfraquece os inimigos atacantes.")
tactical_retreat_of_the_enclave = Skill("Tactical Retreat of the Enclave", "Desaparece habilmente do campo de batalha por um turno, buscando refúgio nas sombras da ancestral Enclave da Sobrevivência. Durante esse tempo, a energia ancestral se manifesta, curando feridas e revigorando a estamina do Guerreiro.")
berserkers_fury_unleashed = Skill("Berserker's Fury Unleashed", "Em um frenesi selvagem, o Guerreiro canaliza a ira ancestral dos Berserkers. Seus ataques tornam-se devastadores, enquanto sua própria resistência física parece ignorar a dor. No entanto, essa fúria desenfreada torna-o mais vulnerável a retaliações.")

knight_skills = [charge_of_the_valiant, riposte_shieldwall, tactical_retreat_of_the_enclave, berserkers_fury_unleashed]

roles = {
    "Knight": Role("Knight", knight_skills, 20, 0, 40, 100)
}

knight = roles["Knight"]
