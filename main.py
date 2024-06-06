import datetime
import time

import game_board
import game_setup

def main():
    username, role_name = game_setup.main_menu()

    players = [game_board.player(username, role_name, "element")]
    turns = [game_board.turn(1, time.localtime(), time.localtime())]
    match_obj = game_board.match([players], 1)

    board = game_board.create_board(match_obj, players, turns)
    game_setup.print_board(board)

if __name__ == '__main__':
    main()
