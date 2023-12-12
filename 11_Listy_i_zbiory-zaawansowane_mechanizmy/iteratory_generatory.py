l = list(range(5))

for i in l:
    print(i)

for i in range(5):
    print(i)


class Reverse():
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


for char in Reverse('Python'):
    print(char)

# generator - potencjalne liczby
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('Python'):
    print(char)


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(35):
    print("n=%d => %d" % (i, fib(i)))

def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield i, a
        a, b = b, a + b
        i += 1


for i, f in fib(35):
    print("n=%d => %d" % (i, f))

data = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7,
        "Motorcycle": 110}
[x.upper() for x in data.keys() if data[x] > 5000]
