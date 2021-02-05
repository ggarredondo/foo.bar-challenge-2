

def decimal_to_base(n, b):
    if b == 10 or n == 0:
        str(n)
    digits = ''
    while n:
        digits += str(n % b)
        n //= b
    return digits[::-1]


def lambda_algorithm(n, b):
    k = len(n)
    string = ''.join(sorted(n))
    x = int(string[::-1], b)
    y = int(string, b)
    z = abs(x - y)
    n = decimal_to_base(z, b)
    while len(n) < k:
        n = '0' + n
    return n


# Precondition: id must represent a nonnegative integer where 2 <= k <= 9 and 2 <= b <= 10
def solution(n, b):
    return lambda_algorithm(n, b)
