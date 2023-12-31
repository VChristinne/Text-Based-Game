from colorama import Fore
from archer_role import Archer
from knight_role import Knight
from mage_role import Mage
from assassin_role import Assassin


class Player:
    def __init__(self):
        self.username = None
        self.role = None
        self.current_skill = None

    def choose_role(self, available_roles):
        while True:
            print("\nEscolha uma classe: ")
            for i, role in enumerate(available_roles):
                print(f"{i + 1}. {role}")

            # TODO: implements choice confirmation
            try:
                choice = int(input("Digite o número da classe desejada: ")) - 1

                if 0 <= choice < len(available_roles):
                    self.role = available_roles[choice]
                    break
                else:
                    print(Fore.RED + "Escolha inválida. Tente novamente." + Fore.RESET)
            except ValueError:
                print(Fore.RED + "Entrada inválida. Digite um número." + Fore.RESET)

    def get_role(self):
        return self.role

    def get_username(self):
        try:
            self.username = str(input("Digite seu username: "))
            while len(self.username) < 3:
                print(Fore.RED + "Username deve conter pelo menos 3 caracteres." + Fore.RESET)
                self.username = str(input("Digite seu username: "))
            return self.username
        except ValueError:
            print(Fore.RED + "Entrada inválida. Digite um username." + Fore.RESET)

    def get_skills(self):
        role_instance = None

        match self.role:
            case "Archer":
                role_instance = Archer()
            case "Knight":
                role_instance = Knight()
            case "Mage":
                role_instance = Mage()
            case "Assassin":
                role_instance = Assassin()
            case _:
                print(Fore.RED + "Classe não reconhecida. Saindo do jogo." + Fore.RESET)

        if role_instance:
            formatted_skills = []
            for skill in role_instance.abilities:
                formatted_skill = f"\n-> {skill.name}\n{skill.description}"

                if hasattr(skill, 'stamina_cost') and skill.stamina_cost:
                    formatted_skill += f"\n- Custo de estamina: {skill.stamina_cost}"
                if hasattr(skill, 'mana_cost') and skill.mana_cost:
                    formatted_skill += f"\n- Custo de mana: {skill.mana_cost}"
                if hasattr(skill, 'damage') and skill.damage:
                    formatted_skill += f"\n- Dano: {skill.damage}"
                if hasattr(skill, 'critic') and skill.critic:
                    formatted_skill += f"\n- Crítico: {skill.critic}"

                formatted_skills.append(formatted_skill)

            return formatted_skills
        else:
            return None
