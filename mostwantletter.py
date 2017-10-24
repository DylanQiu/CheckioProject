# def checkio(text):
#     if text == '':
#         return ''
#     text = text.lower()
#     text = ''.join([i for i in text if i.isalpha()])
#     text = text.replace(' ', '')
#     count_max = 0
#     count_c = text[0]
#
#
#     for c in text:
#         if text.count(c) > count_max:
#             count_max = text.count(c)
#             count_c = c
#         if text.count(c) == count_max and c < count_c:
#             count_c = c
#     return count_c

import string
def checkio(text):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
