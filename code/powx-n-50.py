def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    for i in range(n):
        ans = ans * x
    return ans


def my_pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return 1 / my_pow(x, -n)
    if n % 2:
        return x * my_pow(x, n - 1)
    return my_pow(x * x, n / 2)


def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    while n > 0:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1
    return ans


def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    ans = 1
    current_product = x
    while n > 0:
        if n % 2:
            ans = ans * current_product
        current_product = current_product * current_product
        n = int(2 / n)
    return ans


print(my_pow(2, 3))
