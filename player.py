from colorama import Fore
from archer_role import Archer
from knight_role import Knight
from mage_role import Mage
from assassin_role import Assassin


class Player:
    def __init__(self):
        self.username = None
        self.role = None

    def choose_role(self, available_roles):
        while True:
            print("\nEscolha uma classe: ")
            for i, role in enumerate(available_roles):
                print(f"{i + 1}. {role}")

            try:
                choice = int(input("Digite o número da classe desejada: ")) - 1

                if 0 <= choice < len(available_roles):
                    self.role = available_roles[choice]
                    break
                else:
                    print("Escolha inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

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

        if self.role == "Archer":
            role_instance = Archer()
        elif self.role == "Knight":
            role_instance = Knight()
        elif self.role == "Mage":
            role_instance = Mage()
        elif self.role == "Assassin":
            role_instance = Assassin()

        if role_instance:
            return [f"-> {skill.name}: \n{skill.description}\n" for skill in role_instance.abilities]
        else:
            return None
