class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.start = 0
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.count:
            raise StopIteration

        if not self.counter == 1:
            term = self.start + self.step
            self.start += self.step
            self.counter += 1
            return term
        else:
            self.counter += 1
            return 0
