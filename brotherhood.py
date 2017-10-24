def safe_pawns(pawns):
    safe_pawns = []
    for p in pawns:
        print (p)
        print (chr(ord(p[0])-1) + chr(ord(p[1])-1))
        if (chr(ord(p[0])-1) + chr(ord(p[1])-1)) in pawns or (chr(ord(p[0])+1) + chr(ord(p[1])-1)) in pawns:
            safe_pawns.append(p)
    return len(safe_pawns)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
