from dataclasses import dataclass

species_dict = {}


class SpeciesMeta:
    def __new__(cls, class_name, parents, attributes):
        print("Creating class", class_name)
        c = type(class_name, parents, attributes)
        if attributes['species']:
            species_dict[attributes['species']] = c
        return c


@dataclass
class Character:
    name: str

    # TODO: remove this field
    species: str

    status: str
    type: str
    gender: str
    origin: str
    location: str

    def get_value(self, key):
        """Gets `value` of a specified object key."""
        if key in self.__dict__:
            return self.__dict__[key]


class Human(Character, metaclass=SpeciesMeta):
    species = "Human"


class Alien(Character, metaclass=SpeciesMeta):
    species = "Alien"
