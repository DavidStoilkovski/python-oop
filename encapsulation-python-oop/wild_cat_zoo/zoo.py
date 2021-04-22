class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            find_worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(find_worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salaries = sum([w.salary for w in self.workers])
        if self.__budget >= sum_salaries:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_expenses = sum([a.get_needs() for a in self.animals])
        if self.__budget >= sum_expenses:
            self.__budget -= sum_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        amount_of_lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        amount_of_tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        amount_of_cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals" + '\n'
        result += f"----- {len(amount_of_lions)} Lions:" + '\n'
        result += "{}".format('\n'.join([repr(l) for l in amount_of_lions])) + '\n'
        result += f"----- {len(amount_of_tigers)} Tigers:" + '\n'
        result += "{}".format('\n'.join([repr(t) for t in amount_of_tigers])) + '\n'
        result += f"----- {len(amount_of_cheetahs)} Cheetahs:" + '\n'
        result += "{}".format('\n'.join([repr(c) for c in amount_of_cheetahs]))

        return result

    def workers_status(self):
        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers" + '\n'
        result += f"----- {len(keepers)} Keepers:" + '\n'
        result += "{}".format("\n".join([repr(k) for k in keepers])) + '\n'
        result += f"----- {len(caretakers)} Caretakers:" + '\n'
        result += "{}".format('\n'.join([repr(c) for c in caretakers])) + '\n'
        result += f"----- {len(vets)} Vets:" + '\n'
        result += "{}".format('\n'.join([repr(v) for v in vets]))

        return result