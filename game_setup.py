from prettytable import PrettyTable
from colorama import Fore, Style
import game_data


def role_info(role_name):
    role = game_data.roles[role_name]

    role_table = PrettyTable()
    role_table.field_names = ["Role", "Health", "Stamina", "Mana", "Shield"]
    role_table.add_row([role.name, role.health, role.stamina, role.mana, role.shield])
    print(Fore.RED + Style.BRIGHT + "\nRole Info:" + Fore.RESET)
    print(role_table)

    print(Fore.RED + Style.BRIGHT + "\nSkills:" + Fore.RESET)
    for i, skill in enumerate(role.skills, start=1):
        print(f"{i}. {skill.name}")
    print(Style.RESET_ALL)


def skill_info(role_name, skill_index):
    role = game_data.roles[role_name]
    skill = role.get_skill(skill_index - 1)

    if skill:
        print(Fore.RED + Style.BRIGHT + f"\nSkill {skill_index}:" + Fore.RESET)
        print(f"{skill.name}\n"
              f"{skill.description}\n"
              f"Damage: {skill.damage}\n"
              f"Health Cost: {skill.health_cost}\n"
              f"Stamina Cost: {skill.stamina_cost}\n"
              f"Mana Cost: {skill.mana_cost}")
        print(Style.RESET_ALL)
    else:
        print("Invalid skill index.")
        menu_role()


def menu_role():
    print(Fore.RED + Style.BRIGHT + "\nROLES AVAILABLES:" + Fore.RESET)
    for role_name in game_data.roles:
        print(role_name)
    print(Style.RESET_ALL)

    role_name = input(Fore.BLUE + Style.BRIGHT + "> Enter role name: " + Style.RESET_ALL).capitalize()
    if role_name in game_data.roles:
        role_info(role_name)
        skill_index = int(input(Fore.BLUE + Style.BRIGHT + "> Enter skill index: " + Style.RESET_ALL))
        skill_info(role_name, skill_index)
    else:
        print("Invalid role name.")
        menu_role()
