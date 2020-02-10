def is_valid(s):
    stack = []
    c_map = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c not in c_map:
            stack.append(c)
        elif not stack or c_map[c] != stack.pop():
            return False
    return not stack


def is_valid(s):
    lenth = 0
    while len(s) != lenth:
        lenth = len(s)
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return len(s) == 0


print(is_valid('(){}[[]]({[]})'))
