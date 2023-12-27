from colorama import Fore


class Player:
    def __init__(self):
        self.username = None
        self.role = None

    def choose_role(self, available_roles):
        while True:
            print("Escolha uma role: ")
            for i, role in enumerate(available_roles):
                print(f"{i + 1}. {role}")

            try:
                choice = int(input("Digite o número da role desejada: ")) - 1

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
        if self.role == 1:
            ArcherSkill.name()
        elif self.role == 2:
            return Knight.abilities()
        elif self.role == 3:
            return Mage.abilities()
        elif self.role == 4:
            return Assassin.abilities()
        else:
            return None