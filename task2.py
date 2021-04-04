import math
import typing

# Task 2a

def filter(sequence: typing.Iterable, condition: typing.Callable[[int], bool]) -> list:
    elements_list = []
    for i in sequence:
        if i == 0:
            continue
        if condition(i):
            elements_list.append(i)
    print(elements_list)
    return elements_list


def is_square(item: int) -> bool:
    if math.sqrt(item) - math.floor(math.sqrt(item)) == 0:
        return True
    else:
        return False


def is_prime(item: int) -> bool:
    if 1 <= item <= 3:
        return True

    for i in range(2, item):
        if (item % i) == 0:
            return False
    return True


assert filter(range(25), is_square) == [1, 4, 9, 16]
assert filter(range(25), is_prime) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

# Task 2b

def filter(sequence: typing.Iterable, condition: typing.Callable[[str], bool]) -> list:
    elements_list = []
    for i in sequence:
        if condition(i):
            elements_list.append(i)
    print(elements_list)
    return elements_list


def has_three_a(item: str) -> bool:
    if item.count("a") + item.count("A") >= 3:
        return True
    else:
        return False


def is_alpha_title(item: str) -> bool:
    if item.istitle():
        item = item.split()
        for i in item:
            if i.isalpha():
                continue
            else:
                return False
        return True
    else:
        return False


strings = [
    'Abrakadabra',
    'Abc Abc B',
    'Abc Abc Abc',
    'Chapter 1: Abrakadabra',
    'abc abc abc',
    'awd',
]

assert filter(strings, has_three_a) == ['Abrakadabra', 'Abc Abc Abc', 'Chapter 1: Abrakadabra', 'abc abc abc',]
assert filter(strings, is_alpha_title) == ['Abrakadabra', 'Abc Abc B', 'Abc Abc Abc',]

# Task 2c

initial = [(1, 2, 1), (1, 2, 5), (1, 2, 10), (1, 1, 1), (1, 1, 10), (0, 10, 10), (0, 9, 5)]
result = []

# можно ли это реализовать в одну строку?..
result = sorted(initial, key = lambda initial: initial[2], reverse = True)
result = sorted(result, key = lambda result: result[1])
result = sorted(result, key = lambda result: result[0])
print(result)

assert result == [(0, 9, 5), (0, 10, 10), (1, 1, 10), (1, 1, 1), (1, 2, 10), (1, 2, 5), (1, 2, 1)]

