import unittest
from unittest.mock import patch
import game_setup

class TestGame(unittest.TestCase):
    def test_main_menu(self):
        with patch('builtins.input', side_effect=['3', 'Mage', '2']):
            game_setup.main_menu()

if __name__ == '__main__':
    unittest.main(verbosity=2)
