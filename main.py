from prettytable import PrettyTable
from colorama import Fore, Style
from game_setup import roles

def role_info(role_name):
    role = roles[role_name]

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
    role = roles[role_name]
    skill = role.get_skill(skill_index - 1)

    if skill:
        print(Fore.RED + Style.BRIGHT + f"\nSkill {skill_index}:" + Fore.RESET)
        print(f"{skill.name}")
        print(f"{skill.description}")
        print(f"Damage: {skill.damage}")
        print(f"Health Cost: {skill.health_cost}")
        print(f"Stamina Cost: {skill.stamina_cost}")
        print(f"Mana Cost: {skill.mana_cost}")
        print(Style.RESET_ALL)
    else:
        print("Invalid skill index.")
        menu_role()

def menu_role():
    print(Fore.RED + Style.BRIGHT + "\nROLES AVAILABLES:" + Fore.RESET)
    for role_name in roles:
        print(role_name)
    print(Style.RESET_ALL)

    role_name = input(Fore.BLUE + Style.BRIGHT + "> Enter role name: " + Style.RESET_ALL).capitalize()
    if role_name in roles:
        role_info(role_name)
        skill_index = int(input(Fore.BLUE + Style.BRIGHT + "> Enter skill index: " + Style.RESET_ALL))
        skill_info(role_name, skill_index)
    else:
        print("Invalid role name.")
        menu_role()

def main():
    menu_role()

if __name__ == '__main__':
    main()