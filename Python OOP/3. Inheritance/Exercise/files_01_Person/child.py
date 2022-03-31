from files_01_Person.person import Person


class Child(Person):  # Variant 1
    pass


# class Child(Person):  # Variant 2
#     def __init__(self, name, age):
#         Person.__init__(self, name, age)


c = Child('Peter', 25)

print(c.age)
print(c.name)
