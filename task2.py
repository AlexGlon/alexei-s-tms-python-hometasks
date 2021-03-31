balance = 0
operation = input('Enter the operations in the following format: \"ADD:__  SUB:__\":\n')
print(operation)
add = operation.split()
print(add)
addNo = add[0].split(':')[-1]
subNo = add[1].split(':')[-1]
print(addNo, subNo)
sub = 46
# TODO: check if the input string follows the declared format, otherwise ask the user to enter it once again
# TODO: "not int in __ input" exception