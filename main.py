import game_setup
from element import Element

def main():
    # game_setup.menu_role()
    individualism_list = list(Element.individualism_to_color.keys())
    print(individualism_list)

if __name__ == '__main__':
    main()
