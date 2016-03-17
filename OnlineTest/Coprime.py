def gcd(p, q):
    while q != 0:
        temp = q
        q = p % q
        p = temp
    return p


def relatively_prime(a, b, dictionary):
    obj = Key(a, b)
    if obj in dictionary:
        return dictionary[obj] == 1
    else:
        dictionary[obj] = gcd(a, b)
        return dictionary[obj] == 1


def coprimeCount(a):
    dictionary = dict()
    b = []
    for i in range(len(a)):
        count = 0
        for j in range(1, a[i] + 1):
            if relatively_prime(j, a[i], dictionary):
                count += 1
        b.append(count)
    return b


class Key:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y) or (self.y, self.x) == (other.y, other.x)
