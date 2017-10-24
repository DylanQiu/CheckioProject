def checkrow(x):
    for i in x:
        if i[0] == i[1] == i[2] == "O" or i[0] == i[1] == i[2] == "X":
            return i[0]
    return "D"

def checkcol(x):
    for i in range(3):
        if x[0][i] == x[1][i] == x[2][i] == "O" or x[0][i] == x[1][i] == x[2][i] == "X":
            return x[0][i]
    return "D"

def checkcorss(x):
    if x[0][0] == x[1][1] == x[2][2] == "O" or x[0][0] == x[1][1] == x[2][2] == "X":
        return x[0][0]
    if x[0][2] == x[1][1] == x[2][0] == "O" or x[0][2] == x[1][1] == x[2][0] == "X":
        return x[0][2]
    return "D"

def checkio(game_result):
    a = checkcol(game_result)
    b = checkcorss(game_result)
    c = checkrow(game_result)
    if a != "D":
        return a
    if b != "D":
        return b
    if c != "D":
        return c
    return "D"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
