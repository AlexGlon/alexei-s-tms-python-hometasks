balance = 0
while True:
    user_input = input('Enter the operations in the following format: \"ADD:__  SUB:__\" (or enter \"EXIT\" to exit):\n')
    if user_input == 'EXIT':
        break
    operations = user_input.split()
    try:
      add = float(operations[0].split(':')[-1])
      sub = float(operations[1].split(':')[-1])
    except:
        print('Invalid input format. Please try again.')
        continue
    balance = balance - sub + add
    print(f"Your current balance is ${balance}.\nThanks for banking with us!\n")
