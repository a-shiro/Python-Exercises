from project.bakery import Bakery

bakery = Bakery('Bakery1')

bakery.add_food('Bread', 'White Bread', 10)
bakery.add_table('OutsideTable', 80, 3)
print(bakery.order_food(80, 'White Bread', 'White Bread', 'Brown Bread'))