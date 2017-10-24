import string
def checkio(data):
    if len(data) >= 10:
        digit = 0
        lower = 0
        upper = 0
        for i in data:
            if i.isdigit():
                digit += 1
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
        if digit > 0 and lower > 0 and upper > 0:
            return True
    #replace this for solution
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
