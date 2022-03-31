def make_bold(func):
    def wrapper(*args):
        text = func(*args)
        result = '<b>' + text + '</b>'
        return result
    return wrapper


def make_italic(func):
    def wrapper(*args):
        text = func(*args)
        result = '<i>' + text + '</i>'
        return result
    return wrapper


def make_underline(func):
    def wrapper(*args):
        text = func(*args)
        result = '<u>' + text + '</u>'
        return result
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f'Hello, {name}'

print(greet('Peter'))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f'Hello, {", ".join(args)}'

print(greet_all('Peter', 'George'))