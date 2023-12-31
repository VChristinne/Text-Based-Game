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


def waves():
    waves: int = 0
    while enemy_status.get_health() > 0:
        waves += 1
        print(Style.BRIGHT + Fore.BLUE + f"\n***WAVE {waves}***" + Style.RESET_ALL)

        try:
            player_choice = int(input("Digite o número da habilidade desejada: ")) - 1
            player_in_game.current_skill = player_in_game.get_skills()[player_choice]

            if 0 <= player_choice < len(player_in_game.get_skills()):
                selected_skill_info = player_in_game.current_skill
                selected_skill_lines = selected_skill_info.split('\n')

                for index in range(7):
                    display_skill_info(selected_skill_lines, index)

            else:
                print("Escolha inválida. Tente novamente.")

        except IndexError:
            print("Entrada inválida. Digite um número.")

    print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)

def display_skill_info(skill_lines, index):
    print(skill_lines[index] if index < len(skill_lines) else "")


if __name__ == '__main__':
    main()
