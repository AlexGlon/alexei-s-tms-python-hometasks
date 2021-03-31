balance = 0
while True:
    operation = input('Enter the operations in the following format: \"ADD:__  SUB:__\":\n')
    add = operation.split()
    print(add)
    addNo = float(add[0].split(':')[-1])
    subNo = float(add[1].split(':')[-1])
    print(addNo, subNo)
    balance = balance - subNo + addNo
    print(f"Your current balance is ${balance}.\nThanks for banking with us!\n")
# TODO: check if the input string follows the declared format, otherwise ask the user to enter it once again
# TODO: "not int in __ input" exception
