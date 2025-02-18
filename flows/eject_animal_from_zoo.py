from entitis.animal import animal
from entitis.cage import cage
from entitis.animal_food import animal_food
from flows.accepting_animal_to_zoo import accepting_animal_request, accepting_animal_to_zoo, accepting_animal_response


class eject_animal_request:
    age: int
    name: str
    legs: int
    is_predador: bool

class eject_animal_response:
    requested_animal: animal
    request_status: str

    def __str__(self):
        return f"{self.requested_animal}, {self.request_status}"

def eject_animal_from_zoo(zoo_list, animal_located: eject_animal_request):

# find the animal in the list

# feed the animal

# remove the animal from the zoo

    response = eject_animal_response()
    response.requested_animal = found_animal
    response.request_status = "success"
    return response