def vowel_filter(function):
    def wrapper():
        result = function()
        return [letter for letter in result if letter in 'aouei'.lower()]
    return wrapper


@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']


print(get_letters())