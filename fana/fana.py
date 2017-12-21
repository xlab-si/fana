ANIMALS = {
    "cat": "MEOW",
    "cow": "MOO",
    "dog": "WOOF",
}


class NoSuchAnimal(Exception):
    pass


def list_animals():
    return ANIMALS.keys()


def make_a_noise(animal):
    try:
        return ANIMALS[animal]
    except KeyError:
        raise NoSuchAnimal(animal)
