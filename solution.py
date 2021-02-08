

class BooleanArray:
    def __init__(self, size):
        self.array = [False] * size

    def __resize(self, size):
        new_array = [False] * (size - len(self.array))
        self.array.extend(new_array)

    # Precondition: i >= 0
    def __getitem__(self, i):
        if i >= len(self.array):
            self.__resize(2*i + 1)
        return self.array[i]

    # Precondition: i >= 0
    def __setitem__(self, i, value):
        if i >= len(self.array):
            self.__resize(2*i + 1)
        self.array[i] = value


def decimal_to_base(n, b):
    if b == 10 or n == 0:
        return str(n)
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
    notfound = True
    counting = False
    counter = 0
    pos0 = -1
    max_iterations = 10000  # in case it's not possible to find the cycle in a reasonable time
    array = BooleanArray(int(n, b))
    array[int(n, b)] = True

    while notfound or counting:
        n = lambda_algorithm(n, b)
        pos = int(n, b)

        counter += 1
        if counting:
            if pos == pos0:
                counting = False
        elif counter >= max_iterations:
            notfound = False

        if array[pos] and notfound:
            notfound = False
            counting = True
            counter = 0
            pos0 = pos
        array[pos] = True

    return counter
