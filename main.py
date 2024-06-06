import datetime
import time
import game_board
import game_setup


def main():
    username, role_name, element_name = game_setup.main_menu()

    players = [game_board.player(username, role_name, element_name)]
    turn = game_board.turn(1, datetime.datetime.now(), None)
    turns = [turn]
    match_obj = game_board.match([players], 1)

    time.sleep(5)

    turn['end_at'] = datetime.datetime.now()
    board = game_board.create_board(match_obj, players, turns)
    game_setup.print_board(board)

if __name__ == '__main__':
    main()
