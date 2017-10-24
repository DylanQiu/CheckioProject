# import string
#
# def checkio(num, base):
#     num_rep = {}
#     for i in string.digits:
#         num_rep[i] = ord(i)-48
#     for i in string.lowercase:
#         num_rep[i] = ord(i)-87
#
#     num = num.lower()
#     result = 0
#     count = 0
#     for i in num[::-1]:
#         if num_rep[i]>=base:
#             return -1
#         result += num_rep[i]*(base**count)
#         count += 1
#     return result

def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except:
        return -1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
