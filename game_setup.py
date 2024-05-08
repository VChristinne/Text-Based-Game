from prettytable import PrettyTable
from colorama import Fore, Style
import game_data


def role_info(role_name):
    role = game_data.roles[role_name]

    role_table = PrettyTable()
    role_table.field_names = ["Role", "Element", "Health", "Stamina", "Mana", "Shield"]
    role_table.add_row([role.name, role.element, role.health, role.stamina, role.mana, role.shield])
    print(Fore.RED + Style.BRIGHT + "\nPlayer Role Info:" + Fore.RESET)
    print(role_table)

    print(Fore.RED + Style.BRIGHT + "\nSkills:" + Fore.RESET)
    for i, skill in enumerate(role.skills, start=1):
        print(f"{i}. {skill.name}")
    print(Style.RESET_ALL)

def enemies_info(role_name):
    enemy = game_data.enemies[role_name]

    role_table = PrettyTable()
    role_table.field_names = ["Role", "Element", "Health", "Stamina", "Mana", "Shield"]
    role_table.add_row([enemy.name, enemy.element, enemy.health, enemy.stamina, enemy.mana, enemy.shield])
    print(Fore.RED + Style.BRIGHT + "\nEnemy Role Info:" + Fore.RESET)
    print(role_table)

    print(Fore.RED + Style.BRIGHT + "\nSkills:" + Fore.RESET)
    for i, skill in enumerate(enemy.skills, start=1):
        print(f"{i}. {skill.name}")
    print(Style.RESET_ALL)

def get_skill(role, index):
    if 0 <= index < len(role.skills):
        return role.skills[index]
    else:
        return None

def player_skill_info(role_name, skill_index):
    role = game_data.roles[role_name]
    skill = get_skill(role, skill_index - 1)

    if skill:
        print(Fore.RED + Style.BRIGHT + f"\nPlayer {role.name} skill {skill_index}:" + Fore.RESET)
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

def enemy_skill_info(role_name, skill_index):
    enemy = game_data.enemies[role_name]
    skill = get_skill(enemy, skill_index)

    if skill:
        print(Fore.RED + Style.BRIGHT + f"\nEnemy {enemy.name} skill {skill_index}:" + Fore.RESET)
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

def get_associated_roles_list(element_name, roles):
    element = game_data.elements[element_name]
    for role_name, role in roles.items():
        if role.element == element:
            element.associated_roles.append(role)
    return ', '.join(str(role) for role in element.associated_roles)

def get_associated_skills_list(self, index):
    if 0 <= index < len(self.associated_skills):
        return self.associated_skills[index]
    else:
        return None


def menu_role():
    print(Fore.RED + Style.BRIGHT + "\nROLES AVAILABLES:" + Fore.RESET)
    for role_name, role in game_data.roles.items():
        element = role.element
        print(f"{role_name} ({element})")
    print(Style.RESET_ALL)

    role_name = input(Fore.BLUE + Style.BRIGHT + "> Enter role name: " + Style.RESET_ALL).capitalize()
    if role_name in game_data.roles:
        role_info(role_name)
        skill_index = int(input(Fore.BLUE + Style.BRIGHT + "> Enter skill index: " + Style.RESET_ALL))
        player_skill_info(role_name, skill_index)
    else:
        print("Invalid role name.")
        menu_role()
