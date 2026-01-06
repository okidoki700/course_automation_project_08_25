from pet import Pet
from cat import Cat

pet1 = Pet("Luna", 1, "Dog", "Ofek")
pet2 = Pet("Milo", 2, "Cat", "Dana")
pet3 = Pet("Nala", 3, "Parrot", "Avi")

my_cat = Cat("Milo", "2", "Cat", "Dana")
print(my_cat.make_sound())

cat_1 = Cat("Milo", "2", "Cat", "Dana")

pet.append(cat_1)
print(f"Milo's sound is: {cat_1.make_sound()}")

print(pet1.get_info())
print(pet2.get_info())
print(pet3.get_info())
