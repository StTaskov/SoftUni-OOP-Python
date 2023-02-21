class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = list(sequence)
        self.number = number
        self.start = 0
        self.term = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.number - 1:
            raise StopIteration
        if self.term == len(self.sequence) - 1:
            self.term = -1
        self.start += 1
        self.term += 1
        return self.sequence[self.term]
