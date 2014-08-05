__author__ = 'Parthan'

"""Tic Tac Toe Referee

Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the spaces in
 a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal row wins
 the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result of a game
and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X"
if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D."
"""

def checkio(game_result):
    def check_win(sym):
        if game_result[0][0] == sym:
            if (game_result[0][1] == sym and game_result[0][2] == sym) or \
                    (game_result[1][0] == sym and game_result[2][0] == sym) or \
                    (game_result[1][1] == sym and game_result[2][2] == sym):
                return sym
        if game_result[2][0] == sym:
            if (game_result[2][1] == sym and game_result[2][2] == sym) or \
                    (game_result[1][1] == sym and game_result[0][2] == sym):
                return sym
        if game_result[1][1] == sym:
            if (game_result[1][0] == sym and game_result[1][2] == sym) or \
                    (game_result[0][1] == sym and game_result[2][1] == sym):
                return sym
        if game_result[0][2] == sym and game_result[1][2] == sym and game_result[2][2] == sym:
            return sym
        return ''

    return check_win('X') or check_win('O') or 'D'


if __name__ == "__main__":
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
