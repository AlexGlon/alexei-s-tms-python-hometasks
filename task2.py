def balance_processing(balance, plus, minus):
    return balance + plus - minus


def format_check(string):
    """Checks whether user input follows the defined ADD/SUB format."""
    return string[0].split(':')[0].upper() != "ADD" or string[1].split(':')[0].upper() != "SUB"


def welcome_message():
    return input('Enter an operation in the following format: \"ADD:__  SUB:__\" (or enter \"EXIT\" to exit):\n')


def extraction(string, n):
    """Extracts valuables from split input string."""
    return float(string[n].split(':')[-1])


def main():
    balance = 0
    while True:
        user_input = welcome_message()
        if user_input == 'EXIT':
            break
        operations = user_input.split()
        try:
            if format_check(operations):
                raise Exception('Invalid input format. Please try again.')
                continue
            add = extraction(operations, 0)
            sub = extraction(operations, 1)
        except:
            print('Invalid input format. Please try again.')
            continue
        balance = balance_processing(balance, add, sub)
        print(f"Your current balance is ${balance}.\nThanks for banking with us!\n")


if __name__ == "__main__":
    main()
