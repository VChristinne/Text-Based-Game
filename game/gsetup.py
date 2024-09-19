import os
import prettytable
from colorama import Fore, Style
from database import data


def get_role(role_name):
    role = data.get_role_by_name(role_name)
    if not role:
        print(f"Role '{role_name}' not found.")
        return

    element_name = data.get_element_name_by_id(role['element_id'])

    role_table = prettytable.PrettyTable()
    role_table.field_names = ["Role", "Element", "Health", "Stamina", "Mana", "Shield"]
    role_table.add_row([role['name'], element_name, role['health'], role["stamina"], role['mana'], role['shield']])
    role_table.set_style(prettytable.DOUBLE_BORDER)
    print(Fore.RED + Style.BRIGHT + "\nRole Info:" + Fore.RESET)
    print(role_table)

    print(Fore.RED + Style.BRIGHT + "\nSkills:" + Fore.RESET)
    skills = data.get_all_skills(role['id'])
    skill_table = prettytable.PrettyTable()
    skill_table.field_names = ["Name", "Damage", "Health Cost", "Mana Cost", "Stamina Cost"]
    for skill in skills:
        skill_table.add_row(
            [
                skill['name'], 
                skill['damage'], 
                skill['health_cost'], 
                skill['mana_cost'], 
                skill['stamina_cost'], 
            ]
        )
    skill_table.set_style(prettytable.DOUBLE_BORDER)
    print(skill_table)
    print(Style.RESET_ALL)


def get_element(element_name):
    element = data.get_element_by_name(element_name)
    if not element:
        print("Element not found.")
        return

    element_table = prettytable.PrettyTable()
    element_table.field_names = ["Colour", "Associated Roles"]
    associated_roles = "\n".join(element['associated_roles'])
    element_table.add_row([element['colour'], associated_roles])
    element_table.set_style(prettytable.DOUBLE_BORDER)

    print(Fore.RED + Style.BRIGHT + f"\n{element_name} Info" + Fore.RESET)
    print(element_table)
    print(Style.RESET_ALL)


def get_player_skill(role_name, skill_index):
    role = data.get_role_by_name(role_name)
    if not role:
        print("Role not found.")
        return

    skills = data.get_all_skills(role['id'])
    if 0 < skill_index <= len(skills):
        skill = skills[skill_index - 1]
        skill_table = prettytable.PrettyTable()
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
        menu_skill()


def menu_game():
    print(Fore.GREEN + Style.BRIGHT + "\nSTARTING GAME" + Fore.RESET)
    print(Style.RESET_ALL)

    username = input(Fore.BLUE + Style.BRIGHT + "> Enter username: " + Style.RESET_ALL)
    role = menu_role()
    if not role:
        return None, None, None

    element_name = data.get_element_name_by_id(role['element_id'])
    print(Fore.MAGENTA + Style.BRIGHT + f">> {username} selected {role['name']} role <<" + Style.RESET_ALL)

    reselect = input(Fore.BLUE + Style.BRIGHT + "\n> Want to reselect the choices? (yes/no) " + Style.RESET_ALL)
    if reselect.lower() == "yes":
        os.system("clear")
        return menu_game()
    else:
        os.system("clear")
        print(Fore.GREEN + "\nGame started." + Fore.RESET)
        print(Style.RESET_ALL)

    return username, role['name'], element_name


def menu_role():
    roles = data.get_all_roles()

    print(Fore.RED+Style.BRIGHT+"\nROLES AVAILABLES:"+Fore.RESET)
    for role in roles:
        print(role['name'])

    role_name = input(Fore.BLUE+Style.BRIGHT+"\n> Enter role name: "+Style.RESET_ALL).capitalize()
    role = data.get_role_by_name(role_name)
    if role:
        get_role(role_name)
    else:
        print("Invalid role name.")
    return


def menu_element():
    elements = data.get_all_elements()

    print(Fore.RED+Style.BRIGHT+"\nELEMENTS AVAILABLES"+Fore.RESET)
    for element in elements:
        print(element['name'])

    element_name = input(Fore.BLUE+Style.BRIGHT+"\n> Enter element name: "+Style.RESET_ALL).capitalize()
    element = data.get_element_by_name(element_name)
    if element:
        get_element(element_name)
    else:
        print("Invalid element name.")
    return


def menu_skill():
    roles = data.get_all_roles()

    print(Fore.RED+Style.BRIGHT+"\nSKILLS AVAILABLES"+Fore.RESET)
    for role in roles:
        print(Fore.MAGENTA+f"\n{role['name']}"+Fore.RESET)
        skills = data.get_all_skills(role['id'])
        for i, skill in enumerate(skills, start=1):
            print(f"{i}. {skill['name']}")

    role_name = input(Fore.BLUE+Style.BRIGHT+"\n> Enter role name: "+Style.RESET_ALL).capitalize()
    role = data.get_role_by_name(role_name)
    if role:
        skill_index = int(input(Fore.BLUE+Style.BRIGHT+"\n> Enter skill index: "+Style.RESET_ALL))
        get_player_skill(role_name, skill_index)
    else:
        print("Invalid role name.")
    return


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
        begin_at = turn['begin_at'].strftime("%I:%M:%S %p")
        end_at = turn['end_at'].strftime("%I:%M:%S %p") if turn['end_at'] else None
        print(f"  Round: {turn['round']}")
        print(f"  Begin At: {begin_at}")
        print(f"  End At: {end_at}")


def main_menu():
    print(Fore.RED+Style.BRIGHT+"\nMAIN MENU"+Fore.RESET)
    menu_table = prettytable.PrettyTable()
    menu_table.add_column("Options", ["1", "2", "3", "4", "5", "6"])
    menu_table.add_column("Actions", ["Start game", "Role Info", "Element Info", "Skill Info", "Help", "Exit"])
    menu_table.align = "l"
    menu_table.align["Options"] = "c"
    menu_table.set_style(prettytable.DOUBLE_BORDER)
    print(menu_table)
    print(Style.RESET_ALL)

    option = int(input(Fore.BLUE+Style.BRIGHT+"> Enter option: "+Style.RESET_ALL))

    match option:
        case 1:
            os.system("clear")
            return menu_game()
        case 2:
            menu_role()
            return main_menu()
        case 3:
            menu_element()
            return main_menu()
        case 4:
            menu_skill()
            return main_menu()
        case 5:
            menu_help()
            return main_menu()
        case 6:
            exit()
        case _:
            print("Invalid option.")
            return main_menu()
