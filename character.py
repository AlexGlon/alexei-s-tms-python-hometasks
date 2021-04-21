from dataclasses import dataclass


@dataclass
class Character:
    name: str
    species: str
    status: str
    type: str
    gender: str
    origin: str
    location: str

    # def __init__(self, char_dict):
    #     self.name = char_dict['name']
    #     self.species = char_dict['species']
    #     self.status = char_dict['status']
    #     self.type = char_dict['type']
    #     self.gender = char_dict['gender']
    #     self.origin = char_dict['origin']['name']
    #     self.location = char_dict['location']['name']

    def get_value(self, key):
        """Gets `value` of a specified object key."""
        keys_dict = {
            'name': self.name,
            'species': self.species,
            'status': self.status,
            'type': self.type,
            'gender': self.gender,
            'origin': self.origin,
            'location': self.location
        }
        if key in keys_dict:
            return keys_dict[key]
