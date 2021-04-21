import file_processing


class Character:
    def __init__(self, char_dict):
        self.name = char_dict['name']
        self.species = char_dict['species']
        self.status = char_dict['status']
        self.type = char_dict['type']
        self.gender = char_dict['gender']
        self.origin = char_dict['origin']['name']
        self.location = char_dict['location']['name']


class Aggregator:

    pass


class RequestParser:
    def __init__(self, request):
        self.prefix = request[0]
        self.command = request[1]
        self.argument = request[2]


# url response print
chars = file_processing.list_load()

char_obj_list = []

for i in chars:
    new_char = Character(i)
    char_obj_list.append(new_char)

for i in char_obj_list:
    print(i.name, i.origin, i.status, i.gender, i.species, i.location, i.type)

while True:
    request = RequestParser(input("Please enter your command: ").split())
    print(request.prefix, request.command, request.argument)


# TODO: реализуйте класс Aggregator, который аттрибутом принимает список объектов персонажей и, на основании списка всех персонажей, может вывести на экран саггрегированную информацию:
#
# TODO: возможность получить кол-во персонажей по каждому признаку (ключу), указанному выше
# >>> show status alive
# >>> выводит на экран кол-во живых персонажей
#
# >>> show species human
# >>> выводит кол-во людей
#
# TODO: возможность вывести на экран общую аггрегацию по признаку
# >>> show status
# >>> Alive 100
# >>> unknown 37
# ...
#
# >>> show location
# >>> Citadel of Ricks 19
# >>> Earth (Replacement Dimension) 33
# ...
#
