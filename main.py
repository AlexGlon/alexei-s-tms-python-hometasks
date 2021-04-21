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

    def get_value(self, key):
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


class Aggregator:
    def __init__(self, char_list):
        self.char_list = char_list

    def key_info(self, request):
        total = 0

        for i in self.char_list:
            if request.get_argument().upper() == i.get_value(request.get_command()).upper():
                # print(i.get_value(request.get_command()))
                total += 1

        print(total)

    def field_info(self, request):
        total = {}

        for i in self.char_list:
            if i.get_value(request.get_command()) not in total.keys():
                total.update({
                    i.get_value(request.get_command()): 1
                })
            else:
                total[i.get_value(request.get_command())] += 1

        print(total)

    def command_handler(self, request):
        if request.get_argument() == '':
            self.field_info(request)
        else:
            self.key_info(request)


class RequestParser:
    def __init__(self, request):
        self.prefix = request[0].lower()
        self.command = request[1].lower()
        try:
            self.argument = request[2].lower()
        except:
            self.argument = ''

    def get_prefix(self):
        return self.prefix

    def get_command(self):
        return self.command

    def get_argument(self):
        return self.argument


# url response print
chars = file_processing.list_load()

char_obj_list = []

for i in chars:
    new_char = Character(i)
    char_obj_list.append(new_char)

for i in char_obj_list:
    print(i.name, i.origin, i.status, i.gender, i.species, i.location, i.type)
char_aggregator = Aggregator(char_obj_list)

while True:
    request = RequestParser(input("Please enter your command: ").split())
#    print(request.prefix, request.command, request.argument)
    char_aggregator.command_handler(request)


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
