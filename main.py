from colorama import Fore, Style
from life_attributes import LifeAttributes
from player import Player

player_in_game = Player()
player_status = LifeAttributes()
enemy_status = LifeAttributes()


def main():
    available_roles = ["Archer", "Knight", "Mage", "Assassin"]
    player_in_game.choose_role(available_roles)

    print(Style.BRIGHT + Fore.BLUE + f"Nome: {player_in_game.get_username()}" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.GREEN + f"Role: {player_in_game.get_role()}" + Style.RESET_ALL)

    formatted_skills = player_in_game.get_skills()

    if formatted_skills:
        print(Style.BRIGHT + "Skills: " + Style.RESET_ALL)
        print(Style.BRIGHT + '\n'.join(formatted_skills) + Style.RESET_ALL)
        waves()
    else:
        print(Fore.RED + "Classe não reconhecida. Saindo do jogo." + Fore.RESET)


def waves():
    waves: int = 0
    while enemy_status.get_health() > 0:
        waves += 1
        print(Fore.BLACK + f"\n\n***WAVE {waves}***" + Fore.RESET)

        try:
            player_choice = int(input("Digite o número da habilidade desejada: ")) - 1
            selected_ability = player_in_game.get_skills()[player_choice]

            if 0 <= player_choice < len(player_in_game.get_skills()):
                print(f"Você escolheu: {selected_ability}")
            else:
                print("Escolha inválida. Tente novamente.")
        except IndexError:
            print("Entrada inválida. Digite um número.")

    print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)


if __name__ == '__main__':
    main()
