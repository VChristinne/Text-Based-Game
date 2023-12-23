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

    ### Test Life Attributes ###
    rounds = 0
    while enemy.get_health() > 0:
        rounds += 1
        print(Style.BRIGHT + Fore.CYAN + f"\n\n***ROUND {rounds}***" + Style.RESET_ALL)

        ### Test Combat ###
        player_attack = combat.CombatAttributes(random.randint(10, 50))
        player_attack.attack(enemy)
        player.use_stamina()

        print(Fore.BLUE + f"Player damage: {player_attack.get_damage()}" + Fore.RESET)
        print(Fore.RED + f"Enemy health: {enemy.get_health()}" + Fore.RESET)
        print(Fore.RED + f"Enemy shield: {enemy.get_shield()}" + Fore.RESET)
        print(Fore.BLUE + f"Player stamina: {player.get_stamina()}" + Fore.RESET)

        if player.is_exhausted():
            print(Style.BRIGHT + Fore.BLUE + "\nPlayer is exhausted!\n" + Style.RESET_ALL)
            break

    if enemy.get_health() <= 0:
        print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)


def status(atb):
    print("Health: " + str(atb.get_health()) + "/" + str(atb.get_max_health()))
    print("Shield: " + str(atb.get_shield()) + "/" + str(atb.get_max_shield()))
    print("Stamina: " + str(atb.get_stamina()) + "/" + str(atb.get_max_stamina()))
    print("Mana: " + str(atb.get_mana()) + "/" + str(atb.get_max_mana()))


if __name__ == '__main__':
    main()
