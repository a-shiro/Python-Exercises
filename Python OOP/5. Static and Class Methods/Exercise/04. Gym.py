from files_04_Gym.customer import Customer
from files_04_Gym.equipment import Equipment
from files_04_Gym.exercise_plan import ExercisePlan
from files_04_Gym.gym import Gym
from files_04_Gym.subscription import Subscription
from files_04_Gym.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
