from colorama import Fore
from game_setup import roles

def print_role_info(role_name):
    role = roles[role_name]

    print(f"Role: {role.name}")
    print(f"Health: {role.health}")
    print(f"Stamina: {role.stamina}")
    print(f"Mana: {role.mana}")
    print(f"Shield: {role.shield}")

    for skill in role.skills:
        print(f"Skill: {skill.name}")
        print(f"Description: {skill.description}")
        print(f"Damage: {skill.damage}")
        print(f"Health Cost: {skill.health_cost}")
        print(f"Stamina Cost: {skill.stamina_cost}")
        print(f"Mana Cost: {skill.mana_cost}")

def menu_role():
    print(Fore.BLUE + "\nChoose a role:")
    for role_name in roles:
        print(role_name)
    print(Fore.RESET)

    role_name = input("Enter role name: ").capitalize()
    if role_name in roles:
        print_role_info(role_name)
    else:
        print("Invalid role name.")

def main():
    menu_role()


if __name__ == '__main__':
    main()