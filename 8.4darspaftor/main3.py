#    https://www.codewars.com/kata/5f8a15c06dbd530016be0c19/train/python


def duplicate_sandwich(seq):
    positions = {}
    max_length = 0
    result = []

    for i, element in enumerate(seq):
        if element in positions:
            start = positions[element]
            subseq = seq[start + 1:i]
            if len(subseq) > max_length:
                max_length = len(subseq)
                result = subseq
        positions[element] = i

    return result


print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))  # [2, 3, 4, 5, 6]
print(duplicate_sandwich(['None', 'Hello', 'Example', 'hello', 'None', 'Extra']))
print(duplicate_sandwich([0, 0]))
print(duplicate_sandwich([True, False, True]))
print(duplicate_sandwich(['e', 'x', 'a', 'm', 'p', 'l', 'e']))
