import typing

input_array = [1, 5, 5, 25, 125, 3, 9, 9, 27]


def get_triplets_count(arr: typing.List[int], ratio: int) -> int:
    count = 0
    for i in range(len(arr)):
        # print(f"i = {i}, arr[i] = {arr[i]}")
        for k in range(i+1, len(arr)):
            # print(f"{k}) arr[k] = {arr[k]}")
            if arr[i] * ratio == arr[k]:
                # print(f"{k}) arr[k] {arr[k]} follows the ratio pattern")
                for l in range(k+1, len(arr)):
                    if arr[k] * ratio == arr[l]:
                        # print(f"{l})) arr[l] = {arr[l]}")
                        count += 1
    print(count)
    return count


assert get_triplets_count(input_array, 5) == 4
assert get_triplets_count(input_array, 3) == 4
