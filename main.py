import input_processing as input_proc

while True:
    user_input = input("Please enter your command (or enter 'EXIT' to exit):")
    if user_input.upper() == 'EXIT':
        break
    input_proc.input_interpreter(user_input)
