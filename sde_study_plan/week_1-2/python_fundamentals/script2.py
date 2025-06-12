import time


class Context:
    def __init__(self, data):
        self.data = data

    def __enter__(self):
        print("entering the context")
        print("data :", self.data)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting the context")


with Context("data") as context:
    print("inside the with block")


def log(func):
    def inner():
        print("inner")
        func()
        print("after")

    return inner


@log
def test():
    print("test")


test()


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


f = fib(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


class Timer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(time.time() - self.start)


with Timer() as f:
    for val in range(10):
        print()


# Custom iterator class
class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.counter = 1

    def __iter__(self):
        return self  # returns itself as an iterator

    def __next__(self):
        if self.counter > self.max:
            raise StopIteration
        else:
            current = self.counter
            self.counter += 1
            return current


# Create iterable object
counter = CountUpTo(3)

for number in counter:
    print(number)  # Outputs: 1, 2, 3


def debug_calls(func):
    def inner(*args, **kwargs):
        print("function details: ", func.__name__, args, kwargs)
        ret = func(*args, **kwargs)
        print("return val :", ret)

    return inner


@debug_calls
def test22(*args, **kwargs):
    print("tetseestsetse")
    return 15


test22(1, 2, 3, a=4, b=6)


def read_file():
    with open("script1.py") as f:
        while line := f.readline():
            yield line


for data in read_file():
    print("file data", data)


class MyRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.start, self.end, self.step = 0, args[0], 1
        elif len(args) == 2:
            self.start, self.end, self.step = args[0], args[1], 1
        elif len(args) == 3:
            self.start, self.end, self.step = args[0], args[1], args[2]

        self.data = range(self.start, self.end, self.step)
        self.leng = len(self.data)

        self.current = self.data[-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.leng:
            current = self.current
            self.index += 1
            self.current += -self.step

            return current
        else:
            raise StopIteration


for data in MyRange(1, 15, 2):
    print("data :", data)
