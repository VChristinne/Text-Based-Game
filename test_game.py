import unittest
from unittest.mock import patch

import game_data
from element import Element
import game_setup

class TestGame(unittest.TestCase):
    def test_menu_role(self):
        with patch('builtins.input', side_effect=['Mage', '1']):
            game_setup.menu_role()

    def test_role_info(self):
        game_setup.enemies_info('Ghost')
        game_setup.enemy_skill_info('Ghost', 1)

    def test_individualisms_list(self):
        individualism_list = list(Element.individualism_to_color.keys())
        print(individualism_list)

    def test_roles_associated_list(self):
        print(game_setup.get_associated_roles_list('Organisation', game_setup.game_data.roles))
        print(game_setup.get_associated_roles_list('Curiosity', game_setup.game_data.roles))
        print(game_setup.get_associated_roles_list('Self-concern', game_setup.game_data.roles))
        print(game_setup.get_associated_roles_list('Emotion', game_setup.game_data.roles))
        print(game_setup.get_associated_roles_list('Instinct', game_setup.game_data.roles))

    def test_skills_associated_list(self):
        skills_associated_list = game_data.elements['Organisation'].get_associated_skills()
        print(skills_associated_list)

if __name__ == '__main__':
    unittest.main(verbosity=2)
