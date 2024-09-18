import datetime
import time
from tzlocal import get_localzone
import game_board
import game_setup


def get_local_tz():
    local_tz = get_localzone()
    current_time = datetime.datetime.now(local_tz)
    return current_time


def main():
    username, role_name, element_name = game_setup.main_menu()

    players = [game_board.player(username, role_name, element_name)]
    turn = game_board.turn(1, get_local_tz(), None)
    turns = [turn]
    match_obj = game_board.match([players], 1)

    time.sleep(20)

    turn['end_at'] = get_local_tz()
    board = game_board.create_board(match_obj, players, turns)
    game_setup.print_board(board)


if __name__ == '__main__':
    main()
