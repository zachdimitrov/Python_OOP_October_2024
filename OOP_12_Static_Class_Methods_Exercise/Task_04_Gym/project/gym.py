from typing import List
from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

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
        sub = next((x for x in self.subscriptions if x.id == subscription_id), None)
        customer_id = sub.customer_id
        customer = next((x for x in self.customers if x.id == customer_id), None)
        trainer_id = sub.trainer_id
        trainer = next((x for x in self.trainers if x.id == trainer_id), None)
        exercise_id = sub.exercise_id
        exercise_plan = next((x for x in self.plans if x.id == exercise_id), None)
        equipment_id = exercise_plan.equipment_id
        equipment = next((x for x in self.equipment if x.id == equipment_id), None)

        result = f"{str(sub)}\n"
        result += f"{str(customer)}\n"
        result += f"{str(trainer)}\n"
        result += f"{str(equipment)}\n"
        result += f"{str(exercise_plan)}"
        return result
