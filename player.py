class Player:
    def __init__(self, username):
        self.username = username
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

    def get_username(self):
        return self.username

    def get_role(self):
        return self.role
