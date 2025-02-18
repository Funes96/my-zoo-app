from entitis.animal_food import animal_food
from pydantic import BaseModel

class animal():
    age: float
    name: str
    legs: int
    is_hungry: bool = True
    is_predetor: bool = False

    def __init__(self, age: int, name: str, legs: int, is_predetor: bool):
        self.age = age
        self.name = name
        self.legs = legs
        self.is_predetor = is_predetor
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Legs: {self.legs}, Hungry?: {self.is_hungry}"

    def feed(self, food: animal_food):
        if food.vegi and self.is_predetor: 
            print('This food is not for that animal')
            return
        
        self.is_hungry = False
        print("Feeding the animal")

class zebra(animal):
    def __init__(self, age: int, name: str, legs: int, is_predetor: bool, strip_count: int):
        super().__init__(age, name, legs, is_predetor)
        self.strip_count = strip_count

    def show_strip(self):
        print(f"The animal {self.name} has {self.strip_count} strips")
