from colorama import Fore, Style
from player import Player


def main():
    available_roles = ["Archer", "Knight", "Mage", "Assassin"]

    player1 = Player("Yuzu")
    player1.choose_role(available_roles)

    print(Style.BRIGHT + Fore.BLUE + f"Nome: {player1.get_username()}" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.GREEN + f"Role: {player1.get_role()}" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
