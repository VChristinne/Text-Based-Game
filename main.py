import datetime
import time
from tzlocal import get_localzone
from game import gboard, gsetup


def get_local_tz():
    local_tz = get_localzone()
    current_time = datetime.datetime.now(local_tz)
    return current_time


def main():
    while True:
        username, role_name, element_name = gsetup.main_menu()

        if username and role_name and element_name:
            players = [gboard.player(username, role_name, element_name)]
            turn = gboard.turn(1, get_local_tz(), None)
            turns = [turn]
            match_obj = gboard.match([players], 1)

            time.sleep(20)

            turn['end_at'] = get_local_tz()
            board = gboard.create_board(match_obj, players, turns)
            gsetup.print_board(board)


if __name__ == '__main__':
    main()
