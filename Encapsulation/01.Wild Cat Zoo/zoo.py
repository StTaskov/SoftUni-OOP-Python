class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > 0:
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                self.__animal_capacity -= 1
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum([worker.salary for worker in self.workers])
        if workers_salary <= self.__budget:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animal_care = sum([animal.money_for_care for animal in self.animals])
        if animal_care <= self.__budget:
            self.__budget -= animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def animals_status(self):

        result = f"You have {len(self.animals)} animals\n"

        lions = list(filter(lambda animal: type(animal).__name__ == "Lion", self.animals))
        tigers = list(filter(lambda animal: type(animal).__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda animal: type(animal).__name__ == "Cheetah", self.animals))

        result += f"----- {len(lions)} Lions:\n"
        result += "{}\n".format('\n'.join(list(map(lambda lion: repr(lion), lions))))
        result += f"----- {len(tigers)} Tigers:\n"
        result += "{}\n".format('\n'.join(list(map(lambda tiger: repr(tiger), tigers))))
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "{}".format('\n'.join(map(lambda cheetah: repr(cheetah), cheetahs)))

        return result

    def workers_status(self):

        result = f"You have {len(self.workers)} workers\n"

        keepers = list(filter(lambda worker: type(worker).__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda worker: type(worker).__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda worker: type(worker).__name__ == "Vet", self.workers))

        result += f"----- {len(keepers)} Keepers:\n"
        result += "{}\n".format('\n'.join(list(map(lambda keeper: repr(keeper), keepers))))
        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "{}\n".format('\n'.join(list(map(lambda caretaker: repr(caretaker), caretakers))))
        result += f"----- {len(vets)} Vets:\n"
        result += "{}".format('\n'.join(list(map(lambda vet: repr(vet), vets))))

        return result

    def profit(self, amount):
        self.__budget += amount
