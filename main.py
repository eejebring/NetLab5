from connect import GameCom
from gameEngine import GameEngine

answer = input("Do you want to be a server y/N")
game_com = GameCom()


def start_game(allowed_moves, winning_score):
    game = GameEngine(allowed_moves, winning_score)
    print(f"Allowed moves: {game.allowed_moves}")
    while True:
        personal_move = ""
        while not game.allowed_move(personal_move):
            personal_move = input(f"{game.get_score()} Your Move:")

        game_com.send(personal_move)
        opponent_move = game_com.wait_for_response()
        print(f"Opponent's move: {game.get_name(opponent_move)}")
        print(game.play_round(personal_move, opponent_move))

        if game.has_winner():
            print(game.get_winner())
            break


def server():
    game_com.open_server()
    while True:
        try:
            allowed_moves = int(input("Enter amount of allowed moves:"))
            break
        except:
            print("Invalid number")
    while True:
        try:
            winning_score = int(input("Enter the winning score:"))
            break
        except:
            print("Invalid number")
    game_com.send(f"{allowed_moves},{winning_score}")
    return allowed_moves, winning_score


def client():
    server_ip = input("Enter ip (leave blank for local):")
    if server_ip == "":
        game_com.connect_to_server()
    else:
        game_com.connect_to_server(server_ip)
    rules = game_com.wait_for_response().split(",")
    return int(rules[0]), int(rules[1])


while True:
    if answer == "N":
        allowed_moves, winning_score = client()
        start_game(allowed_moves, winning_score)
        break
    elif answer == "y":
        allowed_moves, winning_score = server()
        start_game(allowed_moves, winning_score)
        break
    else:
        answer = input("Do you want to be a server y/N")
game_com.close()