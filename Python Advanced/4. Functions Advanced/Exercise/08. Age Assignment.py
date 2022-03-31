def age_assignment(*args, **kwargs):
    dictionary = kwargs
    result = {}
    for name in args:
        result[name] = dictionary[name[0]]
    return result


print(age_assignment('Peter', 'George', G=26, P=19))
print(age_assignment('Amy', 'Billy', 'Willy', W=36, A=22, B=61))
