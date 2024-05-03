from skill import Skill
from role import Role


"""
GHOST SKILLS
1. Ethereal Transposition: become intangible.
2. Frosty Touch: drains the life energy, dealing damage and slowing down the affected players.
3. Haunting Illusions: creates illusions to confuse the enemies.
4. Shadowy Curse: reduce resistance to damage or inflicting adverse effects such as weakness or confusion.
"""
etheral_transposition = Skill("Ethereal Transposition",
                              "Testemunhe o fantasma tornando-se intangível, atravessando paredes e objetos para surpreender os jogadores. Durante esse estado, o fantasma não pode ser atacado, mas também não pode atacar.",
                              0,
                              0,
                              10,
                              0)

frosty_touch = Skill("Frosty Touch",
                     "Sinta o ar gelado enquanto o fantasma drena energia vital, deixando os heróis mais lentos e vulneráveis.",
                     20,
                     0,
                     10,
                     0)

haunting_illusions = Skill("Haunting Illusions",
                           "As sombras dançam, criando visões do passado distorcido para confundir os jogadores durante o combate.",
                           0,
                           0,
                           15,
                           0)

shadowy_curse = Skill("Shadowy Curse",
                      "Um murmúrio sinistro enche o ar quando o fantasma lança sua maldição, enfraquecendo os heróis e obscurecendo sua visão com trevas.",
                      0,
                      0,
                      20,
                      0)

ghost_skills = [etheral_transposition, frosty_touch, haunting_illusions, shadowy_curse]

roles = {
    "Ghost": Role("Ghost", ghost_skills, 100, 100, 100, 0)
}