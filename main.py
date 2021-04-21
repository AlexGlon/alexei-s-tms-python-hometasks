import file_processing
import character as char
import aggregator as agg
import request_parser as req

chars = file_processing.list_load()

char_obj_list = []
for i in chars:
    new_char = char.Character(name=i['name'], type=i['type'], gender=i['gender'], location=i['location']['name'], origin=i['origin']['name'], status=i['status'], species=i['species'])
    char_obj_list.append(new_char)

char_aggregator = agg.Aggregator(char_obj_list)

while True:
    request = req.RequestParser(input("Please enter your command: ").split())
    char_aggregator.command_handler(request)
