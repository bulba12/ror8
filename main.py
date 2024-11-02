class MyIterable:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1

my_iterable = MyIterable(1, 5)

for value in my_iterable:
    print(value)
