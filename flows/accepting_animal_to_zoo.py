from entitis.animal import animal
from entitis.cage import cage
from entitis.animal_food import animal_food


class accepting_animal_request:
    age: int
    name: str
    legs: int
    is_predador: bool

class accepting_animal_response:
    selected_cage: cage
    requested_animal: animal
    request_status: str

    def __str__(self):
        return f"{self.selected_cage}, {self.requested_animal}, {self.request_status}"


def accepting_animal_to_zoo(accepte_the_animal: accepting_animal_request):
    # create a new animal
    the_new_animal = animal(accepte_the_animal.age, accepte_the_animal.name, accepte_the_animal.legs, accepte_the_animal.is_predador)

    # locate a relevante cage == create a cage
    new_cage = cage(1, 4, "ami")

    # insert animal to cage
    #if we didnt find place for the animal - reject it.
    new_cage.add_animal(the_new_animal)

    # feed the animal
    the_animal_food = animal_food(False, False, 1)
    the_new_animal.feed(the_animal_food)

    response = accepting_animal_response()
    response.selected_cage = new_cage
    response.requested_animal = the_new_animal
    response.request_status = "success"


    return response
