from prettytable import PrettyTable
from colorama import Fore, Style
import firebase_data

def get_role(role_name):
    role = firebase_data.roles[role_name]

    role_table = PrettyTable()
    role_table.field_names = ["Role", "Element", "Health", "Stamina", "Mana", "Shield"]
    role_table.add_row([role['name'], role['element'], role['health'], role['stamina'], role['mana'], role['shield']])
    print(Fore.RED + Style.BRIGHT + "\nPlayer Role Info:" + Fore.RESET)
    print(role_table)

    print(Fore.RED + Style.BRIGHT + "\nSkills:" + Fore.RESET)
    for i, skill in enumerate(role['skills'], start=1):
        print(f"{i}. {skill['name']}")
    print(Style.RESET_ALL)

def get_element(element_name):
    element = firebase_data.elements[element_name]

    element_table = PrettyTable()
    element_table.field_names = ["Colour", "Associated Roles"]
    associated_roles = "\n".join(element['associated_roles'])
    element_table.add_row([element['colour'], associated_roles])

    print(Fore.RED + Style.BRIGHT + f"\n{element_name} Info" + Fore.RESET)
    print(element_table)
    print(Style.RESET_ALL)

def get_skill(role_name, skill_index):
    role = firebase_data.roles[role_name]
    if skill_index < len(role['skills']):
        return role['skills'][skill_index]
    return None

def get_player_skill(role_name, skill_index):
    role = firebase_data.roles[role_name]
    skill = get_skill(role_name, skill_index - 1)

    if skill:
        print(Fore.RED + Style.BRIGHT + f"\n{role['name']} skill {skill_index}:" + Fore.RESET)
        print(f"{skill['name']}\n"
              f"{skill['description']}\n"
              f"Damage: {skill['damage']}\n"
              f"Health Cost: {skill['health_cost']}\n"
              f"Stamina Cost: {skill['stamina_cost']}\n"
              f"Mana Cost: {skill['mana_cost']}")
        print(Style.RESET_ALL)
    else:
        print("Invalid skill index.")
        menu_role()

def menu_role():
    firebase_data.load_game_data()

    print(Fore.RED + Style.BRIGHT + "\nROLES AVAILABLES:" + Fore.RESET)
    for role_name, role in firebase_data.roles.items():
        print(f"{role_name}")
    print(Style.RESET_ALL)

    role_name = input(Fore.BLUE + Style.BRIGHT + "> Enter role name: " + Style.RESET_ALL).capitalize()
    if role_name in firebase_data.roles:
        get_role(role_name)
    else:
        print("Invalid role name.")
        menu_role()

def menu_element():
    firebase_data.load_game_data()

    print(Fore.RED + Style.BRIGHT + "\nELEMENTS AVAILABLES" + Fore.RESET)
    elements_list = list(firebase_data.elements.items())
    for i, (element_name, element) in enumerate(elements_list, start=1):
        print(f"{i}. {element_name}")
    print(Style.RESET_ALL)

    element_index = int(input(Fore.BLUE + Style.BRIGHT + "> Enter element index: " + Style.RESET_ALL))
    if 1 <= element_index <= len(elements_list):
        element_name = elements_list[element_index - 1][0]
        get_element(element_name)
    else:
        print("Invalid element index.")
        menu_element()

def menu_skill():
    firebase_data.load_game_data()

    print(Fore.RED + Style.BRIGHT + "\nSKILLS AVAILABLES" + Fore.RESET)
    for role_name, role in firebase_data.roles.items():
        print(Fore.MAGENTA + f"\n{role_name}" + Fore.RESET)
        for i, skill in enumerate(role['skills'], start=1):
            print(f"{i}. {skill['name']}")
    print(Style.RESET_ALL)

    role_name = input(Fore.BLUE + Style.BRIGHT + "> Enter role name: " + Style.RESET_ALL).capitalize()
    if role_name in firebase_data.roles:
        skill_index = int(input(Fore.BLUE + Style.BRIGHT + "> Enter skill index: " + Style.RESET_ALL))
        get_player_skill(role_name, skill_index)
    else:
        print("Invalid role name.")
        menu_skill()

