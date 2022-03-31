# def log(func):
#     def wrapper():
#         print(f'{func.__name__} executed')
#         return func()
#
#     return wrapper
#
#
# @log
# def f1():
#     return 5
#
# print(f1())

# class Train:
#     TRAIN_FULL = "Train is full"
#     PASSENGER_EXISTS = "Passenger {} Exists"
#     PASSENGER_NOT_FOUND = "Passenger Not Found"
#     PASSENGER_ADD = "Added passenger {}"
#     PASSENGER_REMOVED = "Removed {}"
#     ZERO_CAPACITY = 0
#
#     def __init__(self, name: str, capacity: int):
#         self.name = name
#         self.capacity = capacity
#         self.passengers = []
#
#     def add(self, passenger_name: str) -> str:
#         if len(self.passengers) == self.capacity:
#             raise ValueError(self.TRAIN_FULL)
#
#         if passenger_name in self.passengers:
#             raise ValueError(self.PASSENGER_EXISTS.format(passenger_name))
#
#         self.passengers.append(passenger_name)
#         return self.PASSENGER_ADD.format(passenger_name)
#
#     def remove(self, passenger_name: str) -> str:
#         if passenger_name not in self.passengers:
#             raise ValueError(self.PASSENGER_NOT_FOUND.format(passenger_name))
#
#         self.passengers.remove(passenger_name)
#         return self.PASSENGER_REMOVED.format(passenger_name)
#
#
# t = Train('t1', 1)
#
# print(t.add('kiro'))
# print(t.remove('kiro'))
#
# fruits = ['apple', 'banana', 'cherry']
#
# from numbers import Number
# fruits1 = fruits[0:1]
#
# print(False < 1)


a = 5

a = 6

print (a is A)