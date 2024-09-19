import unittest
from unittest.mock import patch
import gsetup
import main


class TestMenu(unittest.TestCase):
    
    def test_role_selected(self):
        inputs = ['1', 'Yuzu', 'mage', 'no']
        with patch('builtins.input', side_effect=inputs):
            print(f"\nSimulated inputs: {inputs}")
            game_setup.main_menu()
    
    
    def test_role_reselected(self):
        inputs = ['1', 'Yuzu', 'mage', 'yes', 'Yz', 'assassin', 'no']
        with patch('builtins.input', side_effect=inputs):
            print(f"\nSimulated inputs: {inputs}")
            game_setup.main_menu()
    
    
    def test_role_info(self):
        inputs = ['2', 'archer']
        with patch('builtins.input', side_effect=inputs):
            print(f"\nSimulated inputs: {inputs}")
            game_setup.main_menu()
    
            
    def test_element_info(self):
        inputs = ['3', '1']
        with patch('builtins.input', side_effect=inputs):
            print(f"\nSimulated inputs: {inputs}")
            game_setup.main_menu()
    
            
    def test_skill_info(self):
        inputs = ['4', 'ghost', '1']
        with patch('builtins.input', side_effect=inputs):
            print(f"\nSimulated inputs: {inputs}")
            game_setup.main_menu()


class TestBoard(unittest.TestCase):
    
    def test_board(self):
        inputs = ['1', 'Yuzu', 'mage', 'no']
        with patch('builtins.input', side_effect=inputs):
            print(f"\nSimulated inputs: {inputs}")
            main.main()
            

if __name__ == '__main__':
    unittest.main(verbosity=2)
