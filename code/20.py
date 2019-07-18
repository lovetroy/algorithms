# def right(str):
#     d={')':'(',']':'[','}':'{'}
#     stack=None
#     for s in str:
#         if s in d:


def is_valid(string):
    length = 0
    while length != len(string):
        length = len(string)
        string = string.replace('()', '').replace('[]', '').replace('{}', '')
    if string == '':
        return True
    return False


print(is_valid('(){}[[]]({[]})'))
