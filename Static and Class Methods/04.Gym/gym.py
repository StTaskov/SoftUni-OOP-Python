class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscriptions):
        if subscriptions not in self.subscriptions:
            self.subscriptions.append(subscriptions)

    def subscription_info(self, subscriptions_id):
        result = ""

        subscription = None
        for subscription in self.subscriptions:
            if subscription.id == subscriptions_id:
                subscription = subscription

        result += f"{subscription}\n{repr([customer for customer in self.customers if customer.id == subscription.customer_id][0])}\n"\
                  f"{repr([trainer for trainer in self.trainers if trainer.id == subscription.trainer_id][0])}\n" \
                  f"{repr([equipment for equipment in self.equipment if equipment.id == subscription.id][0])}\n" \
                  f"{repr([plan for plan in self.plans if plan.id == subscription.exercise_id][0])}"

        return result


