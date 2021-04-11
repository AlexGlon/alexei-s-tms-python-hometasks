import typing

input_array = [1, 5, 5, 25, 125, 3, 9, 9, 27]


def get_triplets_count(arr: typing.List[int], ratio: int) -> int:
    count = 0
    checklist = []
    for iter in arr:
        i = arr.count(iter)
        j = arr.count(iter * ratio)
        k = arr.count(iter * ratio * ratio)
        if iter not in checklist:
            checklist.append(iter)
            count += i * j * k
    print(count)
    return count


assert get_triplets_count(input_array, 5) == 4
assert get_triplets_count(input_array, 3) == 4
