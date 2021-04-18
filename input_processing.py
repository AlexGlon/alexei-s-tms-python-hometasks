import commands

# TODO: rework this function's logic so that it parses all the arguments
# TODO: break down this function's logic into separate funcs maybe?


def input_interpreter(user_input: str) -> None:
    """Parses all arguments and calls a specific request handler function"""
    input_list = user_input.split()

    command = input_list[0].lower()

    command_handler = {
        'show': commands.show,
        'urlcontains': commands.contains_handler,
        'titlecontains': commands.contains_handler,
        'author': commands.contains_handler,
        'save': commands.save,
        'load': commands.load,
        'help': commands.help
    }

    if command not in command_handler.keys():
        print("Invalid command. Please try again.")
        return

    # dictionary of arguments initialized with default values

    # TODO: implement handling of cases where search string has spaces
    # TODO: more arguments for load/save functions

    arg_dict = {
        'load': 30,
        'keyword': '',
        'pick': 10,
        'toprating': (lambda arg=input_list[1]: True if arg.lower() == 'toprating' else False)(),
        'points_arg': False,
        'points': 100,
        'contains_handler': input_list[0].split('contains')[0]
    }

    # fills `load` and `pick` arguments (and handles a case when the keyword goes after a load argument)
    iteration = 0

    try:
        for i in input_list:
            if i.isnumeric():
                arg_dict['load'] = int(i)
                if input_list[iteration + 1].isnumeric():
                    arg_dict['pick'] = int(input_list[iteration + 1])
                elif input_list[iteration + 1].isalpha():
                    arg_dict['keyword'] = input_list[iteration + 1]
                break
            iteration += 1
    except:
        pass

    try:
        # fills `keyword` argument for sure

        if input_list[1].isalnum():
            arg_dict['keyword'] = input_list[1]

        # fills `points` argument

        if input_list[1].split(':')[0] == 'points' and input_list[1].split(':')[1].isnumeric():
            arg_dict['points_arg'] = True
            arg_dict['points'] = int(input_list[1].split(':')[1])
    except:
        pass

    try:
        command_handler[command](arg_dict)
    except:
        print("Invalid syntax. Please try again.")
