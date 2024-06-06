import time
import prettytable
from prettytable import PrettyTable
from colorama import Fore, Style
import firebase_data

def get_role(role_name):
    role = firebase_data.roles[role_name]

    role_table = PrettyTable()
    role_table.field_names = ["Role", "Element", "Health", "Stamina", "Mana", "Shield"]
    role_table.add_row([role['name'], role['element'], role['health'], role['stamina'], role['mana'], role['shield']])
    role_table.set_style(prettytable.DOUBLE_BORDER)
    print(Fore.RED + Style.BRIGHT + "\nRole Info:" + Fore.RESET)
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
    element_table.set_style(prettytable.DOUBLE_BORDER)

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
    skill_table = PrettyTable()

    if skill:
        print(Fore.RED + Style.BRIGHT + f"\n{role['name']} skill {skill_index}:" + Fore.RESET)
        skill_table.field_names = ["Name", "Description", "Damage", "Health Cost", "Stamina Cost", "Mana Cost"]
        skill_table.add_row([skill['name'], skill['description'], skill['damage'], skill['health_cost'], skill['stamina_cost'], skill['mana_cost']])
        skill_table.set_style(prettytable.DOUBLE_BORDER)
        skill_table.align = "l"
        skill_table.max_width = 50
        print(skill_table)
        print(Style.RESET_ALL)
    else:
        print("Invalid skill index.")
        menu_role()

def menu_game():
    print(Fore.GREEN + Style.BRIGHT + "\nSTARTING GAME" + Fore.RESET)
    print(Style.RESET_ALL)

    username = input(Fore.BLUE + Style.BRIGHT + "> Enter username: " + Style.RESET_ALL)
    role_name = menu_role()
    print(Fore.MAGENTA + Style.BRIGHT + f">> {username} selected {role_name} role <<" + Style.RESET_ALL)
    return username, role_name

    """
    reselect = input(Fore.BLUE + Style.BRIGHT + "\n> Want to reselect the choices? (yes/no) " + Style.RESET_ALL)
    if reselect.lower() == "yes":
        os.system("clear")
        menu_game()
    else:
        print(Fore.GREEN + "\nGame started." + Fore.RESET)
        print(Style.RESET_ALL)
    """

def menu_role():
    firebase_data.load_game_data()

    print(Fore.RED + Style.BRIGHT + "\nROLES AVAILABLES:" + Fore.RESET)
    for role_name, role in firebase_data.roles.items():
        print(f"{role_name}")
    print(Style.RESET_ALL)

    role_name = input(Fore.BLUE + Style.BRIGHT + "> Enter role name: " + Style.RESET_ALL).capitalize()
    if role_name in firebase_data.roles:
        get_role(role_name)
        return role_name
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

def menu_help():
    pass

def print_board(board):
    print("\nMatch:")
    print("  Players:")
    for player in board['match']['players'][0]:
        print(f"    Username: {player['username']}")
    print(f"  Current Turn: {board['match']['current_turn']}")

    print("\nPlayers:")
    for player in board['players']:
        print(f"  Username: {player['username']}")
        print(f"  Role: {player['role']}")
        print(f"  Element: {player['element']}")

    print("\nTurns:")
    for turn in board['turns']:
        begin_at = time.strftime("%H:%M:%S", turn['begin_at'])
        end_at = time.strftime("%H:%M:%S", turn['end_at'])
        print(f"  Round: {turn['round']}")
        print(f"  Begin At: {begin_at}")
        print(f"  End At: {end_at}")

def main_menu():
    print(Fore.RED + Style.BRIGHT + "\nMAIN MENU" + Fore.RESET)
    menu_table = PrettyTable()
    menu_table.add_column("Options", ["1", "2", "3", "4", "5", "6"])
    menu_table.add_column("Actions", ["Start game", "Role Info", "Element Info", "Skill Info", "Help", "Exit"])
    menu_table.align = "l"
    menu_table.align["Options"] = "c"
    menu_table.set_style(prettytable.DOUBLE_BORDER)
    print(menu_table)
    print(Style.RESET_ALL)

    option = int(input(Fore.BLUE + Style.BRIGHT + "> Enter option: " + Style.RESET_ALL))

    match option:
        case 1:
            return menu_game()
        case 2:
            menu_role()
        case 3:
            menu_element()
        case 4:
            menu_skill()
        case 5:
            menu_help()
        case 6:
            exit()
        case _:
            print("Invalid option.")
            return main_menu()
