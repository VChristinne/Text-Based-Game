from colorama import Fore, Style
import life_attributes as life
import combat_attributes as combat


def main():
    player = life.LifeAttributes(100, 100, 100, 100, 100, 100, 100, 100)
    print(Fore.BLUE + "\n### PLAYER ###")
    status(player)

    enemy = life.LifeAttributes(100, 100, 100, 100, 100, 100, 100, 100)
    print(Fore.RED + "\n### ENEMY ###")
    status(enemy)

    ### Test Life Attributes ###
    rounds = 0
    while enemy.get_health() > 0:
        rounds += 1
        print(Fore.BLACK + f"\n\n***ROUND {rounds}***" + Fore.RESET)

        ### Test Combat ###
        player_attack = combat.CombatAttributes(50)

        player_attack.attack(enemy)
        player.use_stamina(20)

        print(Fore.RED + f"Enemy health: {enemy.get_health()}" + Fore.RESET)
        print(Fore.RED + f"Enemy shield: {enemy.get_shield()}" + Fore.RESET)
        print(Fore.BLUE + f"Player stamina: {player.get_stamina()}" + Fore.RESET)

    print(Style.BRIGHT + Fore.GREEN + "\nEnemy defeated!\n" + Style.RESET_ALL)


def status(atb):
    print("Health: " + str(atb.get_health()) + "/" + str(atb.get_max_health()))
    print("Shield: " + str(atb.get_shield()) + "/" + str(atb.get_max_shield()))
    print("Stamina: " + str(atb.get_stamina()) + "/" + str(atb.get_max_stamina()))
    print("Mana: " + str(atb.get_mana()) + "/" + str(atb.get_max_mana()))


if __name__ == '__main__':
    main()
