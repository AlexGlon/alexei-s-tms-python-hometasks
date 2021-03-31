# Task 1
numbers = '1,100,15,17,3,221,9,5,7,2,8,11'
result = {}

# Solution 1
for i in numbers.split(','):
    result.update({int(i): int(i)*int(i)*int(i)})
print(result)

result = {}

# Solution 2
# кажется этот вариант можно было как-то попроще сделать
numbers_list = numbers.split(',')
i = 0
while i < len(numbers_list):
    result.update({int(numbers_list[i]): int(numbers_list[i]) * int(numbers_list[i]) * int(numbers_list[i])})
    i += 1
print(result)

result = {}

# Solution 3
result = {
    int(i): int(i)*int(i)*int(i)
    for i in numbers.split(',')
}
print(result)

# Тесты
assert all(number in result and result[number] == number * number * number for number in (1, 100, 15, 17, 3, 221, 9, 5, 7, 2, 8, 11))
