class vowels:
    def __init__(self, text):
        self.text = text
        self.all_vowels = 'AEIUYOaeiuyo'
        self.vowels_list = self.__get_vowels()
        self.start = 0
        self.end = len(self.vowels_list) - 1

    def __get_vowels(self):
        vowels_list = []

        for char in self.text:
            if char in self.all_vowels:
                vowels_list.append(char)
        return vowels_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        current_char = self.start
        self.start += 1

        return self.vowels_list[current_char]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)