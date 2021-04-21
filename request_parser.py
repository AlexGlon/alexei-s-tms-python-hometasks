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
