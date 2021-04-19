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

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):

        s = [s for s in self.subscriptions if s.id == subscription_id][0]
        c = [c for c in self.customers if s.customer_id == c.id][0]
        t = [t for t in self.trainers if t.id == s.trainer_id][0]
        p = [p for p in self.plans if p.id == t.id][0]
        e = [e for e in self.equipment if e.id == p.equipment_id][0]

        return f'{s}\n{c}\n{t}\n{e}\n{p}'
