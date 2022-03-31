# Original Code:

# from abc import abstractmethod, ABC
#
#
# class Duck(ABC):
#     pass
#
#
# class RubberDuck(Duck):
#     @staticmethod
#     def quack():
#         return "Squeek"
#
#     @staticmethod
#     def walk():
#         """Rubber duck can walk only if you move it"""
#         raise Exception('I cannot walk by myself')
#
#     @staticmethod
#     def fly():
#         """Rubber duck can fly only if you throw it"""
#         raise Exception('I cannot fly by myself')
#
#
# class RobotDuck(Duck):
#     HEIGHT = 50
#
#     def __init__(self):
#         self.height = 0
#
#     @staticmethod
#     def quack():
#         return 'Robotic quacking'
#
#     @staticmethod
#     def walk():
#         return 'Robotic walking'
#
#     def fly(self):
#         """can only fly to specific height but
#         when it reaches it starts landing automatically"""
#         if self.height == RobotDuck.HEIGHT:
#             self.land()
#         else:
#             self.height += 1
#
#     def land(self):
#         self.height = 0


# Refactored Code:


from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class LiveDuck(Duck):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class NotLiveDuck(Duck):
    @staticmethod
    @abstractmethod
    def stay_still():
        pass


class RubberDuck(NotLiveDuck):
    @staticmethod
    def quack():
        return "Squeek"

    @staticmethod
    def stay_still():
        return 'Im still...'


class RobotDuck(NotLiveDuck):
    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def stay_still():
        return 'Im still...'

    @staticmethod
    def walk():
        return 'Robotic walking'


class PondDuck(LiveDuck):
    def __init__(self, species):
        self.species = species

    @staticmethod
    def quack():
        return 'Quack Quack'

    @staticmethod
    def eat():
        return 'Im eating...'

    @staticmethod
    def walk():
        return 'Walking...'


green_duck = PondDuck('greenhead')
print(green_duck.quack())
print(green_duck.walk())
print(green_duck.eat())  # Live ducks can eat

robot_duck = RobotDuck()
print(robot_duck.quack())
print(robot_duck.walk())
print(robot_duck.eat())  # Ducks that are not alive do not need to eat

rubber_duck = RubberDuck()
print(rubber_duck.quack())
print(rubber_duck.walk())  # Robot ducks can walk but rubber can't so you
                           # create a walk method in RobotDuck class but not in RubberDuck

