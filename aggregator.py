class Aggregator:
    def __init__(self, char_list):
        self.char_list = char_list

    def key_info(self, request):
        """Iterates over every `Character` object in the total list and counts how many fit the specified key-value pair."""
        total = 0

        for i in self.char_list:
            if request.get_argument().upper() == i.get_value(request.get_command()).upper():
                total += 1

        print(total)

    def field_info(self, request):
        """Iterates over every `Character` object in the total list and aggregates all information in the specified key."""
        total = {}

        for i in self.char_list:
            if i.get_value(request.get_command()) not in total.keys():
                total.update({
                    i.get_value(request.get_command()): 1
                })
            else:
                total[i.get_value(request.get_command())] += 1

        for i in total:
            print(f"{i}: {total[i]}")

    def command_handler(self, request):
        """Handles which command should be called depending on the user's request."""
        if request.get_argument() == '':
            self.field_info(request)
        else:
            self.key_info(request)
