def round(turns):
    round_obj = {
        "turns": turns
    }
    return round_obj

def turn(round_obj, begin_at, end_at=None, total_time=None):
    turn_obj = {
        "rounds": round_obj,
        "begin_at": begin_at,
        "end_at": end_at,
        "total_time": total_time
    }
    return turn_obj

def match(players, current_turn):
    match_obj = {
        "players": players,
        "current_turn": current_turn
    }
    return match_obj

def create_board(match_obj, players, rounds):
    board_obj = {
        "matches": match_obj,
        "players": players,
        "rounds": rounds
    }
    return board_obj

def get_board(board_obj):
    return board_obj

def update_board(board, match_obj, players, turns):
    board["matches"] = match_obj
    board["players"] = players
    board["turns"] = turns
    return board

def delete_board(board):  # noqa: F841
    del board
