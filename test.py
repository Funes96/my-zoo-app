from entitis.animal import animal, zebra
from entitis.cage import cage
from entitis.animal_food import animal_food

print("animal added:")
lion = animal(2, "avram", 3, True)

print("amimal is hungry?:")
print(lion.is_hungry)
lion_food = animal_food(False, False, "meat")

lion.feed(lion_food)
print(lion.is_hungry)


print("\nanimal added")
zebra1 = zebra(5, "zebi", 4, False, 55)

print("\namimal is hungry?:")
print(zebra.is_hungry)
zebra_food = animal_food(True, False, "tomato")

zebra1.feed(zebra_food)
print(zebra1.is_hungry)

print("\nnumber of strips:")
zebra1.show_strip()

print("\ncage aded")
cage1 = cage(1, 10, "zebra cage")

print("\namimal add to cage:")
cage1.add_animal(zebra1)

print("\namimal add to cage:")
cage1.add_animal(lion)

print("\nshowing list:")
cage1.list_animals()

print("\nremove animal:")
cage1.remove_animal(lion)

print("\nshow list:")
cage1.list_animals()
