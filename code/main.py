import random
from colorama import Fore, Style
import life_attributes as life
import combat_attributes as combat


def main():
    player = life.LifeAttributes()
    print(Fore.BLUE + "\n### PLAYER ###")
    status(player)

    enemy = life.LifeAttributes()
    print(Fore.RED + "\n### ENEMY ###")
    status(enemy)

    player_damage_value = player_dice_roll()
    basic_combat(player, enemy, player_damage_value)


def player_dice_roll():
    """
    Player can choose between 5 dice rolls (10 to 20, 20 to 30, 30 to 40, 40 to 50, 50 to 60)
    First dice roll costs 5 stamina, second costs 10, third costs 15, fourth costs 25, fifth costs 30
    """
    print(Style.BRIGHT + Fore.MAGENTA + "\nRoll dice (10 to 20, 20 to 30, 30 to 40, 40 to 50, 50 to 60)\n" + Style.RESET_ALL)
    print(Fore.MAGENTA + "(1) - 10 to 20: 5 stamina\n" + Fore.RESET)
    print(Fore.MAGENTA + "(2) - 20 to 30: 10 stamina\n" + Fore.RESET)
    print(Fore.MAGENTA + "(3) - 30 to 40: 15 stamina\n" + Fore.RESET)
    print(Fore.MAGENTA + "(4) - 40 to 50: 25 stamina\n" + Fore.RESET)
    print(Fore.MAGENTA + "(5) - 50 to 60: 30 stamina\n" + Fore.RESET)
    player_dice = input("Choose dice: ")

    if player_dice == "1":
        player_damage_value = random.randrange(10, 20, 5)
    elif player_dice == "2":
        player_damage_value = random.randrange(20, 30, 5)
    elif player_dice == "3":
        player_damage_value = random.randrange(30, 40, 5)
    elif player_dice == "4":
        player_damage_value = random.randrange(40, 50, 5)
    elif player_dice == "5":
        player_damage_value = random.randrange(50, 60, 5)
    elif "1" < player_dice < "5":
        print("Invalid input!")
        player_dice_roll()
    return player_damage_value


def basic_combat(player, enemy, player_damage_value):
    """
    Player can only roll dice if they have enough stamina
    Player can only roll dice 20 times
    """
    for rounds in range(0, 20):
        rounds += 1
        print(Style.BRIGHT + Fore.CYAN + f"\n\n***ROUND {rounds}***" + Style.RESET_ALL)

        ### Test Combat ###
        player_attack = combat.CombatAttributes(player_damage_value)
        player_attack.attack(enemy)
        player.use_stamina(player_attack.stamina_cost())

        print(Fore.BLUE + f"Player damage: {player_attack.get_damage()}" + Fore.RESET)
        print(Fore.RED + f"Enemy health: {enemy.get_health()}" + Fore.RESET)
        print(Fore.RED + f"Enemy shield: {enemy.get_shield()}" + Fore.RESET)
        print(Fore.BLUE + f"Player stamina: {player.get_stamina()}" + Fore.RESET)

        if player.is_exhausted():
            print(Style.BRIGHT + Fore.BLUE + "\nPlayer is exhausted!\n" + Style.RESET_ALL)
            break

        if enemy.is_dead():
            print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)
            break

    '''
    rounds = 0
    while enemy.get_health() > 0:
        rounds += 1
        print(Style.BRIGHT + Fore.CYAN + f"\n\n***ROUND {rounds}***" + Style.RESET_ALL)

        ### Test Combat ###
        player_attack = combat.CombatAttributes(random.randrange(10, 60, 5))
        player_attack.attack(enemy)
        player.use_stamina(player_attack.stamina_cost())

        print(Fore.BLUE + f"Player damage: {player_attack.get_damage()}" + Fore.RESET)
        print(Fore.RED + f"Enemy health: {enemy.get_health()}" + Fore.RESET)
        print(Fore.RED + f"Enemy shield: {enemy.get_shield()}" + Fore.RESET)
        print(Fore.BLUE + f"Player stamina: {player.get_stamina()}" + Fore.RESET)

        if player.is_exhausted():
            print(Style.BRIGHT + Fore.BLUE + "\nPlayer is exhausted!\n" + Style.RESET_ALL)
            break

        if enemy.is_dead():
            print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)
            break
    '''

def status(atb):
    print("Health: " + str(atb.get_health()) + "/" + str(atb.get_max_health()))
    print("Shield: " + str(atb.get_shield()) + "/" + str(atb.get_max_shield()))
    print("Stamina: " + str(atb.get_stamina()) + "/" + str(atb.get_max_stamina()))
    print("Mana: " + str(atb.get_mana()) + "/" + str(atb.get_max_mana()))


if __name__ == '__main__':
    main()
