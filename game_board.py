def match(players, current_turn):
    return {
        "players": players,
        "current_turn": current_turn
    }

def player(username, role, element):
    return {
        "username": username,
        "role": role,
        "element": element,
    }

def turn(round, begin_at, end_at=None):
    return {
        "round": round,
        "begin_at": begin_at,
        "end_at": end_at
    }

def create_board(match_obj, players, turns):
    board = {
        "match": match_obj,
        "players": players,
        "turns": turns
    }
    return board

def get_board(board):
    return board

def update_board(board, match_obj, players, turns):
    board["match"] = match_obj
    board["players"] = players
    board["turns"] = turns
    return board

def delete_board(board):
    del board