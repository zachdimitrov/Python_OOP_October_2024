from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__workers_capacity = workers_capacity
        self.__animal_capacity = animal_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.__budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([s.salary for s in self.workers])
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tends = sum([t.money_for_care for t in self.animals])
        if tends <= self.__budget:
            self.__budget -= tends
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        tigers = [x for x in self.animals if x.__class__.__name__ == "Tiger"]
        lions = [x for x in self.animals if x.__class__.__name__ == "Lion"]
        cheetahs = [x for x in self.animals if x.__class__.__name__ == "Cheetah"]
        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([x.__repr__() for x in lions])
        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join([x.__repr__() for x in tigers])
        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([x.__repr__() for x in cheetahs])
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [x for x in self.workers if x.__class__.__name__ == "Keeper"]
        caretakers = [x for x in self.workers if x.__class__.__name__ == "Caretaker"]
        vets = [x for x in self.workers if x.__class__.__name__ == "Vet"]
        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([x.__repr__() for x in keepers])
        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([x.__repr__() for x in caretakers])
        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join([x.__repr__() for x in vets])
        return result


