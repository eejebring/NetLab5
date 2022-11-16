class Rule:
    def __init__(self, move_name, defeats, strike_name):
        self.move_name = move_name
        self.defeats = defeats
        self.strike_name = strike_name

    def can_defeat(self, move):
        return self.defeats.__contains__(move)

    def get_strike(self, move):
        try:
            return self.strike_name[self.defeats.index(move)]
        except:
            return self.strike_name


class GameEngine:
    rules = {
        "R": Rule("Rock", ("S", "L"), ("crushes", "crushes")),
        "P": Rule("Paper", ("R", "SP"), ("traps", "disproves")),
        "S": Rule("Scissor", ("P", "L"), ("cuts", "decapitates")),
        "L": Rule("Lizard", ("P", "SP"), ("eats", "poisons")),
        "SP": Rule("Spock", ("S", "R"), ("smashes", "vaporizes"))
    }
    possible_moves = ["R", "P", "S", "L", "SP"]

    def __init__(self, allowed_moves, win_score):
        self.allowed_moves = self.possible_moves[:allowed_moves]
        self.win_score = win_score
        self.personal_score = 0
        self.opponent_score = 0

    def play_round(self, personal_move, opponent_move):
        if self.rules[personal_move].can_defeat(opponent_move):
            self.personal_score += 1
            return f"{self.rules[personal_move].move_name} " \
                   f"{self.rules[personal_move].get_strike(opponent_move)} " \
                   f"{self.rules[opponent_move].move_name}"
        elif self.rules[opponent_move].can_defeat(personal_move):
            self.opponent_score += 1
            return f"{self.rules[opponent_move].move_name} " \
                   f"{self.rules[opponent_move].get_strike(personal_move)} " \
                   f"{self.rules[personal_move].move_name}"
        else:
            return f"Stalemate, both player played {personal_move}"

    def get_score(self):
        return self.personal_score, self.opponent_score

    def has_winner(self):
        return self.personal_score == self.win_score or self.opponent_score == self.win_score

    def get_winner(self):
        if self.personal_score == self.win_score:
            return f"You won {self.personal_score} against {self.opponent_score}"
        elif self.opponent_score == self.win_score:
            return  f"Opponent won {self.opponent_score} against {self.personal_score}"

    def allowed_move(self, move):
        return self.allowed_moves.__contains__(move)

    def get_name(self, move):
        return self.rules[move].move_name
