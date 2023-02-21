class dictionary_iter:

    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.start = 0
        self.end = len(dict_object) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= len(self.dict_object):
            raise StopIteration()
        keys = list(self.dict_object.keys())
        values = list(self.dict_object.values())
        term = self.start
        self.start += 1
        return keys[term], values[term]