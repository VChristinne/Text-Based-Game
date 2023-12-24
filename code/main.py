import random
from colorama import Fore, Style
import life_attributes as life
import combat_attributes as combat


def main():
    player = life.LifeAttributes()
    enemy = life.LifeAttributes()

    while not player.is_exhausted() and not enemy.is_dead():
        player_damage_value = player_dice_roll()
        basic_combat(player, enemy, player_damage_value)


def player_dice_roll():
    dice_options = {
        "1": (10, 20, 5),
        "2": (20, 30, 10),
        "3": (30, 40, 15),
        "4": (40, 50, 25),
        "5": (50, 60, 30)
    }

    print(Style.BRIGHT + Fore.GREEN + "\nRoll dices\n" + Style.RESET_ALL)
    print(Fore.GREEN + "\n".join(f"({key}) -> {low} to {high}: {stamina} stamina" for key, (low, high, stamina) in dice_options.items()) + Fore.RESET)
    player_dice = input("\nChoose dice: ")

    if player_dice in dice_options:
        low, high, stamina = dice_options[player_dice]
        player_damage_value = random.randrange(low, high, 2)
    else:
        print("Invalid input!")
        player_damage_value = player_dice_roll()

    return player_damage_value


def basic_combat(player, enemy, player_damage_value):
    """
    Player can only roll dice if they have enough stamina
    Player can only roll dice 20 times
    """
    rounds = 0
    while not player.is_exhausted() and not enemy.is_dead() and rounds < 20:
        rounds += 1
        print(Style.BRIGHT + Fore.CYAN + f"\n\n|       ROUND {rounds}        |" + Style.RESET_ALL)

        player_attack = combat.CombatAttributes(player_damage_value)
        player_attack.attack(enemy)
        player.use_stamina(player_attack.stamina_cost())

        print(Fore.BLUE + f"| Player damage: {player_attack.get_damage()}    |" + Fore.RESET)
        print(Fore.RED + f"| Enemy health: {enemy.get_health()}    |" + Fore.RESET)
        print(Fore.RED + f"| Enemy shield: {enemy.get_shield()}     |" + Fore.RESET)
        print(Fore.BLUE + f"| Player stamina: {player.get_stamina()}   | " + Fore.RESET)

        if player.is_exhausted():
            print(Style.BRIGHT + Fore.BLUE + "\nPlayer is exhausted!\n" + Style.RESET_ALL)
            break

        if enemy.is_dead():
            print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)
            break

        player_dice_roll()


if __name__ == '__main__':
    main()
