from files_04_Gym.customer import Customer
from files_04_Gym.equipment import Equipment
from files_04_Gym.exercise_plan import ExercisePlan
from files_04_Gym.subscription import Subscription
from files_04_Gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = str(self.__get_obj_with_id(self.subscriptions, subscription_id))
        customer = str(self.__get_obj_with_id(self.customers, subscription_id))
        trainer = str(self.__get_obj_with_id(self.trainers, subscription_id))
        equipment = str(self.__get_obj_with_id(self.equipment, subscription_id))
        plan = str(self.__get_obj_with_id(self.plans, subscription_id))

        result = [str(el) for el in [subscription, customer, trainer, equipment, plan]]
        return '\n'.join(result)

    def __get_obj_with_id(self, list_of_objects, id):
        for obj in list_of_objects:
            if obj.id == id:
                return obj
