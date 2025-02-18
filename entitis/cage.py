from entitis.animal import animal
from pydantic import BaseModel


class cage:
    id: int
    size: int
    open_close: bool = True
    name: str
    animals_list = []
    cage_list = []




    def __init__(self, id: int, size: int, name: str):
        self.id = id
        self.size = size
        self.name = name

    def __str__(self):
        return f"{self.id}, {self.size}, {self.name}"


    def add_animal(self, animal_to_add: animal):
        for animal_item in self.animals_list:
            animal_in_cage: animal = animal_item
            if animal_in_cage.is_predetor and not animal_to_add.is_predetor:
                print(f"This animal: {animal_to_add.name}, cant be with {animal_in_cage.name}.")
                return
            if not animal_in_cage.is_predetor and animal_to_add.is_predetor:
                print(f"This animal: {animal_to_add.name}, cant be with {animal_in_cage.name}.")
                return
        #print(f"Adding animal: {animal_to_add.name} to cage: {self.name}")
        self.animals_list.append(animal_to_add)
        return {f"Adding animal: {animal_to_add.name} to cage: {self.name}"}


    def remove_animal(self, animal_to_remomve: animal):
            if animal_to_remomve not in self.animals_list:
                print(f"This animal: {animal_to_remomve.name}, is not in the cage.")
                return

            self.animals_list.remove(animal_to_remomve)
            print(f"The animal {animal_to_remomve}, has been remove from the cage.")


    def list_animals(self):
        for animal in self.animals_list:
            print(animal)