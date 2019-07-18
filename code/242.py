def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return str2map(s) == str2map(t)


def str2map(string):
    d = {}
    for s in string:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    return d

# print(is_anagram('ab', 'ba'))
