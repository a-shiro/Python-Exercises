class sequence_repeat:
    def __init__(self, text, count):
        self.text = text
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration

        current_index = self.index
        self.index += 1
        self.count -= 1
        return self.text[current_index % len(self.text)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')