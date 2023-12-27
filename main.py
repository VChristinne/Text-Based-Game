from colorama import Fore, Style
from player import Player


def main():
    available_roles = ["Archer", "Knight", "Mage", "Assassin"]

    player = Player()
    player.choose_role(available_roles)

    print(Style.BRIGHT + Fore.BLUE + f"Nome: {player.get_username()}" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.GREEN + f"Role: {player.get_role()}" + Style.RESET_ALL)

    formatted_skills = player.get_skills()

    if formatted_skills:
        print(Style.BRIGHT + "Skills: " + Style.RESET_ALL)
        print(Style.BRIGHT + '\n'.join(formatted_skills) + Style.RESET_ALL)
    else:
        print(Fore.RED + "Classe não reconhecida. Saindo do jogo." + Fore.RESET)


if __name__ == '__main__':
    main()
