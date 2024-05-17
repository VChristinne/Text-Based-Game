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

def turn(round, begin_at, end_at):
    return {
        "round": round,
        "begin_at": begin_at,
        "end_at": end_at
    }

