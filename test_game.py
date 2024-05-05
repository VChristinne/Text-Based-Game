from unittest.mock import patch
import game_setup

class TestGame:
    def test_menu_role(self):
        with patch('builtins.input', side_effect=['Mage', '1']):
            game_setup.menu_role()

    def test_role_info(self):
        game_setup.enemies_info('Ghost')
        game_setup.enemy_skill_info('Ghost', 1)
